from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FILES_DIR = SCRIPT_DIR / 'files'

APP_NAME = "cheatoglobin"
APP_DISPLAY_NAME = "Cheatoglobin"

NDS_SAVE_FILENAME_FILTER = "NDS Save Files (*.sav *.SaveRAM);;All Files (*)"

PLAYER_NAMES = (
    "MARIO",
    "LUIGI",
    "BOWSER"
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
        "NEXT",
    ), (
        "Gear Slot 1",
        "Gear Slot 2",
        "Gear Slot 3",
    )
)

STAT_NAMES_LANG = ((
        ("HP:", "HP:", "HP:"),
        ("SP:", "SP:", "SP:"),
        ("POW:", "POW:", "POW:"),
        ("DEF:", "DEF:", "DEF:"),
        ("SPEED:", "SPEED:", "SPEED:"),
        ("STACHE:", "STACHE:", "HORN:"),
    ), (
        ("HP:", "HP:", "HP:"),
        ("SP:", "SP:", "SP:"),
    ), (
        "LV:",
        "EXP:",
        "NEXT LV:",
        "RANK:",
    )
)

ML_LEVEL_EXP = (0, 30, 93, 193, 358, 603, 866, 1146, 1446, 1796, 2296, 2971, 3671, 4671, 5796, 7296, 9321, 11946, 14834, 17984, 21434, 25034, 28784, 32684, 37059, 42059, 48809, 56709, 64184, 72434, 82784, 93584, 104834, 117959, 132959, 149834, 168584, 189209, 211709, 236084, 262334, 290459, 320459, 352334, 386084, 421709, 459209, 498584, 539834, 582959, 627959, 674834, 721709, 768584, 815459, 862334, 909209, 956084, 1002959, 1049834, 1096709, 1143584, 1190459, 1237334, 1284209, 1331084, 1377959, 1424834, 1471709, 1518584, 1565459, 1612334, 1659209, 1706084, 1752959, 1799834, 1846709, 1893584, 1940459, 1987334, 2034209, 2081084, 2127959, 2174834, 2221709, 2268584, 2315459, 2362334, 2409209, 2456084, 2502959, 2549834, 2596709, 2643584, 2690459, 2737334, 2784209, 2831084, 2877959)
KP_LEVEL_EXP = (0, 84, 174, 302, 448, 646, 946, 1296, 1696, 2146, 2646, 3126, 3776, 4476, 5196, 5996, 7076, 8676, 10876, 13276, 15996, 19696, 23696, 27996, 33496, 40696, 48496, 57896, 66696, 77896, 90496, 104496, 119896, 136696, 154896, 174496, 195496, 217896, 241696, 266896, 293496, 321496, 350896, 381696, 413896, 447496, 482496, 518896, 556696, 595896, 636496, 678496, 720496, 762496, 804496, 846496, 888496, 930496, 972496, 1014496, 1056496, 1098496, 1140496, 1182496, 1224496, 1266496, 1308496, 1350496, 1392496, 1434496, 1476496, 1518496, 1560496, 1602496, 1644496, 1686496, 1728496, 1770496, 1812496, 1854496, 1896496, 1938496, 1980496, 2022496, 2064496, 2106496, 2148496, 2190496, 2232496, 2274496, 2316496, 2358496, 2400496, 2442496, 2484496, 2526496, 2568496, 2610496, 2652496)

RANK_LEVELS = (
    (6, 12, 18, 25, 40),
    (6, 12, 18, 25, 40),
    (10, 20, 40),
)

RANK_NAMES = (
    "Mushroom Rank",
    "Shell Rank",
    "Flower Rank",
    "Shine Rank",
    "Star Rank",
    "Rainbow Rank",
    "Bronze Boss Rank",
    "Silver Boss Rank",
    "Gold Boss Rank",
    "Final Boss Rank",
)

