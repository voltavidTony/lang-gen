# File path definitions to access game files
PATH = {
    # The Minecraft assets folder (contains 'indexes', 'objects', and 'skins' subfolders)
    "assets": "%AppData%/PrismLauncher/assets",
    # Which index file to use when looking for LANG files (in the 'indexes' subfolder)
    "index_file": "19.json",
    # Path to the Minecraft JAR archive
    "mc_jar": "%AppData%/PrismLauncher/libraries/com/mojang/minecraft/1.21.4/minecraft-1.21.4-client.jar",
    # Filepath to save the resource pack to
    "rp_dest": "%AppData%/PrismLauncher/instances/1.21.4/.minecraft/resourcepacks/Redstone Tweaks 2.4.7.zip",
}

# Space around container inventory GUI
INV_MARGIN = 4
# Space around item name tooltip
TT_MARGIN = 4
# Space escape sequence definitions
# Additional in-game GUI space definitions are found near the bottom in the no-edit zone
SPACE = {}

# The LANG format string definitions. See the README to learn more about how they work
# Comment an entry to disable its generation
LANG = {
    # Buttons (signal duration)
    "block.minecraft.acacia_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.bamboo_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.birch_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.cherry_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.crimson_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.dark_oak_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.jungle_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.mangrove_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.oak_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.pale_oak_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.polished_blackstone_button": "{lang.value} {glyph.clock}1s",
    "block.minecraft.spruce_button": "{lang.value} {glyph.clock}≥1.5s",
    "block.minecraft.stone_button": "{lang.value} {glyph.clock}1s",
    "block.minecraft.warped_button": "{lang.value} {glyph.clock}≥1.5s",
    # Pressure Plates (signal duration)
    "block.minecraft.acacia_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.bamboo_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.birch_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.cherry_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.crimson_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.dark_oak_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.heavy_weighted_pressure_plate": "{lang.value} {glyph.clock}≥0.5s",
    "block.minecraft.jungle_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.light_weighted_pressure_plate": "{lang.value} {glyph.clock}≥0.5s",
    "block.minecraft.mangrove_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.oak_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.pale_oak_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.polished_blackstone_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.spruce_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.stone_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.warped_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    # Other Redstone Components (signal duration & comparator chart)
    "block.minecraft.calibrated_sculk_sensor": "{lang.value} {glyph.clock}0.5s{align.left}{format.white}{glyph.sculk_sensor_guide}",
    "block.minecraft.decorated_pot": "{lang.value}{align.left}{format.white}{glyph.decorated_pot_guide}",
    "block.minecraft.detector_rail": "{lang.value} {glyph.clock}≥1s",
    "block.minecraft.jukebox": "{lang.value}{align.left}{format.white}{glyph.jukebox_guide}",
    "block.minecraft.lectern": "{lang.value} {glyph.clock}0.1s",
    "block.minecraft.lightning_rod": "{lang.value} {glyph.clock}0.4s",
    "block.minecraft.sculk_sensor": "{lang.value} {glyph.clock}1.5s{align.left}{format.white}{glyph.sculk_sensor_guide}",
    "block.minecraft.target": "{lang.value} {glyph.clock}0.4s,1s",
    "block.minecraft.trapped_chest": "{lang.value} {glyph.clock}≥0.05s",
    "block.minecraft.tripwire_hook": "{lang.value} {glyph.clock}≥0.5s",
    # Brewing Stand (brewing guide)
    "container.brewing": "{align.before}{format.white}{glyph.brewing_stand_guide_left}{align.middle}{format.reset}{lang.value}{align.after}{format.white}{glyph.brewing_stand_guide_right}",
    # Container Inventories (comparator chart)
    "container.barrel": "{lang.value}{align.after}{format.white}{glyph.barrel_guide}",
    "container.blast_furnace": "{lang.value}{align.after}{format.white}{glyph.blast_furnace_guide}",
    "container.chest": "{lang.value}{align.after}{format.white}{glyph.chest_guide}",
    "container.chestDouble": "{lang.value}{align.after}{format.white}{glyph.large_chest_guide}",
    "container.dispenser": "{lang.value}{align.after}{format.white}{glyph.dispenser_guide}",
    "container.dropper": "{lang.value}{align.after}{format.white}{glyph.dropper_guide}",
    "container.furnace": "{lang.value}{align.after}{format.white}{glyph.furnace_guide}",
    "container.hopper": "{lang.value}{align.after}{format.white}{glyph.hopper_guide}",
    "container.shulkerBox": "{lang.value}{align.after}{format.white}{glyph.shulker_box_guide}",
    "container.smoker": "{lang.value}{align.after}{format.white}{glyph.smoker_guide}",
    "entity.minecraft.chest_minecart": "{lang.value}{align.after}{format.white}{glyph.chest_guide}",
    "entity.minecraft.hopper_minecart": "{lang.value}{align.after}{format.white}{glyph.hopper_guide}",
    # Music Discs (signal strength & song duration)
    "jukebox_song.minecraft.11": "{lang.value} {format.white}{glyph.comparator}{format.reset}11{format.white}{glyph.clock}{format.reset}1:12.1",
    "jukebox_song.minecraft.13": "{lang.value} {format.white}{glyph.comparator}{format.reset}1{format.white}{glyph.clock}{format.reset}2:59.1",
    "jukebox_song.minecraft.5": "{lang.value} {format.white}{glyph.comparator}{format.reset}15{format.white}{glyph.clock}{format.reset}2:59.1",
    "jukebox_song.minecraft.blocks": "{lang.value} {format.white}{glyph.comparator}{format.reset}3{format.white}{glyph.clock}{format.reset}5:46.1",
    "jukebox_song.minecraft.cat": "{lang.value} {format.white}{glyph.comparator}{format.reset}2{format.white}{glyph.clock}{format.reset}3:06.1",
    "jukebox_song.minecraft.chirp": "{lang.value} {format.white}{glyph.comparator}{format.reset}4{format.white}{glyph.clock}{format.reset}3:06.1",
    "jukebox_song.minecraft.creator_music_box": "{lang.value} {format.white}{glyph.comparator}{format.reset}11{format.white}{glyph.clock}{format.reset}1:14.1",
    "jukebox_song.minecraft.creator": "{lang.value} {format.white}{glyph.comparator}{format.reset}12{format.white}{glyph.clock}{format.reset}2:57.1",
    "jukebox_song.minecraft.far": "{lang.value} {format.white}{glyph.comparator}{format.reset}5{format.white}{glyph.clock}{format.reset}2:55.1",
    "jukebox_song.minecraft.mall": "{lang.value} {format.white}{glyph.comparator}{format.reset}6{format.white}{glyph.clock}{format.reset}3:18.1",
    "jukebox_song.minecraft.mellohi": "{lang.value} {format.white}{glyph.comparator}{format.reset}7{format.white}{glyph.clock}{format.reset}1:37.1",
    "jukebox_song.minecraft.otherside": "{lang.value} {format.white}{glyph.comparator}{format.reset}14{format.white}{glyph.clock}{format.reset}3:16.1",
    "jukebox_song.minecraft.pigstep": "{lang.value} {format.white}{glyph.comparator}{format.reset}13{format.white}{glyph.clock}{format.reset}2:30.1",
    "jukebox_song.minecraft.precipice": "{lang.value} {format.white}{glyph.comparator}{format.reset}13{format.white}{glyph.clock}{format.reset}5:00.1",
    "jukebox_song.minecraft.relic": "{lang.value} {format.white}{glyph.comparator}{format.reset}14{format.white}{glyph.clock}{format.reset}3:39.1",
    "jukebox_song.minecraft.stal": "{lang.value} {format.white}{glyph.comparator}{format.reset}8{format.white}{glyph.clock}{format.reset}2:31.1",
    "jukebox_song.minecraft.strad": "{lang.value} {format.white}{glyph.comparator}{format.reset}9{format.white}{glyph.clock}{format.reset}3:09.1",
    "jukebox_song.minecraft.wait": "{lang.value} {format.white}{glyph.comparator}{format.reset}12{format.white}{glyph.clock}{format.reset}3:59.1",
    "jukebox_song.minecraft.ward": "{lang.value} {format.white}{glyph.comparator}{format.reset}10{format.white}{glyph.clock}{format.reset}4:12.1",
}

