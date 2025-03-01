from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial

from cheatoglobin.constants import *

class PlayerStatsTab(QtWidgets.QWidget):
    def __init__(self, parent, has_rom):
        super().__init__()

        self.stats_data = None
        self.parent = parent
        self.has_rom = has_rom

        # ======================================================================================================================

        # player stats

        main_layout = QtWidgets.QHBoxLayout(self)

        self.base_stat_boxes = ([], [], [])
        self.base_stat_additives = ([], [], [])

        self.current_points_stat_boxes = ([], [], [])
        self.current_points_stat_totals = ([], [], [])

        self.current_level_stats = ([], [], [])
        self.current_rank_icons = []
        self.next_level_exp = []
        
        self.equipped_gear_boxes = ([], [], [])

        for current_player in range(3):
            player_stats = QtWidgets.QFrame()
            player_stats.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            player_stats.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            player_stats_layout = QtWidgets.QVBoxLayout(player_stats)

            player_color = player_stats.palette()
            player_color.setColor(QtGui.QPalette.Window, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 1]))
            player_stats.setPalette(player_color)
            player_stats.setAutoFillBackground(True)

            if self.has_rom:
                player_name_tex = QtGui.QPixmap(str(FILES_DIR / f"NAME_{PLAYER_NAMES[current_player]}.png"))
                player_name_tex = player_name_tex.scaled(player_name_tex.width() * 2, player_name_tex.height() * 2, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                player_name = QtWidgets.QLabel()
                player_name.setPixmap(player_name_tex)
            else:
                player_name = QtWidgets.QLabel(PLAYER_NAMES[current_player])
                player_name.setStyleSheet("color: #000000;") 
                font = QtGui.QFont()
                font.setPointSize(player_name.font().pointSize() * 2)
                player_name.setFont(font)
            player_stats_layout.addWidget(player_name, alignment = QtCore.Qt.AlignmentFlag.AlignCenter)

            # --------------------------------------------------------
            
            # Base Stats

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_color = line.palette()
            line_color.setColor(QtGui.QPalette.Light, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 0]))
            line_color.setColor(QtGui.QPalette.Dark, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 2]))
            line.setPalette(line_color)
            line.setAutoFillBackground(True)
            player_stats_layout.addWidget(line)

            for stat in range(len(STAT_NAMES[0])):
                base_stat = QtWidgets.QWidget()
                base_stat_layout = QtWidgets.QHBoxLayout(base_stat)
                base_stat_layout.setContentsMargins(0, 0, 0, 0)

                base_stat_text = QtWidgets.QLabel("Base")
                base_stat_text.setStyleSheet("color: #000000;") 
                base_stat_layout.addWidget(base_stat_text)

                if self.has_rom:
                    if (stat != 1 and stat != 5) or current_player != 2:
                        base_stat_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[0][stat]}.png"))
                    else:
                        base_stat_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[0][stat]}_1.png"))
                    base_stat_icon = QtWidgets.QLabel()
                    base_stat_icon.setPixmap(base_stat_icon_tex)
                else:
                    if stat != 5 or current_player != 2:
                        base_stat_icon = QtWidgets.QLabel(STAT_NAMES_LANG[0][stat][current_player])
                    else:
                        base_stat_icon = QtWidgets.QLabel(STAT_NAMES_LANG[0][stat][current_player])
                    base_stat_icon.setStyleSheet("color: #000000;") 
                base_stat_layout.addWidget(base_stat_icon)

                padding = QtWidgets.QWidget()
                base_stat_layout.addWidget(padding)
                padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

                base_stat_box = QtWidgets.QSpinBox()
                base_stat_box.setMaximum(999)
                base_stat_box.textChanged.connect(partial(self.change_data, current_player, stat))
                base_stat_layout.addWidget(base_stat_box)

                base_stat_plus = QtWidgets.QLabel("+")
                base_stat_plus.setStyleSheet("color: #000000;") 
                base_stat_layout.addWidget(base_stat_plus)

                base_stat_additive = QtWidgets.QLabel(str(0))
                base_stat_additive.setStyleSheet("color: #000000;")
                base_stat_layout.addWidget(base_stat_additive)

                player_stats_layout.addWidget(base_stat)
                self.base_stat_boxes[current_player].append(base_stat_box)
                self.base_stat_additives[current_player].append(base_stat_additive)

            # --------------------------------------------------------
            
            # Current HP/SP

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_color = line.palette()
            line_color.setColor(QtGui.QPalette.Light, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 0]))
            line_color.setColor(QtGui.QPalette.Dark, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 2]))
            line.setPalette(line_color)
            line.setAutoFillBackground(True)
            player_stats_layout.addWidget(line)

            for stat in range(len(STAT_NAMES[1])):
                current_stat = QtWidgets.QWidget()
                current_stat_layout = QtWidgets.QHBoxLayout(current_stat)
                current_stat_layout.setContentsMargins(0, 0, 0, 0)

                current_stat_text = QtWidgets.QLabel("Current")
                current_stat_text.setStyleSheet("color: #000000;")
                current_stat_layout.addWidget(current_stat_text)

                if self.has_rom:
                    if stat != 1 or current_player != 2:
                        current_stat_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[1][stat]}.png"))
                    else:
                        current_stat_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[1][stat]}_1.png"))
                    current_stat_icon = QtWidgets.QLabel()
                    current_stat_icon.setPixmap(current_stat_icon_tex)
                else:
                    current_stat_icon = QtWidgets.QLabel(STAT_NAMES_LANG[1][stat][current_player])
                    current_stat_icon.setStyleSheet("color: #000000;") 
                current_stat_layout.addWidget(current_stat_icon)

                padding = QtWidgets.QWidget()
                current_stat_layout.addWidget(padding)
                padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

                current_stat_box = QtWidgets.QSpinBox()
                current_stat_box.setMaximum(999)
                current_stat_box.textChanged.connect(partial(self.change_data, current_player, stat + 6))
                current_stat_layout.addWidget(current_stat_box)

                current_stat_slash = QtWidgets.QLabel("/")
                current_stat_slash.setStyleSheet("color: #000000;")
                current_stat_layout.addWidget(current_stat_slash)

                current_stat_total = QtWidgets.QLabel(str(0))
                current_stat_total.setStyleSheet("color: #000000;")
                current_stat_layout.addWidget(current_stat_total)

                player_stats_layout.addWidget(current_stat)
                self.current_points_stat_boxes[current_player].append(current_stat_box)
                self.current_points_stat_totals[current_player].append(current_stat_total)

            # --------------------------------------------------------
            
            # Total EXP/LV

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_color = line.palette()
            line_color.setColor(QtGui.QPalette.Light, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 0]))
            line_color.setColor(QtGui.QPalette.Dark, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 2]))
            line.setPalette(line_color)
            line.setAutoFillBackground(True)
            player_stats_layout.addWidget(line)

            level_info = QtWidgets.QWidget()
            level_info_layout = QtWidgets.QGridLayout(level_info)
            level_info_layout.setContentsMargins(0, 0, 0, 0)

            # LV

            if self.has_rom:
                current_level_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[2][0]}.png"))
                current_level_icon = QtWidgets.QLabel()
                current_level_icon.setPixmap(current_level_icon_tex)
            else:
                current_level_icon = QtWidgets.QLabel(STAT_NAMES_LANG[2][0])
                current_level_icon.setStyleSheet("color: #000000;") 
            level_info_layout.addWidget(current_level_icon, 0, 0)

            current_level_box = QtWidgets.QSpinBox()
            current_level_box.setMinimum(1)
            current_level_box.setMaximum(99)
            current_level_box.textChanged.connect(partial(self.change_data, current_player, 8))
            current_level_box.blockSignals(True)
            level_info_layout.addWidget(current_level_box, 0, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
            self.current_level_stats[current_player].append(current_level_box)

            # EXP

            if self.has_rom:
                current_exp_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[2][1]}.png"))
                current_exp_icon = QtWidgets.QLabel()
                current_exp_icon.setPixmap(current_exp_icon_tex)
            else:
                current_exp_icon = QtWidgets.QLabel(STAT_NAMES_LANG[2][1])
                current_exp_icon.setStyleSheet("color: #000000;") 
            level_info_layout.addWidget(current_exp_icon, 1, 0)

            current_exp_box = QtWidgets.QSpinBox()
            current_exp_box.setMaximum(9999999)
            current_exp_box.textChanged.connect(partial(self.change_data, current_player, 9))
            current_exp_box.blockSignals(True)
            level_info_layout.addWidget(current_exp_box, 1, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
            self.current_level_stats[current_player].append(current_exp_box)

            # NEXT

            if self.has_rom:
                next_exp_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"STAT_{STAT_NAMES[2][2]}.png"))
                next_exp_icon = QtWidgets.QLabel()
                next_exp_icon.setPixmap(next_exp_icon_tex)
            else:
                next_exp_icon = QtWidgets.QLabel(STAT_NAMES_LANG[2][2])
                next_exp_icon.setStyleSheet("color: #000000;") 
            level_info_layout.addWidget(next_exp_icon, 2, 0)

            next_exp_text = QtWidgets.QLabel("0")
            next_exp_text.setStyleSheet("color: #000000;")
            level_info_layout.addWidget(next_exp_text, 2, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
            self.next_level_exp.append(next_exp_text)

            # RANK
            # TO DO: make this dependent on whether a ROM was provided or not

            if current_player != 2:
                player = "ML"
            else:
                player = "KP"

            rank = 0
            current_rank_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"RANK_{player}_{rank}.png"))
            current_rank_icon_tex = current_rank_icon_tex.scaled(current_rank_icon_tex.width() * 2, current_rank_icon_tex.height() * 2, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            current_rank_icon = QtWidgets.QLabel()
            current_rank_icon.setPixmap(current_rank_icon_tex)
            self.current_rank_icons.append(current_rank_icon)
            level_info_layout.addWidget(current_rank_icon, 0, 2, 3, 1, alignment = QtCore.Qt.AlignmentFlag.AlignCenter)

            player_stats_layout.addWidget(level_info)

            # --------------------------------------------------------
            
            # Gear Slots

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_color = line.palette()
            line_color.setColor(QtGui.QPalette.Light, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 0]))
            line_color.setColor(QtGui.QPalette.Dark, QtGui.QColor(*PLAYER_COLORS[(current_player * 3) + 2]))
            line.setPalette(line_color)
            line.setAutoFillBackground(True)
            player_stats_layout.addWidget(line)

            gear_label = QtWidgets.QLabel("Equipped Gear:")
            gear_label.setStyleSheet("color: #000000;")
            player_stats_layout.addWidget(gear_label)

            for stat in range(len(STAT_NAMES[3])):
                current_gear_box = QtWidgets.QComboBox()

                for gear in GEAR_DATA:
                    if self.has_rom:
                        current_gear_box.addItem(QtGui.QIcon(str(FILES_DIR / f"GEAR_{gear[0]}.png")), gear[1])
                    else:
                        current_gear_box.addItem(gear[1])
                current_gear_box.currentIndexChanged.connect(partial(self.change_data, current_player, stat + 10))
                
                player_stats_layout.addWidget(current_gear_box)
                self.equipped_gear_boxes[current_player].append(current_gear_box)


            # --------------------------------------------------------

            main_layout.addWidget(player_stats)
    
    def change_data(self, player, stat, value):
        self.parent.set_edited(True)

        self.stats_data[player][stat] = int(str(value), 0)

        if stat == 8:
            self.current_level_stats[player][1].blockSignals(True)
            if player != 2:
                self.stats_data[player][9] = ML_LEVEL_EXP[int(str(value), 0) - 1]
            else:
                self.stats_data[player][9] = KP_LEVEL_EXP[int(str(value), 0) - 1]

        if stat == 9:
            self.current_level_stats[player][0].blockSignals(True)
            if player != 2:
                lv = 0
                test = int(str(value), 0)
                for i in ML_LEVEL_EXP:
                    if test >= i:
                        lv += 1
                self.stats_data[player][8] = lv
            else:
                lv = 0
                test = int(str(value), 0)
                for i in KP_LEVEL_EXP:
                    if test >= i:
                        lv += 1
                self.stats_data[player][8] = lv   

        self.set_data()
    
    def set_data(self):
        for current_player in range(3):
            gear_add = [0, 0, 0, 0, 0, 0]

            for gear in range(3):
                current_gear = GEAR_DATA[self.stats_data[current_player][gear + 10]]
                for stat_boost in current_gear[2]:
                    match stat_boost[1]:
                        case 0:
                            gear_add[stat_boost[0]] += stat_boost[2]
                        case 1:
                            stat_to_mult = self.stats_data[current_player][stat_boost[0]] + gear_add[stat_boost[0]]
                            mult_add = round(stat_to_mult * stat_boost[2])
                            gear_add[stat_boost[0]] += mult_add

            current_stat = 0
            for i in range(len(self.base_stat_boxes[current_player])):
                box = self.base_stat_boxes[current_player][i]
                add = self.base_stat_additives[current_player][i]

                box.blockSignals(True)

                box.setValue(self.stats_data[current_player][current_stat])
                add.setText(str(gear_add[i]))

                box.blockSignals(False)

                current_stat += 1

            for i in range(len(self.current_points_stat_boxes[current_player])):
                box = self.current_points_stat_boxes[current_player][i]
                total = self.current_points_stat_totals[current_player][i]

                box.blockSignals(True)

                box.setValue(self.stats_data[current_player][current_stat])
                box.setMaximum(self.stats_data[current_player][i] + gear_add[i])
                total.setText(str(self.stats_data[current_player][i] + gear_add[i]))

                box.blockSignals(False)

                current_stat += 1
            
            for i in range(len(self.current_level_stats[current_player])):
                box = self.current_level_stats[current_player][i]

                box.blockSignals(True)

                box.setValue(self.stats_data[current_player][current_stat])

                box.blockSignals(False)

                current_stat += 1
            
            if self.stats_data[current_player][8] < 99:
                if current_player != 2:
                    self.next_level_exp[current_player].setText(str(ML_LEVEL_EXP[self.stats_data[current_player][8]] - self.stats_data[current_player][9]))
                else:
                    self.next_level_exp[current_player].setText(str(KP_LEVEL_EXP[self.stats_data[current_player][8]] - self.stats_data[current_player][9]))
            else:
                self.next_level_exp[current_player].setText("0")
            
            self.current_level_stats[current_player][0].blockSignals(False)
            self.current_level_stats[current_player][1].blockSignals(False)

            if current_player != 2:
                player = "ML"
            else:
                player = "KP"

            rank = 0
            for i in RANK_LEVELS[current_player]:
                if self.stats_data[current_player][8] >= i:
                    rank += 1
            current_rank_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"RANK_{player}_{rank}.png"))
            current_rank_icon_tex = current_rank_icon_tex.scaled(current_rank_icon_tex.width() * 2, current_rank_icon_tex.height() * 2, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.current_rank_icons[current_player].setPixmap(current_rank_icon_tex)

            for i in range(len(self.equipped_gear_boxes[current_player])):
                gear = self.equipped_gear_boxes[current_player][i]

                gear.blockSignals(True)

                gear.setCurrentIndex(self.stats_data[current_player][current_stat])

                if i > rank:
                    gear.setEnabled(False)
                else:
                    gear.setEnabled(True)

                gear_to_compare = []
                for j in range(3):
                    if i != j:
                        gear_to_compare.append(self.stats_data[current_player][j + 10])
                problem_list = []
                for j in range(len(GEAR_DATA)):
                    for k in gear_to_compare:
                        if (GEAR_DATA[j][0] == GEAR_DATA[k][0] and GEAR_DATA[j][0] != "NONE") or (GEAR_DATA[j][0] in GEAR_DISALLOWED_LIST[current_player]):
                            if j not in problem_list:
                                problem_list.append(j)
                if gear.currentIndex() in problem_list:
                    gear.setStyleSheet("color: #FF6666;")
                else:
                    gear.setStyleSheet("")
                for j in range(len(GEAR_DATA)):
                    if j in problem_list:
                        gear.setItemData(j, QtGui.QColor(255, 0, 0, 60), QtCore.Qt.BackgroundRole)
                    else:
                        gear.setItemData(j, QtGui.QColor(0, 0, 0, 0), QtCore.Qt.BackgroundRole)

                gear.blockSignals(False)

                current_stat += 1