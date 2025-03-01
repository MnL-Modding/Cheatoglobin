from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FILES_DIR = SCRIPT_DIR / 'files'

APP_NAME = "cheatoglobin"
APP_DISPLAY_NAME = "Cheatoglobin"

NDS_SAVE_FILENAME_FILTER = "NDS Save Files (*.sav *.SaveRAM);;All Files (*)"

PLAYER_NAMES = (
    "MARIO",
    "LUIGI",
    "KOOPA"
)

PLAYER_COLORS = ( # light, med, dark
    (248, 88, 16),  (244, 24, 16),  (152, 16, 8),
    (48, 232, 136), (56, 184, 136), (32, 128, 96),
    (248, 144, 8),  (240, 112, 16), (168, 88, 8),
)

STAT_NAMES = ((
        "HP",
        "SP",
        "POW",
        "DEF",
        "SPEED",
        "STACHE",
    ), (
        "HP",
        "SP",
    ), (
        "LV",
        "EXP",
    ), (
        "Gear Slot 1",
        "Gear Slot 2",
        "Gear Slot 3",
    )
)

ML_LEVEL_EXP = (0, 30, 93, 193, 358, 603, 866, 1146, 1446, 1796, 2296, 2971, 3671, 4671, 5796, 7296, 9321, 11946, 14834, 17984, 21434, 25034, 28784, 32684, 37059, 42059, 48809, 56709, 64184, 72434, 82784, 93584, 104834, 117959, 132959, 149834, 168584, 189209, 211709, 236084, 262334, 290459, 320459, 352334, 386084, 421709, 459209, 498584, 539834, 582959, 627959, 674834, 721709, 768584, 815459, 862334, 909209, 956084, 1002959, 1049834, 1096709, 1143584, 1190459, 1237334, 1284209, 1331084, 1377959, 1424834, 1471709, 1518584, 1565459, 1612334, 1659209, 1706084, 1752959, 1799834, 1846709, 1893584, 1940459, 1987334, 2034209, 2081084, 2127959, 2174834, 2221709, 2268584, 2315459, 2362334, 2409209, 2456084, 2502959, 2549834, 2596709, 2643584, 2690459, 2737334, 2784209, 2831084, 2877959)
KP_LEVEL_EXP = (0, 84, 174, 302, 448, 646, 946, 1296, 1696, 2146, 2646, 3126, 3776, 4476, 5196, 5996, 7076, 8676, 10876, 13276, 15996, 19696, 23696, 27996, 33496, 40696, 48496, 57896, 66696, 77896, 90496, 104496, 119896, 136696, 154896, 174496, 195496, 217896, 241696, 266896, 293496, 321496, 350896, 381696, 413896, 447496, 482496, 518896, 556696, 595896, 636496, 678496, 720496, 762496, 804496, 846496, 888496, 930496, 972496, 1014496, 1056496, 1098496, 1140496, 1182496, 1224496, 1266496, 1308496, 1350496, 1392496, 1434496, 1476496, 1518496, 1560496, 1602496, 1644496, 1686496, 1728496, 1770496, 1812496, 1854496, 1896496, 1938496, 1980496, 2022496, 2064496, 2106496, 2148496, 2190496, 2232496, 2274496, 2316496, 2358496, 2400496, 2442496, 2484496, 2526496, 2568496, 2610496, 2652496)

RANK_LEVELS = (
    (6, 12, 18, 25, 40),
    (6, 12, 18, 25, 40),
    (10, 20, 40),
)

ITEM_DATA = (
    ("MUSHROOM", "Mushroom"),
    ("MUSHROOM", "Super Mushroom"),
    ("MUSHROOM", "Ultra Mushroom"),
    ("MUSHROOM", "Max Mushroom"),
    ("DRUMSTICK", "Hot Drumstick"),
    ("DRUMSTICK", "Fiery Drumstick"),
    ("DRUMSTICK", "TNT Drumstick"),
    ("NUT", "Nut"),
    ("NUT", "Super Nut"),
    ("NUT", "Ultra Nut"),
    ("NUT", "Max Nut"),
    ("SYRUP", "Syrup Jar"),
    ("SYRUP", "Supersyrup Jar"),
    ("SYRUP", "Ultrasyrup Jar"),
    ("SYRUP", "Max Syrup Jar"),
    ("CANDY", "Star Candy"),
    ("LIFE", "1-Up Mushroom"),
    ("LIFE", "1-Up Deluxe"),
    ("HERB", "Refreshing Herb"),
    ("DUMMY", "DUMMY"),
    ("BEAN", "Heart Bean"),
    ("BEAN", "Special Bean"),
    ("BEAN", "Power Bean"),
    ("CLOCK", "Retry Clock"),
    ("NONE", "DUMMY"),
    ("NONE", "DUMMY"),
)

