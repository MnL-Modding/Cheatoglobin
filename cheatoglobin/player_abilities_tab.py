from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial

from cheatoglobin.image import create_MObj_sprite
from cheatoglobin.constants import *

class PlayerAbilitiesTab(QtWidgets.QWidget):
    def __init__(self, parent, has_rom):
        super().__init__()

        self.badge_data = None
        self.parent = parent
        self.has_rom = has_rom

        main_layout = QtWidgets.QVBoxLayout(self)

        # ======================================================================================================================

        # player badges

        player_badges = QtWidgets.QWidget()
        player_badges_layout = QtWidgets.QHBoxLayout(player_badges)
        player_badges_layout.setContentsMargins(0, 0, 0, 0)

        mario_badges = QtWidgets.QFrame()
        mario_badges.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        mario_badges.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        mario_badges_layout = QtWidgets.QGridLayout(mario_badges)
        mario_color = mario_badges.palette()
        mario_color.setColor(QtGui.QPalette.Window, QtGui.QColor(*PLAYER_COLORS[1]))
        mario_badges.setPalette(mario_color)
        mario_badges.setAutoFillBackground(True)

        luigi_badges = QtWidgets.QFrame()
        luigi_badges.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        luigi_badges.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        luigi_badges_layout = QtWidgets.QGridLayout(luigi_badges)
        luigi_color = luigi_badges.palette()
        luigi_color.setColor(QtGui.QPalette.Window, QtGui.QColor(*PLAYER_COLORS[4]))
        luigi_badges.setPalette(luigi_color)
        luigi_badges.setAutoFillBackground(True)

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

        luigi_badges_layout.addWidget(QtWidgets.QLabel("Badge Meter:"), 1, 0, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        mario_badges_layout.addWidget(QtWidgets.QLabel("Badge Meter:"), 1, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.luigi_badge_meter = QtWidgets.QSpinBox()
        self.luigi_badge_meter.setMaximum(999)
        #self.luigi_badge_meter.textChanged.connect(partial(self.change_data, current_player, stat))
        luigi_badges_layout.addWidget(self.luigi_badge_meter, 1, 1)
        
        self.mario_badge_meter = QtWidgets.QSpinBox()
        self.mario_badge_meter.setMaximum(999)
        #self.mario_badge_meter.textChanged.connect(partial(self.change_data, current_player, stat))
        mario_badges_layout.addWidget(self.mario_badge_meter, 1, 2)

        luigi_badges_layout.addWidget(QtWidgets.QLabel("/ 100"), 1, 2, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        mario_badges_layout.addWidget(QtWidgets.QLabel("/ 100"), 1, 3, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        self.luigi_badge_icon = QtWidgets.QLabel()
        luigi_badges_layout.addWidget(self.luigi_badge_icon, 0, 3, 2, 1, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

        self.mario_badge_icon = QtWidgets.QLabel()
        mario_badges_layout.addWidget(self.mario_badge_icon, 0, 0, 2, 1, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        player_badges_layout.addWidget(luigi_badges)
        player_badges_layout.addWidget(mario_badges)

        main_layout.addWidget(player_badges)

        # --------------------------------------------------------

        # player abilities

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        padding = QtWidgets.QWidget()
        main_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # --------------------------------------------------------

        self.assign_sprites()
    
    def assign_badge_sprites(self, badge):
        tex = create_MObj_sprite(
            self.parent.parent.overlay_MObj_offsets,
            self.parent.parent.overlay_MObj,
            self.parent.parent.MObj_file,
            259,
            badge + 12,
            self.parent.parent.lang)
        tex = tex.scaled(tex.width() * 2, tex.height() * 2, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        return tex
    
    def assign_sprites(self):
        if not self.has_rom:
            return

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
    
    def change_data(self, data_type, stat, value):
        self.parent.set_edited(True)

        if data_type == 0 and stat == 1:
            value += 4

        self.badge_data[data_type][stat] = int(str(value), 0)

        self.set_data()
    
    def set_data(self):
        self.mario_badge_icon.setPixmap(self.assign_badge_sprites(self.badge_data[0][0]))
        self.mario_badge_selection.setCurrentIndex(self.badge_data[0][0])
        self.luigi_badge_icon.setPixmap(self.assign_badge_sprites(self.badge_data[0][1]))
        self.luigi_badge_selection.setCurrentIndex(self.badge_data[0][1] - 4)