# The contents of the RPO file to generate for each language (*.lang.rpo)
# Note that each RPO file will be identical
RPO_CONTENT = {
    # To prevent RPO file generation, remove only the contents of 'RPO_CONTENT', not the entire constant
    "condition": "false",
    "fallback": "assets/minecraft/lang/respackopts/en_us.json",
}

# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #
# Do not modify the contents of this file after this point!    #
# STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP #

from json import load as _load
from os import path as _path

# Allowable escape sequence command constants for parsing
ALIGN_TAG = "align"
FORMAT_TAG = "format"
GLYPH_TAG = "glyph"
LANG_TAG = "lang"
TEXT_TAG = "text"
SPACE_TAG = "space"
# Allowable escape sequences in the LANG format string
TAGS = (ALIGN_TAG, FORMAT_TAG, GLYPH_TAG, LANG_TAG, SPACE_TAG)

# Allowable alignment escape sequence value constants for parsing
#   See the README for a diagram of what they do
ALIGN_BEFORE = "before"
ALIGN_LEFT = "left"
ALIGN_START = "start"
ALIGN_MIDDLE = "middle"
ALIGN_RIGHT = "right"
ALIGN_AFTER = "after"
# Left to right order of alignments
ALIGNMENTS = (ALIGN_BEFORE, ALIGN_LEFT, ALIGN_START, ALIGN_MIDDLE, ALIGN_RIGHT, ALIGN_AFTER)
# Valid non-inventory title alignments
ALIGNMENTS_TT = (ALIGN_BEFORE, ALIGN_LEFT, ALIGN_START)

