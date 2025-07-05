# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #
# You do not need to modify this file to edit the generated LANG strings!  #
# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #

from os import chdir as _cd, path as _path, walk as _walk
from zipfile import ZipFile as _ZipFile, ZIP_DEFLATED as _ZIP_DEFLATED

from config import (
    HASH_TO_PATH as _HTP,
    OBJECTS as _OBJECTS,
    PATH as _PATH,
    SCRIPT_ROOT as _SCRIPT_ROOT,
)


def _copy_files():
    # Files only found in the Minecraft jar
    with _ZipFile(_path.expandvars(_PATH["mc_jar"])) as mc_jar:
        for file in (
            "assets/minecraft/font/include/default.json",
            "assets/minecraft/font/include/space.json",
            "assets/minecraft/lang/en_us.json",
            "assets/minecraft/textures/font/accented.png",
            "assets/minecraft/textures/font/ascii.png",
            "assets/minecraft/textures/font/nonlatin_european.png",
        ):
            with open(_path.join(_SCRIPT_ROOT, _path.basename(file)), "wb") as asset_file:
                asset_file.write(mc_jar.read(file))
    # unifont.json
    with open(_HTP(_OBJECTS["minecraft/font/include/unifont.json"])) as uni_obj:
        with open(_path.join(_SCRIPT_ROOT, "unifont.json"), "w") as uni_json:
            uni_json.write(uni_obj.read())
    # All characters Unifont
    with _ZipFile(_HTP(_OBJECTS["minecraft/font/unifont.zip"])) as uni_all:
        uni_all.extractall(_SCRIPT_ROOT)
    # JP patch Unifont
    with _ZipFile(_HTP(_OBJECTS["minecraft/font/unifont_jp.zip"])) as uni_jp:
        uni_jp.extractall(_SCRIPT_ROOT)


def recompress_rp():
    _cd(_path.join(_SCRIPT_ROOT, ".."))

    # Compress resource pack files and save the archive to the specified destination
    with _ZipFile(_path.expandvars(_PATH["rp_dest"]), "w", _ZIP_DEFLATED, True, 9) as rp_archive:
        for root, _, files in _walk("."):
            if not _path.abspath(root).startswith(_SCRIPT_ROOT):
                for file in files:
                    rp_archive.write(_path.join(root, file))


if __name__ == "__main__":
    # Run file task
    _copy_files()
