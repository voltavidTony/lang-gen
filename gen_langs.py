# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #
# You do not need to modify this file to edit the generated LANG strings!  #
# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #

from fnmatch import fnmatch
from json import dump, load
from os import chdir, path
from typing import Any, Generator, Iterator

from characters import *
from config import *
from file_tasks import *


def apply_format(
    lang_block: tuple[str, str, int, int], lang_value: str, lang_unit: str, gui_width: int, title_align: str
) -> tuple[str, int, int]:
    text, alignment, before_space, after_space = lang_block
    if alignment == ALIGN_START:
        alignment = title_align

    # Insert original LANG unit and value
    text = text.replace(f"{{{LANG_TAG}.{LANG_UNIT}}}", lang_unit)
    text = text.replace(f"{{{LANG_TAG}.{LANG_VALUE}}}", lang_value)

    # Determine starting and ending positions of a text segment
    text_width = calc_text_width(text)
    if alignment == ALIGN_BEFORE:
        start = -text_width - after_space
    elif alignment == ALIGN_LEFT:
        start = before_space
    elif alignment == ALIGN_MIDDLE:
        start = gui_width // 2 - (text_width + after_space - before_space + 1) // 2
    elif alignment == ALIGN_RIGHT:
        start = gui_width - text_width - after_space
    elif alignment == ALIGN_AFTER:
        start = gui_width + before_space
    else:
        start = 0

    return text, start, start + text_width


def arrange_segments(
    lang_formatters: list[tuple[str, str | int]], alignment: str, lang_key: str
) -> tuple[str, str, int, int]:

    # Get GUI dimensions
    gui_width, title_align, title_offset = GUI_TITLES.get(lang_key, GUI_TITLE_DEFAULT)
    margin = INV_MARGIN if lang_key in GUI_TITLES else TT_MARGIN

    # Determine implicit GUI spaces
    before_space, after_space = 0, 0
    if alignment == ALIGN_BEFORE:
        before_space, after_space = 0, margin
    elif alignment == ALIGN_AFTER:
        before_space, after_space = margin, 0
    elif alignment == ALIGN_START:
        if title_align == ALIGN_LEFT:
            before_space, after_space = title_offset, 0
        elif title_align == ALIGN_MIDDLE:
            before_space, after_space = gui_width - 2 * title_offset, 0

    # Trim space at the start of the section
    while lang_formatters and lang_formatters[0][0] == SPACE_TAG:
        before_space += lang_formatters.pop(0)[1]

    # Trim space at the end of the section
    while lang_formatters and lang_formatters[-1][0] == SPACE_TAG:
        after_space += lang_formatters.pop()[1]

    return (
        "".join(
            # Substitute spacing (remaining) escape sequences
            space_to_chars(fvalue) if ftype == SPACE_TAG else fvalue
            for ftype, fvalue in lang_formatters
        ),
        alignment,
        before_space,
        after_space,
    )


def dump_with_defaults(path: str, content: dict = {}):
    # Get default values
    defaults = {}
    for pattern in KEY_VALUE_DEFAULTS_AND_FILTER.keys():
        if fnmatch(path, pattern):
            defaults = KEY_VALUE_DEFAULTS_AND_FILTER[pattern]
            break

    # Overwrite with existing values
    try:
        with open(path, "r", encoding="utf-8") as in_file:
            existing: dict = load(in_file)
            defaults.update({item: existing[item] for item in defaults if item in existing})
    except FileNotFoundError:
        pass

    # Apply new values
    defaults.update(content)

    # Save to file
    with open(path, "w", encoding="utf-8") as out_file:
        dump(defaults, out_file)


def generate_lang(
    lang_asset: str,
    lang_file: str,
    lang_format: dict[str, tuple[str, str, bool, list[tuple[str, str, int, int]]]],
) -> None:
    print("Processing", path.basename(lang_asset), "->", lang_file)

    # Obtain game lang strings
    with open(lang_asset, "r", encoding="utf-8") as lang_asset:
        lang_asset: dict[str, str] = load(lang_asset)

    # Generate formatted lang strings
    lang_unit = lang_file.split(".")[0]
    lang_content = {}
    rpo_content = {}
    for lang_key, expansion, exclusion, lang_blocks in lang_format:

        # Generate the formatted lang string
        lang_value = lang_asset.get(lang_key, MISSING_KEY)
        lang_gen = recombine_lang(iter(lang_blocks), lang_key, lang_value, lang_unit)

        # Save it to the lang data
        if not exclusion == ONLY_RPO:
            # Every lang_key that is part of lang_content should exist in lang_asset
            if not lang_value:
                print("The following key is missing in this file: ", lang_key)
            lang_content[lang_key] = lang_gen

        # Save it to the RPO data
        if GENERATE_RPO and not exclusion == ONLY_LANG:
            if expansion:
                lang_key = f"${{{expansion}}}{lang_key}"
            rpo_content[lang_key] = lang_gen

    # Save lang strings to file
    dump_with_defaults(f"lang/{lang_file}", lang_content)

    # Generate RPO file
    if GENERATE_RPO:
        # Generate RPO file
        dump_with_defaults(f"lang_rpo/{lang_file}", rpo_content)

        # Generate RPO expansions file
        dump_with_defaults(f"lang_rpo/{lang_file}.rpo")


