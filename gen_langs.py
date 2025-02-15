# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #
# You do not need to modify this file to edit the generated LANG strings!  #
# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #

from json import dump, load
from os import chdir, path
from typing import Any, Generator, Iterator

from characters import *
from config import *
from file_tasks import *


def apply_format(lang_block: tuple[str, str, int, int], lang_value: str) -> tuple[str, int, int]:
    text, alignment, before_space, after_space = lang_block

    # Insert original LANG value
    text = text.replace(f"{{{LANG_TAG}.{LANG_VALUE}}}", lang_value)

    # Determine starting and ending positions of a text segment
    width = calc_text_width(text)
    if alignment == ALIGN_BEFORE:
        start = -width - after_space
    elif alignment == ALIGN_LEFT:
        start = before_space
    elif alignment == ALIGN_MIDDLE:
        start = (INV_WIDTH + 1) // 2 - (width + after_space - before_space + 1) // 2
    elif alignment == ALIGN_RIGHT:
        start = INV_WIDTH - width - after_space
    elif alignment == ALIGN_AFTER:
        start = INV_WIDTH + before_space
    else:
        start = 0

    return text, start, start + width


def arrange_segments(
    lang_formatters: list[tuple[str, str | int]], alignment: str
) -> tuple[str, str, int, int]:
    # Trim space at the start of the section
    before_space = 0
    while lang_formatters[0][0] == SPACE_TAG:
        before_space += lang_formatters.pop(0)[1]

    # Trim space at the end of the section
    after_space = 0
    while lang_formatters[-1][0] == SPACE_TAG:
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


def generate_lang(
    lang_source: str, lang_dest: str, lang_format: dict[str, list[tuple[str, str, int, int]]]
) -> None:
    print("Processing", path.basename(lang_source), "->", lang_dest)

    # Generate formatted LANG strings
    with open(lang_source, encoding="utf-8") as lang_file:
        lang_dest_strings = {
            lang_key: recombine_lang(iter(lang_format[lang_key]), lang_key, lang_value)
            for lang_key, lang_value in load(lang_file).items()
            if lang_key in LANG
        }

    # Detect if some keys are missing from the original LANG file
    if len(lang_dest_strings) < len(LANG):
        print("Some keys were missing in this lang file: ", LANG.keys() - lang_dest_strings.keys())

    # Save LANG strings to file
    with open(lang_dest, "w", encoding="utf-8") as lang_file:
        dump(lang_dest_strings, lang_file)

    # Generate ResourcePackOptions file
    if RPO_CONTENT:
        with open(f"{lang_dest}.rpo", "w") as rpo_file:
            dump(RPO_CONTENT, rpo_file)


def parse_escape_sequence(ftype: str, fvalue: str, lang_key: str) -> tuple[str, str | int]:
    # Alignment escape sequence
    if ftype == ALIGN_TAG:
        if not fvalue in ALIGNMENTS:
            raise ValueError(
                f"Invalid alignment value '{fvalue}' in {lang_key} Expect one of "
                + str(ALIGNMENTS)[1:-1]
            )
        return ALIGN_TAG, fvalue

    # Formatting code escape sequence
    elif ftype == FORMAT_TAG:
        if not fvalue in FORMAT_TAGS:
            raise ValueError(
                f"Invalid formatting value '{fvalue}' in {lang_key} Expect one of "
                + str(FORMAT_TAGS.keys())[1:-1]
            )
        return TEXT_TAG, f"§{FORMAT_TAGS[fvalue]}"

    # Custom glyph character escape sequence
    elif ftype == GLYPH_TAG:
        if not fvalue in GLYPHS:
            raise ValueError(
                f"Invalid glyph value '{fvalue}' in {lang_key} "
                "Check glyph definitions in resource pack"
            )
        return TEXT_TAG, GLYPHS[fvalue]

    # Original LANG value escape sequence
    elif ftype == LANG_TAG:
        if not fvalue == LANG_VALUE:
            raise ValueError(
                f"Invalid escape sequence '{LANG_TAG}.{fvalue}' in {lang_key} "
                f"Expect '{LANG_TAG}.{LANG_VALUE}'"
            )
        return TEXT_TAG, f"{{{LANG_TAG}.{LANG_VALUE}}}"

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


def precompute_format(lang_key: str) -> list[tuple[str, str, int, int]]:
    cur_section = ALIGN_MIDDLE if lang_key in CENTERED_TITLES else ALIGN_LEFT
    lang_sections = []
    section_builder = []

    # Arrange each sequence of segments to its appropriate section
    for ftype, fvalue in segment_lang_format(lang_key):
        if ftype == ALIGN_TAG:
            # Apply current section
            if section_builder:
                lang_sections.append(arrange_segments(section_builder, cur_section))
                section_builder = []
            # Start new section
            cur_section = fvalue
        else:
            # Accumulate section
            section_builder.append((ftype, fvalue))

    if section_builder:
        # Accumulate remainder
        lang_sections.append(arrange_segments(section_builder, cur_section))

    return sorted(lang_sections, key=lambda ls: ALIGNMENTS.index(ls[1]))


def recombine_lang(
    lang_blocks: Iterator[tuple[str, str, int, int]], lang_key: str, lang_value: str
) -> str:
    # Process first LANG block
    lang_text, first_pos, caret = apply_format(next(lang_blocks), lang_value)
    if not lang_key in CENTERED_TITLES and caret_min != 0:
        lang_text = space_to_chars(caret_min) + lang_text
        first_pos -= 1

    # String maximum dimensions
    caret_min = first_pos
    caret_max = caret

    # Process remaining LANG blocks
    for lang_block in lang_blocks:
        text, start, last_pos = apply_format(lang_block, lang_value)
        caret_min, caret_max = min(caret_min, start - 1), max(caret_max + 1, last_pos)
        lang_text += space_to_chars(start - caret - 1)
        lang_text += text
        caret = last_pos

    # Add required padding for centered titles
    if lang_key in CENTERED_TITLES:
        # Center dimensions around title offset
        caret_min = INV_WIDTH // 2 - caret_min
        caret_max -= INV_WIDTH // 2
        first_pos = INV_WIDTH // 2 - first_pos
        last_pos -= INV_WIDTH // 2

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
                        f"Invalid escape sequence command '{ftype}' in {lang_key} Expect one of "
                        + str(TAGS[1:-1])
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
    return empty(128) * (amount // 128) + "".join(
        empty(1 << n) for n in range(6, -1, -1) if (1 << n) & amount
    )


if __name__ == "__main__":
    # Pre-compute LANG format strings
    print("Pre-computing LANG format strings..")
    lang_format = {lang_key: precompute_format(lang_key) for lang_key in LANG}

    # LANG file generation
    print("Generating LANG files..")
    chdir(path.join(SCRIPT_ROOT, "../assets/minecraft/lang"))
    generate_lang(path.join(SCRIPT_ROOT, "en_us.json"), "en_us.json", lang_format)
    for obj in OBJECTS:
        if obj.startswith("minecraft/lang/"):
            generate_lang(HASH_TO_PATH(OBJECTS[obj]), path.basename(obj), lang_format)

    # Resource pack creation
    if PATH["rp_dest"]:
        print("Saving resource pack..")
        recompress_rp()

    print("Done!")
