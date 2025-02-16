# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #
# You do not need to modify this file to edit the generated LANG strings!  #
# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #

from PIL import Image as _Img
from json import load as _load
from math import floor as _floor, log2 as _log2
from numpy import (
    apply_along_axis as _aaa,
    arange as _arange,
    array as _array,
    bitwise_or as _or,
    fromiter as _fromiter,
)
from os import listdir as _ls, path as _path

from config import SCRIPT_ROOT as _SCRIPT_ROOT


def calc_text_width(text: str) -> int:
    formatter = False
    n_chars = 0
    width = 0
    for t in text:
        # Ignore formatting code
        if formatter:
            formatter = False
        elif t == "§":
            formatter = True
        else:
            # Normal character
            # Missing characters are 8 pixels wide
            n_chars += 1
            width += CHAR_WIDTHS.get(t, 8) + 1
    return width - int(bool(n_chars))


def _extract_texture_char_widths(provider: dict[str, str | int | list[str]]) -> dict[str, int]:
    # Load font image (check resource pack first, if not found, use default)
    tex_path = _path.join(_SCRIPT_ROOT, "../assets", provider["file"].replace(":", "/textures/"))
    if not _path.exists(tex_path):
        tex_path = _path.join(_SCRIPT_ROOT, _path.basename(tex_path))
    with _Img.open(tex_path) as tex:
        tex_np = _array(tex)

    # Get atlas dimensions
    chars = provider["chars"]
    n_cols = len(chars[0])
    n_rows = len(chars)
    chars = "".join(chars)

    # Get character dimensions
    char_h = tex_np.shape[0] // n_rows
    char_w = tex_np.shape[1] // n_cols
    scale = char_h // provider.get("height", 8)

    # Calculate maximum widths
    tex_np = tex_np.reshape(n_rows, char_h, n_cols, char_w).transpose(0, 2, 1, 3)
    tex_np = _aaa(lambda a: (a * _arange(tex_np.shape[3])).max(), 3, tex_np)
    tex_np = _aaa(lambda a: a.max() + 1, 2, tex_np).ravel()

    # Collect maximum widths
    char_widths = {}
    for n in range(len(chars)):
        char_widths[chars[n]] = int(tex_np[n]) // scale
    del char_widths["\u0000"]  # Don't include null character

    return char_widths


def _extract_unifont_char_widths(
    uni_fname: str, blacklist: set[str], overrides: dict[str, int]
) -> dict[str, int]:
    # Find Unifont file
    for fname in _ls(_SCRIPT_ROOT):
        if fname.startswith(uni_fname):
            break

    # Process file
    char_widths = {}
    with open(_path.join(_SCRIPT_ROOT, fname)) as uni_font:
        for line in uni_font:
            # Read character data
            char, cdata = line.strip().split(":")
            char = chr(int(char, base=16))
            # Don't process characters on the blacklist
            if char in blacklist:
                continue
            # Check for a value override
            if char in overrides:
                char_widths[char] = overrides[char]
                continue
            # Transform each row of pixels (bit array) into an integer
            # Combine each row of a character using bit-or
            n = len(cdata) // 16
            cdata = _or.reduce(
                _fromiter((int(cdata[i : i + n], base=16) for i in range(0, len(cdata), n)), int)
            )
            # width = MSB position - LSB position + 1
            # Unifont characters are rendered at half-size
            if cdata:
                width = (_floor(_log2(cdata)) - _floor(_log2(cdata & ~(cdata - 1))) + 1) // 2
                # Exclude characters rendered with a width of 8
                if width != 8:
                    char_widths[char] = width
            else:
                char_widths[char] = 0

    return char_widths