def parse_escape_sequence(ftype: str, fvalue: str, lang_key: str) -> tuple[str, str | int]:
    # Alignment escape sequence
    if ftype == ALIGN_TAG:
        if not fvalue in ALIGNMENTS:
            raise ValueError(f"Invalid alignment value '{fvalue}' in {lang_key} Expect one of " + str(ALIGNMENTS)[1:-1])
        return ALIGN_TAG, fvalue

    # Formatting code escape sequence
    elif ftype == FORMAT_TAG:
        if not fvalue in FORMAT_TAGS:
            raise ValueError(
                f"Invalid formatting value '{fvalue}' in {lang_key} Expect one of " + str(FORMAT_TAGS.keys())[1:-1]
            )
        return TEXT_TAG, f"§{FORMAT_TAGS[fvalue]}"

    # Custom glyph character escape sequence
    elif ftype == GLYPH_TAG:
        if not fvalue in GLYPHS:
            raise ValueError(
                f"Invalid glyph value '{fvalue}' in {lang_key} " "Check glyph definitions in resource pack"
            )
        return TEXT_TAG, GLYPHS[fvalue]

    # Original LANG value escape sequence
    elif ftype == LANG_TAG:
        if not fvalue in (LANG_UNIT, LANG_VALUE):
            raise ValueError(
                f"Invalid lang value '{fvalue}' in {lang_key} " f"Expect one of '{LANG_UNIT}', '{LANG_VALUE}'"
            )
        return TEXT_TAG, f"{{{LANG_TAG}.{fvalue}}}"

    # Spacing escape sequence
    elif ftype == SPACE_TAG:
        try:
            return SPACE_TAG, int(SPACE.get(fvalue, fvalue))
        except:
            raise ValueError(
                f"Invalid space value '{fvalue}' in {lang_key} "
                f"'{SPACE_TAG}' specifier must be defined in CONFIG or an integer"
            )

    # Text characters not from escape sequences
    elif ftype == TEXT_TAG:
        return TEXT_TAG, fvalue

    # Invalid escape sequence
    else:
        raise ValueError(f"Invalid escape sequence command '{ftype}' in {lang_key}")


def parse_key(lfs_key: str) -> tuple[str, str, str]:
    # Check if LFS contains an exclusion modifier
    if lfs_key[0] in (ONLY_LANG, ONLY_RPO):
        exclusion, lang_key = lfs_key[0], lfs_key[1:]
    else:
        exclusion, lang_key = "", lfs_key

    # Get leading RPO expansion in LFS key
    if lang_key.startswith("${"):
        idx = lang_key.find("}")
        if idx == -1:
            raise ValueError(f"Unfinished RPO expansion in '{lfs_key}'")
        expansion, lang_key = lang_key[2:idx], lang_key[idx + 1 :]
    else:
        expansion = ""

    return lang_key, expansion, exclusion


def precompute_format(lfs_key: str) -> tuple[str, str, str, list[tuple[str, str, int, int]]]:
    cur_section = ALIGN_START
    lang_sections = []
    section_builder = []

    lang_key, expansion, exclusion = parse_key(lfs_key)

    # Arrange each sequence of segments to its appropriate section
    for ftype, fvalue in segment_lang_format(lfs_key):
        if ftype == ALIGN_TAG:
            if not lang_key in GUI_TITLES and not fvalue in ALIGNMENTS_TT:
                # Disallowed alignment value
                raise ValueError(
                    f"Invalid alignment value '{fvalue}' in {lfs_key} Non-inventory titles only support "
                    + str(ALIGNMENTS_TT)[1:-1]
                )

            if section_builder:
                # Arrange current section
                segment = arrange_segments(section_builder, cur_section, lang_key)
                if segment[0]:
                    lang_sections.append(segment)
                # Start new section
                section_builder = []

            cur_section = fvalue
        else:
            # Accumulate section
            section_builder.append((ftype, fvalue))

    return (
        lang_key,
        expansion,
        exclusion,
        sorted(lang_sections, key=lambda ls: ALIGNMENTS.index(ls[1])),
    )


