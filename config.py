# File path definitions to access game files
PATH = {
    # The Minecraft assets folder (contains 'indexes', 'objects', and 'skins' subfolders)
    "assets": "%AppData%/.minecraft/assets",
    # Which index file to use when looking for LANG files (in the 'indexes' subfolder)
    "index_file": "19.json",
    # Path to the Minecraft JAR archive
    "mc_jar": "%AppData%/.minecraft/versions/1.21.4/1.21.4.jar",
    # Filepath to save the resource pack to
    "rp_dest": "%AppData%/.minecraft/resourcepacks/Redstone Tweaks 2.4.7.zip",
}

# Space around container inventory GUI
INV_MARGIN = 4
# Space around item name tooltip
TT_MARGIN = 4
# Space escape sequence definitions
# Additional in-game GUI space definitions are found near the bottom in the no-edit zone
SPACE = {}

# Whether to generate a ResPackOpts file alongside the lang files
GENERATE_RPO = True

# The LANG format string definitions. See the README to learn more about how they work
# Comment an entry to disable its generation
LANG = {
    # Buttons (signal duration)
    "${activation_duration}block.minecraft.acacia_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.bamboo_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.birch_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.cherry_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.crimson_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.dark_oak_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.jungle_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.mangrove_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.oak_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.pale_oak_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.polished_blackstone_button": "{lang.value} {glyph.clock}1s",
    "${activation_duration}block.minecraft.spruce_button": "{lang.value} {glyph.clock}≥1.5s",
    "${activation_duration}block.minecraft.stone_button": "{lang.value} {glyph.clock}1s",
    "${activation_duration}block.minecraft.warped_button": "{lang.value} {glyph.clock}≥1.5s",
    # Pressure Plates (signal duration)
    "${activation_duration}block.minecraft.acacia_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.bamboo_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.birch_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.cherry_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.crimson_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.dark_oak_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.heavy_weighted_pressure_plate": "{lang.value} {glyph.clock}≥0.5s",
    "${activation_duration}block.minecraft.jungle_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.light_weighted_pressure_plate": "{lang.value} {glyph.clock}≥0.5s",
    "${activation_duration}block.minecraft.mangrove_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.oak_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.pale_oak_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.polished_blackstone_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.spruce_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.stone_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    "${activation_duration}block.minecraft.warped_pressure_plate": "{lang.value} {glyph.clock}≥1s",
    # Other Redstone Components (signal duration & comparator chart)
    "${sculk_both}block.minecraft.calibrated_sculk_sensor": "{lang.value} {glyph.clock}0.5s{align.left}{format.white}{glyph.sculk_sensor_guide}",
    "+${sculk_chart}block.minecraft.calibrated_sculk_sensor": "{lang.value}{align.left}{format.white}{glyph.sculk_sensor_guide}",
    "+${sculk_duration}block.minecraft.calibrated_sculk_sensor": "{lang.value} {glyph.clock}0.5s",
    "${ss_decorated_pot}block.minecraft.decorated_pot": "{lang.value}{align.left}{format.white}{glyph.decorated_pot_guide}",
    "${activation_duration}block.minecraft.detector_rail": "{lang.value} {glyph.clock}≥1s",
    "${jukebox}block.minecraft.jukebox": "{lang.value}{align.left}{format.white}{glyph.jukebox_guide}",
    "${activation_duration}block.minecraft.lectern": "{lang.value} {glyph.clock}0.1s",
    "${activation_duration}block.minecraft.lightning_rod": "{lang.value} {glyph.clock}0.4s",
    "${sculk_both}block.minecraft.sculk_sensor": "{lang.value} {glyph.clock}1.5s{align.left}{format.white}{glyph.sculk_sensor_guide}",
    "+${sculk_chart}block.minecraft.sculk_sensor": "{lang.value}{align.left}{format.white}{glyph.sculk_sensor_guide}",
    "+${sculk_duration}block.minecraft.sculk_sensor": "{lang.value} {glyph.clock}1.5s",
    "${activation_duration}block.minecraft.target": "{lang.value} {glyph.clock}0.4s,1s",
    "${activation_duration}block.minecraft.trapped_chest": "{lang.value} {glyph.clock}≥0.05s",
    "${activation_duration}block.minecraft.tripwire_hook": "{lang.value} {glyph.clock}≥0.5s",
    # Brewing Stand (brewing guide)
    "${ss_brewing}container.brewing": "{align.before}{format.white}{glyph.brewing_stand_guide_left}{align.middle}{format.reset}{lang.value}{align.after}{format.white}{glyph.brewing_stand_guide_right}",
    # Container Inventories (comparator chart)
    "${ss_barrel}container.barrel": "{lang.value}{align.after}{format.white}{glyph.barrel_guide}",
    "${ss_furnaces}container.blast_furnace": "{lang.value}{align.after}{format.white}{glyph.blast_furnace_guide}",
    "${ss_chests}container.chest": "{lang.value}{align.after}{format.white}{glyph.chest_guide}",
    "${ss_chests}container.chestDouble": "{lang.value}{align.after}{format.white}{glyph.large_chest_guide}",
    "${ss_droppers}container.dispenser": "{lang.value}{align.after}{format.white}{glyph.dispenser_guide}",
    "${ss_droppers}container.dropper": "{lang.value}{align.after}{format.white}{glyph.dropper_guide}",
    "${ss_furnaces}container.furnace": "{lang.value}{align.after}{format.white}{glyph.furnace_guide}",
    "${ss_hopper}container.hopper": "{lang.value}{align.after}{format.white}{glyph.hopper_guide}",
    "${ss_shulker}container.shulkerBox": "{lang.value}{align.after}{format.white}{glyph.shulker_box_guide}",
    "${ss_furnaces}container.smoker": "{lang.value}{align.after}{format.white}{glyph.smoker_guide}",
    "${ss_chest_minecart}entity.minecraft.chest_minecart": "{lang.value}{align.after}{format.white}{glyph.chest_guide}",
    "${ss_hopper_minecart}entity.minecraft.hopper_minecart": "{lang.value}{align.after}{format.white}{glyph.hopper_guide}",
    # Music Discs (signal strength & song duration)
    "${discs}jukebox_song.minecraft.11": "{lang.value} {format.white}{glyph.comparator}{format.reset}11{format.white}{glyph.clock}{format.reset}1:12.1",
    "${discs}jukebox_song.minecraft.13": "{lang.value} {format.white}{glyph.comparator}{format.reset}1{format.white}{glyph.clock}{format.reset}2:59.1",
    "${discs}jukebox_song.minecraft.5": "{lang.value} {format.white}{glyph.comparator}{format.reset}15{format.white}{glyph.clock}{format.reset}2:59.1",
    "${discs}jukebox_song.minecraft.blocks": "{lang.value} {format.white}{glyph.comparator}{format.reset}3{format.white}{glyph.clock}{format.reset}5:46.1",
    "${discs}jukebox_song.minecraft.cat": "{lang.value} {format.white}{glyph.comparator}{format.reset}2{format.white}{glyph.clock}{format.reset}3:06.1",
    "${discs}jukebox_song.minecraft.chirp": "{lang.value} {format.white}{glyph.comparator}{format.reset}4{format.white}{glyph.clock}{format.reset}3:06.1",
    "${discs}jukebox_song.minecraft.creator_music_box": "{lang.value} {format.white}{glyph.comparator}{format.reset}11{format.white}{glyph.clock}{format.reset}1:14.1",
    "${discs}jukebox_song.minecraft.creator": "{lang.value} {format.white}{glyph.comparator}{format.reset}12{format.white}{glyph.clock}{format.reset}2:57.1",
    "${discs}jukebox_song.minecraft.far": "{lang.value} {format.white}{glyph.comparator}{format.reset}5{format.white}{glyph.clock}{format.reset}2:55.1",
    "${discs}jukebox_song.minecraft.mall": "{lang.value} {format.white}{glyph.comparator}{format.reset}6{format.white}{glyph.clock}{format.reset}3:18.1",
    "${discs}jukebox_song.minecraft.mellohi": "{lang.value} {format.white}{glyph.comparator}{format.reset}7{format.white}{glyph.clock}{format.reset}1:37.1",
    "${discs}jukebox_song.minecraft.otherside": "{lang.value} {format.white}{glyph.comparator}{format.reset}14{format.white}{glyph.clock}{format.reset}3:16.1",
    "${discs}jukebox_song.minecraft.pigstep": "{lang.value} {format.white}{glyph.comparator}{format.reset}13{format.white}{glyph.clock}{format.reset}2:30.1",
    "${discs}jukebox_song.minecraft.precipice": "{lang.value} {format.white}{glyph.comparator}{format.reset}13{format.white}{glyph.clock}{format.reset}5:00.1",
    "${discs}jukebox_song.minecraft.relic": "{lang.value} {format.white}{glyph.comparator}{format.reset}14{format.white}{glyph.clock}{format.reset}3:39.1",
    "${discs}jukebox_song.minecraft.stal": "{lang.value} {format.white}{glyph.comparator}{format.reset}8{format.white}{glyph.clock}{format.reset}2:31.1",
    "${discs}jukebox_song.minecraft.strad": "{lang.value} {format.white}{glyph.comparator}{format.reset}9{format.white}{glyph.clock}{format.reset}3:09.1",
    "${discs}jukebox_song.minecraft.wait": "{lang.value} {format.white}{glyph.comparator}{format.reset}12{format.white}{glyph.clock}{format.reset}3:59.1",
    "${discs}jukebox_song.minecraft.ward": "{lang.value} {format.white}{glyph.comparator}{format.reset}10{format.white}{glyph.clock}{format.reset}4:12.1",
    "+condition": "false",
    "+fallback": "assets/minecraft/lang/respackopts/{lang.unit}.json",
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

# Allowable lang escape sequence value constants
LANG_UNIT = "unit"
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
