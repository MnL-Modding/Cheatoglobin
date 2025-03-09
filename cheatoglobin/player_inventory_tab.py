from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial

from cheatoglobin.image import create_MObj_sprite
from cheatoglobin.constants import *

class PlayerInventoryTab(QtWidgets.QScrollArea):
    def __init__(self, parent, has_rom):
        super().__init__()

        self.inventory_data = None
        self.parent = parent
        self.has_rom = has_rom

        main = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(main)
        
        self.setWidget(main)
        self.setWidgetResizable(True)
        self.setBackgroundRole(QtGui.QPalette.Button)

        self.labels_that_need_item_sprites = []

        # ======================================================================================================================

        # coin count

        coin_count = QtWidgets.QWidget()
        coin_count_layout = QtWidgets.QHBoxLayout(coin_count)
        coin_count_layout.setContentsMargins(0, 0, 0, 0)

        padding = QtWidgets.QWidget()
        coin_count_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if self.has_rom:
            self.coin_count_icon = QtWidgets.QLabel()
            coin_count_layout.addWidget(self.coin_count_icon)

        coin_count_label = QtWidgets.QLabel("Total &Coins:")
        coin_count_layout.addWidget(coin_count_label, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        self.coin_count_box = QtWidgets.QSpinBox()
        self.coin_count_box.setMaximum(999999)
        self.coin_count_box.textChanged.connect(partial(self.change_data, 0, 0))
        coin_count_label.setBuddy(self.coin_count_box)
        coin_count_layout.addWidget(self.coin_count_box, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        padding = QtWidgets.QWidget()
        coin_count_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        main_layout.addWidget(coin_count)

        # --------------------------------------------------------

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        # item counts

        item_counts = QtWidgets.QWidget()
        item_counts_layout = QtWidgets.QGridLayout(item_counts)

        self.all_item_widget_sets = []

        for i in range(len(ITEM_DATA)):
            item = ITEM_DATA[i]

            current_item = QtWidgets.QWidget()
            current_item_layout = QtWidgets.QHBoxLayout(current_item)
            current_item_layout.setContentsMargins(0, 0, 0, 0)

            if self.has_rom:
                current_item_icon = QtWidgets.QLabel()
                self.labels_that_need_item_sprites.append((current_item_icon, item[0]))
                current_item_layout.addWidget(current_item_icon)
            else:
                current_item_icon = QtWidgets.QLabel("")

            current_item_name = QtWidgets.QLabel(item[1])
            current_item_layout.addWidget(current_item_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
            
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            current_item_layout.addWidget(line)
            
            current_item_box = QtWidgets.QSpinBox()
            current_item_box.setMaximum(99)
            current_item_box.textChanged.connect(partial(self.change_data, 1, i))
            current_item_layout.addWidget(current_item_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            item_counts_layout.addWidget(current_item, i // 4, i % 4)
            self.all_item_widget_sets.append((current_item_icon, current_item_name, current_item_box))
        
        main_layout.addWidget(QtWidgets.QLabel("Consumables Inventory:"))
        main_layout.addWidget(item_counts)

        # --------------------------------------------------------

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        main_layout.addWidget(line)

        # gear counts

        gear_counts = QtWidgets.QWidget()
        gear_counts_layout = QtWidgets.QGridLayout(gear_counts)

        self.all_gear_widget_sets = []

        for i in range(len(GEAR_DATA) - 2):
            gear = GEAR_DATA[i + 1]

            current_gear = QtWidgets.QWidget()
            current_gear_layout = QtWidgets.QHBoxLayout(current_gear)
            current_gear_layout.setContentsMargins(0, 0, 0, 0)

            if self.has_rom:
                current_gear_icon = QtWidgets.QLabel()
                self.labels_that_need_item_sprites.append((current_gear_icon, gear[0]))
                current_gear_layout.addWidget(current_gear_icon)
            else:
                current_gear_icon = QtWidgets.QLabel("")

            current_gear_name = QtWidgets.QLabel(gear[1])
            current_gear_layout.addWidget(current_gear_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            current_gear_layout.addWidget(line)
            
            current_gear_box = QtWidgets.QSpinBox()
            current_gear_box.setMaximum(9)
            current_gear_box.textChanged.connect(partial(self.change_data, 2, i))
            current_gear_layout.addWidget(current_gear_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            gear_counts_layout.addWidget(current_gear, i // 4, i % 4)
            self.all_gear_widget_sets.append((current_gear_icon, current_gear_name, current_gear_box))
        
        main_layout.addWidget(QtWidgets.QLabel("Gear Inventory:"))
        main_layout.addWidget(gear_counts)

        # --------------------------------------------------------

        self.assign_sprites()
    
    def assign_sprites(self):
        if not self.has_rom:
            return

        coin_count_tex = create_MObj_sprite(
            self.parent.parent.overlay_MObj_offsets,
            self.parent.parent.overlay_MObj,
            self.parent.parent.MObj_file,
            145,
            0,
            self.parent.parent.lang)
        self.coin_count_icon.setPixmap(coin_count_tex)
        self.coin_count_icon.setFixedWidth(coin_count_tex.width())

        item_sprite_cache = {}
        for item in self.labels_that_need_item_sprites:
            if item[1] not in item_sprite_cache:
                item_sprite_cache[item[1]] = create_MObj_sprite(
                self.parent.parent.overlay_MObj_offsets,
                self.parent.parent.overlay_MObj,
                self.parent.parent.MObj_file,
                9,
                item[1] * 2,
                self.parent.parent.lang)

            item[0].setPixmap(item_sprite_cache[item[1]])
            item[0].setFixedWidth(item_sprite_cache[item[1]].width())
    
    def change_data(self, data_type, stat, value):
        self.parent.set_edited(True)

        self.inventory_data[data_type][stat] = int(value, 0)
        self.set_data()
    
    def set_data(self):
        self.coin_count_box.blockSignals(True)
        self.coin_count_box.setValue(self.inventory_data[0][0])
        self.coin_count_box.blockSignals(False)

        for i in range(len(self.all_item_widget_sets)):
            item_widgets = self.all_item_widget_sets[i]

            item_widgets[2].blockSignals(True)

            item_widgets[0].setEnabled(self.inventory_data[1][i] != 0)
            item_widgets[1].setEnabled(self.inventory_data[1][i] != 0)
            item_widgets[2].setValue(self.inventory_data[1][i])

            item_widgets[2].blockSignals(False)

        for i in range(len(self.all_gear_widget_sets)):
            gear_widgets = self.all_gear_widget_sets[i]

            gear_widgets[2].blockSignals(True)

            gear_widgets[0].setEnabled(self.inventory_data[2][i] != 0)
            gear_widgets[1].setEnabled(self.inventory_data[2][i] != 0)
            gear_widgets[2].setValue(self.inventory_data[2][i])

            gear_widgets[2].blockSignals(False)