def recombine_lang(
    lang_blocks: Iterator[tuple[str, str, int, int]], lang_key: str, lang_value: str, lang_unit: str
) -> str:
    # TODO: Figure out how to sort the segments in a way that minimizes caret travel

    # Get GUI dimensions
    gui_width, title_align, title_offset = GUI_TITLES.get(lang_key, GUI_TITLE_DEFAULT)

    # Process first LANG block
    lang_text, first_pos, last_pos = apply_format(next(lang_blocks), lang_value, lang_unit, gui_width, title_align)
    if title_align == ALIGN_LEFT and first_pos != title_offset:
        lang_text = space_to_chars(first_pos - title_offset) + lang_text
        first_pos -= 1

    # String maximum dimensions
    caret_min = first_pos
    caret_max = last_pos
    caret = last_pos

    # Process remaining LANG blocks
    for lang_block in lang_blocks:
        text, start, last_pos = apply_format(lang_block, lang_value, lang_unit, gui_width, title_align)
        caret_min, caret_max = min(caret_min, start - 1), max(caret_max + 1, last_pos)
        lang_text += space_to_chars(start - caret - 1)
        lang_text += text
        caret = last_pos

    # Add required padding for centered titles
    if title_align == ALIGN_MIDDLE:
        # Center dimensions around title offset
        caret_min = title_offset - caret_min
        caret_max -= title_offset
        first_pos = title_offset - first_pos
        last_pos -= title_offset

        # Determine extra padding requirements
        if caret_min < caret_max:
            lang_text = space_to_chars(caret_max - first_pos) + lang_text
        elif caret_min > caret_max:
            lang_text += space_to_chars(caret_min - last_pos)

    return lang_text


def segment_lang_format(lang_key: str) -> Generator[tuple[str, str | int], Any, None]:
    escape_builder = ""
    in_escape = False
    text_builder = ""

    for cur_char in LANG[lang_key]:
        # Currently in escape sequence
        if in_escape:
            # Escaped { character
            if cur_char == "{":
                if escape_builder:
                    # Nested escape sequences not supported
                    raise ValueError(
                        f"Invalid escape sequence '{{{escape_builder}{{' in {lang_key} "
                        "Expect closing brace instead of opening brace"
                    )
                text_builder += "{"

                # Exit escape sequence
                escape_builder = ""
                in_escape = False

            # End of escape sequence
            elif cur_char == "}":
                try:
                    # Extract formatter type and value
                    ftype, fvalue = escape_builder.split(".")
                except:
                    raise ValueError(
                        f"Invalid escape sequence '{escape_builder}' in {lang_key} "
                        "Expect a format of <command>.<value>"
                    )
                if not ftype in TAGS:
                    # Invalid escape command
                    raise ValueError(
                        f"Invalid escape sequence command '{ftype}' in {lang_key} Expect one of " + str(TAGS[1:-1])
                    )

                # Parse escape sequence
                ftype, fvalue = parse_escape_sequence(ftype, fvalue, lang_key)
                if ftype == TEXT_TAG:
                    # Text sequence
                    text_builder += fvalue
                else:
                    # Escape sequence
                    if text_builder:
                        # Finish current segment
                        yield TEXT_TAG, text_builder
                        text_builder = ""
                    yield ftype, fvalue

                # Exit escape sequence
                escape_builder = ""
                in_escape = False

            # Part of escape sequence
            else:
                escape_builder += cur_char

        # Start of escape sequence
        elif cur_char == "{":
            escape_builder = ""
            in_escape = True

        # Regular character
        else:
            text_builder += cur_char

    if in_escape:
        # Unfinished escape sequences not supported
        raise ValueError(f"Unfinished escape sequence '{{{escape_builder}' in {lang_key}")

    if text_builder:
        # Finish current segment
        yield TEXT_TAG, text_builder

    # This allows 'precompute_lang' to close the last section without extra logic
    yield ALIGN_TAG, ALIGN_START


def space_to_chars(amount: int) -> str:
    if amount == 0:
        return ""
    elif amount < 0:
        # Negative space character code calculator
        empty = lambda s: chr(0xF800 - s)
        amount = -amount
    else:
        # Positive space character code calculator
        empty = lambda s: chr(0xF800 + s)

    # Construct space character sequence
    return empty(128) * (amount // 128) + "".join(empty(1 << n) for n in range(6, -1, -1) if (1 << n) & amount)


if __name__ == "__main__":
    # Pre-compute LANG format strings
    print("Pre-computing LANG format strings..")
    lang_format = [precompute_format(lang_key) for lang_key in LANG]

    # LANG file generation
    print("Generating LANG files..")
    chdir(path.join(SCRIPT_ROOT, "../assets/minecraft"))
    generate_lang(path.join(SCRIPT_ROOT, "en_us.json"), "en_us.json", lang_format)
    for obj in OBJECTS:
        if obj.startswith("minecraft/lang/"):
            generate_lang(HASH_TO_PATH(OBJECTS[obj]), path.basename(obj), lang_format)
    if GENERATE_RPO:
        # Generate redirection RPO file
        dump_with_defaults("lang/.rpo")

    # Resource pack creation
    if PATH["rp_dest"]:
        print("Saving resource pack..")
        recompress_rp()

    print("Done!")