ITEM_DATA = (
    ( 0, "Mushroom"),
    ( 0, "Super Mushroom"),
    ( 0, "Ultra Mushroom"),
    ( 0, "Max Mushroom"),
    (40, "Hot Drumstick"),
    (40, "Fiery Drumstick"),
    (40, "TNT Drumstick"),
    (22, "Nut"),
    (22, "Super Nut"),
    (22, "Ultra Nut"),
    (22, "Max Nut"),
    ( 4, "Syrup Jar"),
    ( 4, "Supersyrup Jar"),
    ( 4, "Ultrasyrup Jar"),
    ( 4, "Max Syrup Jar"),
    (41, "Star Candy"),
    ( 1, "1-Up Mushroom"),
    ( 1, "1-Up Deluxe"),
    ( 6, "Refreshing Herb"),
    (21, "DUMMY"),
    (38, "Heart Bean"),
    (38, "Special Bean"),
    (38, "Power Bean"),
    (42, "Retry Clock"),
    ( 2, "DUMMY"),
    ( 2, "DUMMY"),
)

GEAR_DATA = ( # stat increases: (stat, [add, mult], modifier)   (stat 3 is defense)
    ( 2, "None",             []),

    (12, "Thin Wear",        [(3, 0, 5)]),
    (12, "Picnic Wear",      [(3, 0, 15)]),
    (12, "Leisure Wear",     [(3, 0, 30)]),
    (12, "Fighter Wear",     [(2, 0, 5), (3, 0, 25)]),
    (12, "Heart Wear",       [(0, 0, 10), (3, 0, 80)]),
    (12, "Brawny Wear",      [(2, 0, 10), (3, 0, 45)]),
    (12, "Grown-up Wear",    [(3, 0, 50), (4, 0, 10), (5, 0, 10)]),
    (12, "Koopa Wear",       [(3, 0, 40)]),
    (12, "Hero Wear",        [(3, 0, 60)]),
    (12, "Balm Wear",        [(3, 0, 90)]),
    (12, "Muscle Wear",      [(2, 0, 20), (3, 0, 65)]),
    (12, "Master Wear",      [(1, 0, 20), (3, 0, 140)]),
    (12, "King Wear",        [(3, 0, 100)]),
    (12, "Star Wear",        [(0, 0, 20), (1, 0, 10), (3, 0, 120)]),
    (12, "D-Star Wear",      [(2, 0, 80)]),
    (12, "A-OK Wear",        [(0, 0, 30), (1, 0, 10), (2, 0, 20), (3, 0, 150), (4, 0, 20), (5, 0, 20)]),
    (12, "Rental Wear",      []),

    (13, "HP Socks",         [(0, 1, 0.2)]),
    (13, "Deluxe HP Socks",  [(0, 1, 0.3)]),
    (13, "SP Socks",         [(1, 1, 0.2)]),
    (13, "DX SP Socks",      [(1, 1, 0.3)]),
    (13, "Hustle Socks",     []),
    (13, "Coin Socks",       []),
    (13, "Starched Socks",   [(3, 1, 0.1)]),
    (13, "Gumption Socks",   []),
    (13, "Bro Socks",        []),
    (13, "Gall Socks",       []),
    (13, "Rugged Socks",     [(3, 1, 0.2)]),
    (13, "EXP Socks",        []),
    (13, "No-touch Socks",   []),
    (13, "Nurse Socks",      []),
    (13, "Doctor Socks",     []),
    (13, "Special Socks",    []),
    (13, "Surprising Socks", []),
    (13, "Guardian Socks",   []),

    ( 3, "POW Gloves",       [(2, 1, 0.1)]),
    ( 3, "DX POW Gloves",    [(2, 1, 0.2)]),
    ( 3, "Mushroom Gloves",  []),
    ( 3, "Special Gloves",   []),
    ( 3, "Heavy Gloves",     []),
    ( 3, "Delicious Gloves", []),
    ( 3, "Flower Gloves",    []),
    ( 3, "Bye-Bye Gloves",   []),
    ( 3, "Softener Gloves",  []),
    ( 3, "Item Gloves",      []),
    ( 3, "Siphon Gloves",    []),
    ( 3, "Dent Gloves",      []),

    (14, "POW Boots",        [(2, 1, 0.1)]),
    (14, "DX POW Boots",     [(2, 1, 0.2)]),
    (14, "Tip-Top Boots",    []),
    (14, "Special Boots",    []),
    (14, "Heavy Boots",      []),
    (14, "Daredevil Boots",  []),
    (14, "Shell Boots",      []),
    (14, "Dizzy Boots",      []),
    (14, "Shroob Boots",     []),
    (14, "Coin Boots",       []),
    (14, "Siphon Boots",     []),
    (14, "Big Stomp Boots",  []),
    
    (11, "Happy Charm",      []),
    (11, "Luck Charm",       []),
    (11, "Thrift Charm",     []),
    (11, "Budget Charm",     []),
    (11, "Tight Belt",       []),
    (11, "Advice Patch",     []),
    (11, "Luxury Patch",     []),
    (11, "Heroic Patch",     []),
    (11, "Small Shell",      []),
    (11, "Big Shell",        []),
    (11, "Giant Shell",      []),
    (11, "KO Shell",         []),
    (11, "Gold Ring",        []),
    (11, "Gold Crown",       []),
    (11, "Lazy Scarf",       []),
    (11, "Mushroom Stone",   []),
    (11, "POW Mush Jam",     []),
    (11, "DEF Mush Jam",     []),
    (11, "Treasure Specs",   []),
    (11, "Vengeance Cape",   []),
    (11, "Challenge Medal",  []),

    (15, "Shabby Shell",     [(3, 0, 20)]),
    (15, "Special Shell",    [(3, 0, 40)]),
    (15, "Safety Shell",     [(3, 0, 60)]),
    (15, "Judge Shell",      [(3, 0, 75)]),
    (15, "Rock Shell",       [(3, 0, 90)]),
    (15, "Armored Shell",    [(3, 0, 130)]),
    (15, "Rampage Shell",    [(2, 0, 20), (3, 0, 100)]),
    (15, "Dream Shell",      [(3, 0, 220)]),
    (15, "Wicked Shell",     [(2, 0, 30), (3, 0, 180)]),
    (15, "Ironclad Shell",   [(3, 0, 300)]),

    (16, "Block Ring",       [(3, 1, 0.3)]),

    (15, "King Shell",       [(1, 0, 20), (2, 0, 20), (3, 0, 260)]),

    (17, "Power Band",       [(2, 1, 0.1)]),
    (17, "Power Band +",     [(2, 1, 0.2)]),
    (17, "Minion Band",      []),
    (17, "Minion Band SP",   []),
    (17, "Iron Fist Band",   []),
    (17, "Vampire Band",     []),
    (17, "Stamina Band",     []),
    (17, "Hunter Band",      []),
    (17, "Lucky Band",       []),
    (17, "Block Band",       [(3, 1, 0.2)]),
    (17, "Fury Band",        []),

    (18, "Power Fangs",      [(2, 1, 0.1)]),
    (18, "Power Fangs X",    [(2, 1, 0.2)]),
    (18, "Special Fangs",    [(1, 1, 0.2)]),
    (18, "Special Fangs X",  [(1, 1, 0.4)]),
    (18, "Red-hot Fangs",    []),
    (18, "Burning Fangs",    []),
    (18, "Fury Fangs",       []),
    (18, "Bone Fangs",       []),
    (18, "Intruder Fangs",   []),
    (18, "Block Fangs",      [(3, 1, 0.2)]),
    (18, "Flashy Fangs",     []),

    (16, "Cheap Ring",       []),
    (16, "Economy Ring",     []),
    (16, "Heroic Ring",      []),
    (16, "Glutton Ring",     []),
    (16, "Excellent Ring",   []),
    (16, "Drumstick Ring",   []),
    (16, "Peace Ring",       []),
    (16, "Fill-up Ring",     []),
    (16, "Restore Ring",     []),
    (16, "Fast Cash Ring",   []),
    (16, "Treasure Ring",    []),
    (16, "Safety Ring",      [(0, 1, 0.2)]),
    (16, "Hard Ring",        [(3, 1, 0.2)]),

    (15, "Rental Shell",     []),
)

GEAR_DISALLOWED_LIST = (
    (15, 17, 18, 16),
    (15, 17, 18, 16),
    (12, 13,  3, 14, 11),
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

BADGE_PENALTIES = (
    20,  0,  0, 40,
    80, 20,  0,  0,
)
