from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial

from cheatoglobin.image import create_MObj_sprite, create_FObj_sprite, create_BObjUI_sprite
from cheatoglobin.constants import *

class PlayerAbilitiesTab(QtWidgets.QWidget):
    def __init__(self, parent, has_rom):
        super().__init__()

        self.badge_data = None
        self.var_2xxx_data = None
        self.parent = parent
        self.has_rom = has_rom

        main_layout = QtWidgets.QVBoxLayout(self)

        self.labels_that_need_badge_sprites = []
        self.labels_that_need_ability_sprites = []

        # ======================================================================================================================

        # badges enabled

        badges_enabled = QtWidgets.QWidget()
        badges_enabled_layout = QtWidgets.QHBoxLayout(badges_enabled)

        padding = QtWidgets.QWidget()
        badges_enabled_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        if self.has_rom:
            self.badges_enabled_icon = QtWidgets.QLabel()
            badges_enabled_layout.addWidget(self.badges_enabled_icon)

        badges_enabled_label = QtWidgets.QLabel("Player Can Use Badges:")
        badges_enabled_layout.addWidget(badges_enabled_label, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        self.badges_enabled_box = QtWidgets.QCheckBox()
        self.badges_enabled_box.checkStateChanged.connect(partial(self.change_data, 3, 8))
        badges_enabled_layout.addWidget(self.badges_enabled_box, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        padding = QtWidgets.QWidget()
        badges_enabled_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        main_layout.addWidget(badges_enabled)

        # --------------------------------------------------------

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        # player badges

        self.player_badges = QtWidgets.QWidget()
        player_badges_layout = QtWidgets.QHBoxLayout(self.player_badges)
        player_badges_layout.setContentsMargins(0, 0, 0, 0)

        mario_badges = QtWidgets.QFrame()
        mario_badges.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        mario_badges.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        mario_badges_layout = QtWidgets.QGridLayout(mario_badges)
        mario_badges.setStyleSheet("QFrame { background-color: " + '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[1]) + " ; }"
                                   "QFrame:disabled { background-color: " + '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[2]) + " ; }")

        luigi_badges = QtWidgets.QFrame()
        luigi_badges.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        luigi_badges.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        luigi_badges_layout = QtWidgets.QGridLayout(luigi_badges)
        luigi_badges.setStyleSheet("QFrame { background-color: " + '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[4]) + " ; }"
                                   "QFrame:disabled { background-color: " + '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[5]) + " ; }")

        luigi_badge_text = QtWidgets.QLabel("Current badge:")
        luigi_badge_text.setStyleSheet("color: #000000;")
        luigi_badges_layout.addWidget(luigi_badge_text, 0, 0, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        mario_badge_text = QtWidgets.QLabel("Current badge:")
        mario_badge_text.setStyleSheet("color: #000000;")
        mario_badges_layout.addWidget(mario_badge_text, 0, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        self.luigi_badge_selection = QtWidgets.QComboBox()
        self.luigi_badge_selection.addItems(BADGE_NAMES[4:])
        self.luigi_badge_selection.currentIndexChanged.connect(partial(self.change_data, 0, 1))
        luigi_badges_layout.addWidget(self.luigi_badge_selection, 0, 1, 1, 2)

        self.mario_badge_selection = QtWidgets.QComboBox()
        self.mario_badge_selection.addItems(BADGE_NAMES[:4])
        self.mario_badge_selection.currentIndexChanged.connect(partial(self.change_data, 0, 0))
        mario_badges_layout.addWidget(self.mario_badge_selection, 0, 2, 1, 2)

        luigi_badge_meter_text = QtWidgets.QLabel("Badge Meter:")
        luigi_badge_meter_text.setStyleSheet("color: #000000;")
        luigi_badges_layout.addWidget(luigi_badge_meter_text, 1, 0, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        mario_badge_meter_text = QtWidgets.QLabel("Badge Meter:")
        mario_badge_meter_text.setStyleSheet("color: #000000;")
        mario_badges_layout.addWidget(mario_badge_meter_text, 1, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.luigi_badge_meter = QtWidgets.QSpinBox()
        self.luigi_badge_meter.textChanged.connect(partial(self.change_data, 2, 1))
        self.luigi_badge_meter.setMinimum(0)
        luigi_badges_layout.addWidget(self.luigi_badge_meter, 1, 1)
        
        self.mario_badge_meter = QtWidgets.QSpinBox()
        self.mario_badge_meter.textChanged.connect(partial(self.change_data, 2, 0))
        self.mario_badge_meter.setMinimum(0)
        mario_badges_layout.addWidget(self.mario_badge_meter, 1, 2)

        self.luigi_badge_meter_total_text = QtWidgets.QLabel("/ 100")
        self.luigi_badge_meter_total_text.setStyleSheet("color: #000000;")
        luigi_badges_layout.addWidget(self.luigi_badge_meter_total_text, 1, 2, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        self.mario_badge_meter_total_text = QtWidgets.QLabel("/ 100")
        self.mario_badge_meter_total_text.setStyleSheet("color: #000000;")
        mario_badges_layout.addWidget(self.mario_badge_meter_total_text, 1, 3, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        if self.parent.parent.has_rom:
            self.badge_icon = QtWidgets.QLabel()

        player_badges_layout.addWidget(luigi_badges)
        if self.parent.parent.has_rom:
            self.badge_icon = QtWidgets.QLabel()
            player_badges_layout.addWidget(self.badge_icon)
        player_badges_layout.addWidget(mario_badges)

        main_layout.addWidget(self.player_badges)

        # --------------------------------------------------------

        # badge meter

        self.badge_meter_bar = QtWidgets.QProgressBar()
        self.badge_meter_bar.setMaximum(1)
        self.badge_meter_bar.setValue(1)
        self.badge_meter_bar.setTextVisible(False)

        main_layout.addWidget(QtWidgets.QLabel("Badge Meter:"))
        main_layout.addWidget(self.badge_meter_bar)

        # --------------------------------------------------------

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        # badge inventory

        self.badge_inventory = QtWidgets.QWidget()
        badge_inventory_layout = QtWidgets.QGridLayout(self.badge_inventory)
        badge_inventory_layout.setContentsMargins(0, 0, 0, 0)

        self.all_badge_widget_sets = []

        for i in range(len(BADGE_NAMES)):
            current_badge = QtWidgets.QFrame()
            current_badge_layout = QtWidgets.QHBoxLayout(current_badge)
            current_badge.setAutoFillBackground(True)

            if self.has_rom:
                current_badge_icon = QtWidgets.QLabel()
                self.labels_that_need_badge_sprites.append((current_badge_icon, i))
                current_badge_layout.addWidget(current_badge_icon)
            else:
                current_badge_icon = QtWidgets.QLabel("")

            current_badge_name = QtWidgets.QLabel(BADGE_NAMES[i])
            current_badge_layout.addWidget(current_badge_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            line.setAutoFillBackground(True)
            current_badge_layout.addWidget(line)
            
            current_badge_box = QtWidgets.QCheckBox()
            current_badge_box.checkStateChanged.connect(partial(self.change_data, 1, i))
            current_badge_layout.addWidget(current_badge_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            badge_inventory_layout.addWidget(current_badge, i // 4, i % 4)
            self.all_badge_widget_sets.append((current_badge_icon, current_badge_name, current_badge_box, current_badge, line))
        
        main_layout.addWidget(QtWidgets.QLabel("Owned Badges:"))
        main_layout.addWidget(self.badge_inventory)

        # --------------------------------------------------------

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        # field abilities

        field_abilities = QtWidgets.QWidget()
        field_abilities_layout = QtWidgets.QGridLayout(field_abilities)
        field_abilities_layout.setContentsMargins(0, 0, 0, 0)

        self.all_ability_widget_sets = []

        for i in range(8):
            current_ability = QtWidgets.QFrame()
            current_ability_layout = QtWidgets.QHBoxLayout(current_ability)
            current_ability_layout.setContentsMargins(11, 0, 11, 0)

            if self.has_rom:
                current_ability_icon = QtWidgets.QLabel()
                self.labels_that_need_ability_sprites.append((current_ability_icon, i))
                current_ability_layout.addWidget(current_ability_icon)
            else:
                current_ability_icon = QtWidgets.QLabel("")

            current_ability_name = QtWidgets.QLabel(ABILITY_NAMES[i])
            current_ability_layout.addWidget(current_ability_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            current_ability_layout.addWidget(line)
            
            current_ability_box = QtWidgets.QCheckBox()
            current_ability_box.checkStateChanged.connect(partial(self.change_data, 3, i))
            current_ability_layout.addWidget(current_ability_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            organization = [1, 0, 2, 3, 5, 4, 7, 6]
            field_abilities_layout.addWidget(current_ability, organization[i] // 4, organization[i] % 4)
            self.all_ability_widget_sets.append((current_ability_icon, current_ability_name, current_ability_box, current_ability, line))
        
        main_layout.addWidget(QtWidgets.QLabel("Field Abilities:"))
        main_layout.addWidget(field_abilities)

        # --------------------------------------------------------

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        # battle abilities

        battle_abilities = QtWidgets.QWidget()
        battle_abilities_layout = QtWidgets.QGridLayout(battle_abilities)
        battle_abilities_layout.setContentsMargins(0, 0, 0, 0)

        for i in range(2):
            current_ability = QtWidgets.QFrame()
            current_ability_layout = QtWidgets.QHBoxLayout(current_ability)
            current_ability_layout.setContentsMargins(11, 0, 11, 0)

            if self.has_rom:
                current_ability_icon = QtWidgets.QLabel()
                self.labels_that_need_ability_sprites.append((current_ability_icon, i + 9))
                current_ability_layout.addWidget(current_ability_icon)
            else:
                current_ability_icon = QtWidgets.QLabel("")

            current_ability_name = QtWidgets.QLabel(ABILITY_NAMES[i + 8])
            current_ability_layout.addWidget(current_ability_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            current_ability_layout.addWidget(line)
            
            current_ability_box = QtWidgets.QCheckBox()
            current_ability_box.checkStateChanged.connect(partial(self.change_data, 3, i + 9))
            current_ability_layout.addWidget(current_ability_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            battle_abilities_layout.addWidget(current_ability, 0, i)
            self.all_ability_widget_sets.append((current_ability_icon, current_ability_name, current_ability_box, current_ability, line))

        for i in range(2):
            padding = QtWidgets.QWidget()
            main_layout.addWidget(padding)
            padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            battle_abilities_layout.addWidget(padding, 0, i + 2)

        main_layout.addWidget(QtWidgets.QLabel("Battle Abilities:"))
        main_layout.addWidget(battle_abilities)

        # --------------------------------------------------------

        padding = QtWidgets.QWidget()
        main_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.assign_sprites()
    
    def assign_badge_sprites(self, badges):
        tex = create_MObj_sprite(
            self.parent.parent.overlay_MObj_offsets,
            self.parent.parent.overlay_MObj,
            self.parent.parent.MObj_file,
            [32, 259][self.parent.parent.rom_base],
            badges,
            self.parent.parent.lang)
        tex = tex.scaled(tex.width() * 2, tex.height() * 2, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        return tex
    
    def assign_sprites(self):
        if not self.has_rom:
            return
        
        self.badges_enabled_icon.setPixmap(create_MObj_sprite(
                self.parent.parent.overlay_MObj_offsets,
                self.parent.parent.overlay_MObj,
                self.parent.parent.MObj_file,
                31,
                [0, 4],
                self.parent.parent.lang))

        for i in range(4):
            self.mario_badge_selection.setItemIcon(i, create_MObj_sprite(
                self.parent.parent.overlay_MObj_offsets,
                self.parent.parent.overlay_MObj,
                self.parent.parent.MObj_file,
                31,
                i,
                self.parent.parent.lang))

            self.luigi_badge_selection.setItemIcon(i, create_MObj_sprite(
                self.parent.parent.overlay_MObj_offsets,
                self.parent.parent.overlay_MObj,
                self.parent.parent.MObj_file,
                31,
                i + 4,
                self.parent.parent.lang))

        for badge in self.labels_that_need_badge_sprites:
            tex = create_MObj_sprite(
                self.parent.parent.overlay_MObj_offsets,
                self.parent.parent.overlay_MObj,
                self.parent.parent.MObj_file,
                31,
                badge[1],
                self.parent.parent.lang)
            badge[0].setPixmap(tex)
            badge[0].setFixedWidth(tex.width())

        index = 0
        ability_sprites = [[0x2E, 1, 6], [0x2E, 0, 5], [0x2E, 0, 7], [0x2E, 1, 8], [0x1E0, 1, 4], [0x1E0, 0, 3], [0x1E0, 1, 5], [0x1E0, 0, 6]]
        for ability in self.labels_that_need_ability_sprites:
            if index < 8:
                tex = create_FObj_sprite(
                    self.parent.parent.overlay_FObj_offsets,
                    self.parent.parent.overlay_FObj,
                    self.parent.parent.FObj_file,
                    ability_sprites[index][0],
                    [ability_sprites[index][1], ability_sprites[index][2]],
                    self.parent.parent.lang)
                ability[0].setPixmap(tex)
                ability[0].setFixedWidth(tex.width())
            else:
                tex = create_BObjUI_sprite(
                    self.parent.parent.overlay_BObjUI_offsets,
                    self.parent.parent.overlay_BObjUI_filedata,
                    self.parent.parent.overlay_BObjUI_groupdata,
                    self.parent.parent.BObjUI_file,
                    [12, 11][index - 8],
                    [13, 46][index - 8],
                    self.parent.parent.lang)
                ability[0].setPixmap(tex)
                ability[0].setFixedWidth(tex.width())
            index += 1
    
    def change_data(self, data_type, stat, value):
        self.parent.set_edited(True)

        if data_type == 1:
            checked = value == QtCore.Qt.Checked
            if checked:
                self.badge_data[1][0] |= (1 << stat)
            else:
                self.badge_data[1][0] &= ~(1 << stat)
        elif data_type == 3:
            checked = value == QtCore.Qt.Checked

            if stat == 4: # bowser fire
                checked = not checked

            stat_to_mod = 0
            if stat == 8: # badges enabled
                stat_to_mod = 1
                stat = 4
            elif stat == 9: # vacuum
                stat_to_mod = 1
                stat = 6
            if stat == 10: # shell counter
                stat_to_mod = 2
                stat = 4

            if checked:
                self.var_2xxx_data[stat_to_mod] |= (1 << stat)
            else:
                self.var_2xxx_data[stat_to_mod] &= ~(1 << stat)
        else:
            if data_type == 0:
                self.badge_data[2][0] = 0
                self.badge_data[2][1] = 0
                if stat == 1:
                    value += 4
                self.badge_data[1][0] |= (1 << value)
            self.badge_data[data_type][stat] = int(str(value), 0)

        self.set_data()
    
    def set_data(self):
        self.badges_enabled_box.blockSignals(True)
        self.badges_enabled_box.setChecked(self.var_2xxx_data[1] & 0b00010000 != 0)
        self.badges_enabled_box.blockSignals(False)

        self.player_badges.setEnabled(self.var_2xxx_data[1] & 0b00010000 != 0)
        self.badge_meter_bar.setEnabled(self.var_2xxx_data[1] & 0b00010000 != 0)
        self.badge_inventory.setEnabled(self.var_2xxx_data[1] & 0b00010000 != 0)

        self.mario_badge_selection.blockSignals(True)
        self.mario_badge_selection.setCurrentIndex(self.badge_data[0][0])
        self.mario_badge_selection.blockSignals(False)

        self.luigi_badge_selection.blockSignals(True)
        self.luigi_badge_selection.setCurrentIndex(self.badge_data[0][1] - 4)
        self.luigi_badge_selection.blockSignals(False)

        if self.parent.parent.has_rom:
            self.badge_icon.setPixmap(self.assign_badge_sprites([self.badge_data[0][0] + 12, self.badge_data[0][1] + 12]))

        badge_meter_full = 140 + BADGE_PENALTIES[self.badge_data[0][0]] + BADGE_PENALTIES[self.badge_data[0][1]]

        self.mario_badge_meter.blockSignals(True)
        self.luigi_badge_meter.blockSignals(True)

        self.mario_badge_meter_total_text.setText(f"/ {badge_meter_full}")
        self.luigi_badge_meter_total_text.setText(f"/ {badge_meter_full}")

        self.luigi_badge_meter.setMaximum(badge_meter_full - self.badge_data[2][0])
        self.mario_badge_meter.setMaximum(badge_meter_full - self.badge_data[2][1])
        
        self.mario_badge_meter.setValue(self.badge_data[2][0])
        self.luigi_badge_meter.setValue(self.badge_data[2][1])

        self.mario_badge_meter.blockSignals(False)
        self.luigi_badge_meter.blockSignals(False)

        badge_meter_is_enabled = 1 - int(self.badge_meter_bar.isEnabled())
        m_color = '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[1 + badge_meter_is_enabled])
        m_color_1 = '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[0 + (badge_meter_is_enabled * 2)])
        l_color = '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[4 + badge_meter_is_enabled])
        l_color_1 = '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[3 + (badge_meter_is_enabled * 2)])
        mid_color = "transparent"

        if self.badge_data[2][0] + self.badge_data[2][1] == badge_meter_full:
            middle_section = ""
        else:
            middle_section = f"stop: {(self.badge_data[2][1] / badge_meter_full)} {mid_color}, stop: {1 - (self.badge_data[2][0] / badge_meter_full)} {mid_color}, "
        
        if self.badge_data[2][0] != 0:
            mario_section = f"stop: {min(1, 1 - (self.badge_data[2][0] / badge_meter_full) + 0.00001)} {m_color_1}, stop: 1 {m_color}"
        else:
            mario_section = f"stop: 1 {mid_color}"
        
        if self.badge_data[2][1] != 0:
            luigi_section = f"stop: 0 {l_color}, stop: {max(0, (self.badge_data[2][1] / badge_meter_full) - 0.00001)} {l_color_1}, "
        else:
            luigi_section = f"stop: 0 {mid_color}, "

        self.badge_meter_bar.setStyleSheet("::chunk {"
                   "background-color: "
                   "qlineargradient(x0: 0, x2: 1, "
                   f"{luigi_section}"
                   f"{middle_section}"
                   f"{mario_section}"
                   ")}")

        for i in range(len(self.all_badge_widget_sets)):
            badge_widgets = self.all_badge_widget_sets[i]

            badge_widgets[2].blockSignals(True)

            badge_widgets[0].setEnabled(self.badge_data[1][0] & (1 << i) != 0)
            badge_widgets[1].setEnabled(self.badge_data[1][0] & (1 << i) != 0)
            badge_widgets[2].setChecked(self.badge_data[1][0] & (1 << i) != 0)

            if self.badge_data[0][0] == i or self.badge_data[0][1] == i:
                badge_widgets[2].setEnabled(False)

                badge_widgets[3].setStyleSheet("QFrame { background-color: " + '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[((i // 4) * 3) + 1]) + " ; }"
                                               "QFrame:disabled { background-color: " + '#{:02X}{:02X}{:02X}'.format(*PLAYER_COLORS[((i // 4) * 3) + 2]) + " ; }")

                line_color = QtGui.QPalette()
                line_color.setColor(QtGui.QPalette.Light, QtGui.QColor(*PLAYER_COLORS[((i // 4) * 3) + 0]))
                line_color.setColor(QtGui.QPalette.Dark, QtGui.QColor(*PLAYER_COLORS[((i // 4) * 3) + 2]))
                badge_widgets[4].setPalette(line_color)
            else:
                badge_widgets[2].setEnabled(True)

                if self.badge_data[1][0] & (1 << i) != 0:
                    badge_widgets[3].setStyleSheet("QFrame { background-color: #00000000 ; }"
                                                   "QFrame:disabled { background-color: #00000000 ; }")
                else:
                    badge_widgets[3].setStyleSheet("")

                line_color = QtGui.QPalette()
                badge_widgets[4].setPalette(line_color)

            badge_widgets[2].blockSignals(False)
        
        for i in range(len(self.all_ability_widget_sets)):
            ability_widgets = self.all_ability_widget_sets[i]

            if i < 8:
                stat_enabled = self.var_2xxx_data[0] & (1 << i) != 0
                if i == 4:
                    stat_enabled = not stat_enabled
                    print(i)
            elif i == 8:
                stat_enabled = self.var_2xxx_data[1] & (1 << 6) != 0
                print("wqow")
            elif i == 9:
                stat_enabled = self.var_2xxx_data[2] & (1 << 4) != 0
                print("whar")

            ability_widgets[2].blockSignals(True)

            ability_widgets[0].setEnabled(stat_enabled)
            ability_widgets[1].setEnabled(stat_enabled)
            ability_widgets[2].setChecked(stat_enabled)

            ability_widgets[2].blockSignals(False)