GEAR_DATA = ( # stat increases: (stat, [add, mult], modifier)   (stat 3 is defense)
    ("NONE", "None",             []),

    ("WEAR", "Thin Wear",        [(3, 0, 5)]),
    ("WEAR", "Picnic Wear",      [(3, 0, 15)]),
    ("WEAR", "Leisure Wear",     [(3, 0, 30)]),
    ("WEAR", "Fighter Wear",     [(2, 0, 5), (3, 0, 25)]),
    ("WEAR", "Heart Wear",       [(0, 0, 10), (3, 0, 80)]),
    ("WEAR", "Brawny Wear",      [(2, 0, 10), (3, 0, 45)]),
    ("WEAR", "Grown-up Wear",    [(3, 0, 50), (4, 0, 10), (5, 0, 10)]),
    ("WEAR", "Koopa Wear",       [(3, 0, 40)]),
    ("WEAR", "Hero Wear",        [(3, 0, 60)]),
    ("WEAR", "Balm Wear",        [(3, 0, 90)]),
    ("WEAR", "Muscle Wear",      [(2, 0, 20), (3, 0, 65)]),
    ("WEAR", "Master Wear",      [(1, 0, 20), (3, 0, 140)]),
    ("WEAR", "King Wear",        [(3, 0, 100)]),
    ("WEAR", "Star Wear",        [(0, 0, 20), (1, 0, 10), (3, 0, 120)]),
    ("WEAR", "D-Star Wear",      [(2, 0, 80)]),
    ("WEAR", "A-OK Wear",        [(0, 0, 30), (1, 0, 10), (2, 0, 20), (3, 0, 150), (4, 0, 20), (5, 0, 20)]),
    ("WEAR", "Rental Wear",      []),

    ("SOCK", "HP Socks",         [(0, 1, 0.2)]),
    ("SOCK", "Deluxe HP Socks",  [(0, 1, 0.3)]),
    ("SOCK", "SP Socks",         [(1, 1, 0.2)]),
    ("SOCK", "DX SP Socks",      [(1, 1, 0.3)]),
    ("SOCK", "Hustle Socks",     []),
    ("SOCK", "Coin Socks",       []),
    ("SOCK", "Starched Socks",   [(3, 1, 0.1)]),
    ("SOCK", "Gumption Socks",   []),
    ("SOCK", "Bro Socks",        []),
    ("SOCK", "Gall Socks",       []),
    ("SOCK", "Rugged Socks",     [(3, 1, 0.2)]),
    ("SOCK", "EXP Socks",        []),
    ("SOCK", "No-touch Socks",   []),
    ("SOCK", "Nurse Socks",      []),
    ("SOCK", "Doctor Socks",     []),
    ("SOCK", "Special Socks",    []),
    ("SOCK", "Surprising Socks", []),
    ("SOCK", "Guardian Socks",   []),

    ("GLOV", "POW Gloves",       [(2, 1, 0.1)]),
    ("GLOV", "DX POW Gloves",    [(2, 1, 0.2)]),
    ("GLOV", "Mushroom Gloves",  []),
    ("GLOV", "Special Gloves",   []),
    ("GLOV", "Heavy Gloves",     []),
    ("GLOV", "Delicious Gloves", []),
    ("GLOV", "Flower Gloves",    []),
    ("GLOV", "Bye-Bye Gloves",   []),
    ("GLOV", "Softener Gloves",  []),
    ("GLOV", "Item Gloves",      []),
    ("GLOV", "Siphon Gloves",    []),
    ("GLOV", "Dent Gloves",      []),

    ("BOOT", "POW Boots",        [(2, 1, 0.1)]),
    ("BOOT", "DX POW Boots",     [(2, 1, 0.2)]),
    ("BOOT", "Tip-Top Boots",    []),
    ("BOOT", "Special Boots",    []),
    ("BOOT", "Heavy Boots",      []),
    ("BOOT", "Daredevil Boots",  []),
    ("BOOT", "Shell Boots",      []),
    ("BOOT", "Dizzy Boots",      []),
    ("BOOT", "Shroob Boots",     []),
    ("BOOT", "Coin Boots",       []),
    ("BOOT", "Siphon Boots",     []),
    ("BOOT", "Big Stomp Boots",  []),
    
    ("MISC", "Happy Charm",      []),
    ("MISC", "Luck Charm",       []),
    ("MISC", "Thrift Charm",     []),
    ("MISC", "Budget Charm",     []),
    ("MISC", "Tight Belt",       []),
    ("MISC", "Advice Patch",     []),
    ("MISC", "Luxury Patch",     []),
    ("MISC", "Heroic Patch",     []),
    ("MISC", "Small Shell",      []),
    ("MISC", "Big Shell",        []),
    ("MISC", "Giant Shell",      []),
    ("MISC", "KO Shell",         []),
    ("MISC", "Gold Ring",        []),
    ("MISC", "Gold Crown",       []),
    ("MISC", "Lazy Scarf",       []),
    ("MISC", "Mushroom Stone",   []),
    ("MISC", "POW Mush Jam",     []),
    ("MISC", "DEF Mush Jam",     []),
    ("MISC", "Treasure Specs",   []),
    ("MISC", "Vengeance Cape",   []),
    ("MISC", "Challenge Medal",  []),

    ("SHEL", "Shabby Shell",     [(3, 0, 20)]),
    ("SHEL", "Special Shell",    [(3, 0, 40)]),
    ("SHEL", "Safety Shell",     [(3, 0, 60)]),
    ("SHEL", "Judge Shell",      [(3, 0, 75)]),
    ("SHEL", "Rock Shell",       [(3, 0, 90)]),
    ("SHEL", "Armored Shell",    [(3, 0, 130)]),
    ("SHEL", "Rampage Shell",    [(2, 0, 20), (3, 0, 100)]),
    ("SHEL", "Dream Shell",      [(3, 0, 220)]),
    ("SHEL", "Wicked Shell",     [(2, 0, 30), (3, 0, 180)]),
    ("SHEL", "Ironclad Shell",   [(3, 0, 300)]),

    ("RING", "Block Ring",       [(3, 1, 0.3)]),

    ("SHEL", "King Shell",       [(1, 0, 20), (2, 0, 20), (3, 0, 260)]),

    ("BAND", "Power Band",       [(2, 1, 0.1)]),
    ("BAND", "Power Band +",     [(2, 1, 0.2)]),
    ("BAND", "Minion Band",      []),
    ("BAND", "Minion Band SP",   []),
    ("BAND", "Iron Fist Band",   []),
    ("BAND", "Vampire Band",     []),
    ("BAND", "Stamina Band",     []),
    ("BAND", "Hunter Band",      []),
    ("BAND", "Lucky Band",       []),
    ("BAND", "Block Band",       [(3, 1, 0.2)]),
    ("BAND", "Fury Band",        []),

    ("FANG", "Power Fangs",      [(2, 1, 0.1)]),
    ("FANG", "Power Fangs X",    [(2, 1, 0.2)]),
    ("FANG", "Special Fangs",    [(1, 1, 0.2)]),
    ("FANG", "Special Fangs X",  [(1, 1, 0.4)]),
    ("FANG", "Red-hot Fangs",    []),
    ("FANG", "Burning Fangs",    []),
    ("FANG", "Fury Fangs",       []),
    ("FANG", "Bone Fangs",       []),
    ("FANG", "Intruder Fangs",   []),
    ("FANG", "Block Fangs",      [(3, 1, 0.2)]),
    ("FANG", "Flashy Fangs",     []),

    ("RING", "Cheap Ring",       []),
    ("RING", "Economy Ring",     []),
    ("RING", "Heroic Ring",      []),
    ("RING", "Glutton Ring",     []),
    ("RING", "Excellent Ring",   []),
    ("RING", "Drumstick Ring",   []),
    ("RING", "Peace Ring",       []),
    ("RING", "Fill-up Ring",     []),
    ("RING", "Restore Ring",     []),
    ("RING", "Fast Cash Ring",   []),
    ("RING", "Treasure Ring",    []),
    ("RING", "Safety Ring",      [(0, 1, 0.2)]),
    ("RING", "Hard Ring",        [(3, 1, 0.2)]),

    ("SHEL", "Rental Shell",     []),
)

GEAR_DISALLOWED_LIST = (
    ("SHEL", "BAND", "FANG", "RING"),
    ("SHEL", "BAND", "FANG", "RING"),
    ("WEAR", "SOCK", "GLOV", "BOOT", "MISC"),
)

BADGE_NAMES = (
    "Mushroom Badge",
    "Powerful Badge",
    "Bonus Badge",
    "Bro Badge",
    "Good Badge",
    "Great Badge",
    "Excellent! Badge",
    "Excellent!! Badge",
)