def _get_char_widths() -> dict[str, int]:
    # Prepare character widths by combining a total of 6 sources

    # 1. Space characters defined by font files (measured in-game)
    char_widths = {
        "\u00a0": 5,
        "\u2000": 5,
        "\u2001": 5,
        "\u2002": 5,
        "\u2003": 5,
        "\u2004": 5,
        "\u2005": 5,
        "\u2006": 5,
        "\u2007": 5,
        "\u2008": 5,
        "\u2009": 5,
        "\u200A": 5,
        "\u202F": 5,
        "\u205F": 5,
        "\u3000": 9,
    }

    # 2. unifont.json width overrides, also used as blacklist
    with open(_path.join(_SCRIPT_ROOT, "unifont.json")) as uni_file:
        # For now, every character on the blacklist is a Unifont character with width 16
        # Thus, the character width map doesn't contain any entries in the blacklist
        blacklist = set()
        overrides = {}
        for uni in _load(uni_file)["providers"]:
            for uni_ranges in uni["size_overrides"]:
                width = (uni_ranges["right"] - uni_ranges["left"] + 1) // 2
                if width == 8:
                    blacklist.update(
                        chr(char)
                        for char in range(ord(uni_ranges["from"]), ord(uni_ranges["to"]) + 1)
                    )
                else:
                    overrides.update(
                        (chr(char), width)
                        for char in range(ord(uni_ranges["from"]), ord(uni_ranges["to"]) + 1)
                    )

    # 3. unifont_all.hex
    char_widths.update(_extract_unifont_char_widths("unifont_all", blacklist, overrides))

    # 4. unifont_jp.hex
    char_widths.update(_extract_unifont_char_widths("unifont_jp_patch", blacklist, overrides))

    # 5. default.json
    with open(_path.join(_SCRIPT_ROOT, "default.json")) as default_file:
        for provider in _load(default_file)["providers"]:
            char_widths.update(_extract_texture_char_widths(provider))

    # 6. space.json
    with open(_path.join(_SCRIPT_ROOT, "space.json")) as space_file:
        spaces = _load(space_file)["providers"][0]["advances"]
        for s in spaces:
            char_widths[s] = spaces[s] - 1

    return char_widths


def _tally():
    # Create a tally of all character widths
    _tally = {_x: 0 for _x in range(-1, 10)}
    for _char, _width in CHAR_WIDTHS.items():
        if ord(_char) < 0xE000 or 0xF8FF < ord(_char):
            _tally[_width] += 1
    print(sum(_tally.values()), "computed characters")
    print(_tally)
    print(
        "Note: The most common blacklist character group is 8 pixels wide. "
        "It has been omitted from the character map to conserve space"
    )


def _width_calculator():
    # Calculate the character width of the input strings
    print("Enter any text to calculate its width in pixels or an empty line to quit.")
    print("Note that the 1 pixel gap is not inserted at the end of the text.")
    while text := input("> ").encode().decode("unicode-escape"):
        print(calc_text_width(text))


print("Obtaining character map..")

# Character width definitions
CHAR_WIDTHS: dict[str, int] = _get_char_widths()

# Glyph character code definitions
GLYPHS: dict[str, str] = {}

# Load custom glyph characters and widths
with open(_path.join(_SCRIPT_ROOT, "../assets/minecraft/font/default.json")) as _def_file:
    for _glyph in _load(_def_file)["providers"]:
        GLYPHS[_glyph["file"].split("/")[-1][:-4]] = _glyph["chars"][0]
        _png = _Img.open(
            _path.join(_SCRIPT_ROOT, "../assets", _glyph["file"].replace(":", "/textures/"))
        )
        # TODO: Investigate further exactly how the game considers character widths for non-integer scaling amounts
        CHAR_WIDTHS[_glyph["chars"][0]] = _png.width * _glyph["height"] // _png.height
    del GLYPHS["empty"]

# Calculate spacing character widths
for _n in (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80):
    CHAR_WIDTHS[chr(0xF800 + _n)] = _n - 1
    CHAR_WIDTHS[chr(0xF800 - _n)] = -_n - 1

if __name__ == "__main__":
    _tally()
    print()
    _width_calculator()