# Allowable formatting codes
FORMAT_TAGS = {
    "black": "0",
    "dark_blue": "1",
    "dark_green": "2",
    "dark_aqua": "3",
    "dark_red": "4",
    "dark_purple": "5",
    "gold": "6",
    "gray": "7",
    "dark_gray": "8",
    "blue": "9",
    "green": "a",
    "aqua": "b",
    "red": "c",
    "light_purple": "d",
    "yellow": "e",
    "white": "f",
    "obfuscated": "k",
    "bold": "l",
    "strikethrough": "m",
    "underlined": "n",
    "italic": "o",
    "reset": "r",
}

# List of inventory titles and their alignments (map of LANG keys)
GUI_TITLES = {
    "block.minecraft.beacon.primary": (230, ALIGN_MIDDLE, 61),
    "block.minecraft.beacon.secondary": (230, ALIGN_MIDDLE, 168),
    "container.barrel": (176, ALIGN_LEFT, 8),
    "container.blast_furnace": (176, ALIGN_MIDDLE, 88),
    "container.brewing": (176, ALIGN_MIDDLE, 88),
    "container.cartography_table": (176, ALIGN_LEFT, 8),
    "container.chest": (176, ALIGN_LEFT, 8),
    "container.chestDouble": (176, ALIGN_LEFT, 8),
    "container.crafter": (176, ALIGN_MIDDLE, 88),
    # NOTE: container.crafting is omitted since it is used twice with different anchors,
    #       once in the player inventory and once in the crafting table
    "container.dispenser": (176, ALIGN_MIDDLE, 88),
    "container.dropper": (176, ALIGN_MIDDLE, 88),
    "container.enchant": (176, ALIGN_LEFT, 8),
    "container.enderchest": (176, ALIGN_LEFT, 8),
    "container.furnace": (176, ALIGN_MIDDLE, 88),
    "container.grindstone_title": (176, ALIGN_LEFT, 8),
    "container.hopper": (176, ALIGN_LEFT, 8),
    "container.loom": (176, ALIGN_LEFT, 8),
    "container.repair": (176, ALIGN_LEFT, 60),  # Anvil
    "container.shulkerBox": (176, ALIGN_LEFT, 8),
    "container.smoker": (176, ALIGN_MIDDLE, 88),
    "container.stonecutter": (176, ALIGN_LEFT, 8),
    "container.upgrade": (176, ALIGN_LEFT, 44),  # Smithing table
    "entity.minecraft.*_chest_boat": (176, ALIGN_LEFT, 8),
    "entity.minecraft.bamboo_chest_raft": (176, ALIGN_LEFT, 8),
    "entity.minecraft.camel": (176, ALIGN_LEFT, 8),
    "entity.minecraft.chest_minecart": (176, ALIGN_LEFT, 8),
    "entity.minecraft.donkey": (176, ALIGN_LEFT, 8),
    "entity.minecraft.hopper_minecart": (176, ALIGN_LEFT, 8),
    "entity.minecraft.horse": (176, ALIGN_LEFT, 8),
    "entity.minecraft.llama": (176, ALIGN_LEFT, 8),
    "entity.minecraft.mule": (176, ALIGN_LEFT, 8),
    "entity.minecraft.skeleton_horse": (176, ALIGN_LEFT, 186),
    "entity.minecraft.villager.*": (276, ALIGN_MIDDLE, 186),
    "entity.minecraft.wandering_trader": (276, ALIGN_MIDDLE, 96),
    "entity.minecraft.zombie_horse": (176, ALIGN_LEFT, 8),
    "merchant.trades": (276, ALIGN_MIDDLE, 52),  # Title for trades list
}

# The default text alignment for non-inventory titles (i.e. tooltips)
GUI_TITLE_DEFAULT = (0, ALIGN_LEFT, 4)

# Allowable lang escape sequence value constant
LANG_VALUE = "value"

# Additional definitions for space values based on in-game GUI dimensions
SPACE.update(
    {
        # The travel of the text dropshadow
        "dropshadow": 1,
        # Amount of space around the outside of the inventory GUI edges
        "inv_margin": INV_MARGIN,
        "inv_margin_n": -INV_MARGIN,
        # Width of an inventory slot
        "inv_slot": 18,
        "inv_slot_n": -18,
        # Amount of space around the outside of the tooltip GUI edges
        "tt_margin": TT_MARGIN,
        "tt_margin_n": -TT_MARGIN,
    }
)

# Object hash to file path converter
HASH_TO_PATH = lambda h: _path.join(_path.expandvars(PATH["assets"]), "objects", h[:2], h)

# Objects file provided by the game
with open(
    _path.join(_path.expandvars(PATH["assets"]), "indexes", PATH["index_file"])
) as _index_file:
    OBJECTS: dict[str, str] = {
        obj: info["hash"] for obj, info in _load(_index_file)["objects"].items()
    }

# The path that the scripts are in
SCRIPT_ROOT: str = _path.dirname(__file__)
