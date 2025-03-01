from PySide6 import QtCore, QtGui, QtWidgets
from functools import partial

from cheatoglobin.constants import *

class PlayerInventoryTab(QtWidgets.QScrollArea):
    def __init__(self, parent):
        super().__init__()

        self.inventory_data = None
        self.parent = parent

        # ======================================================================================================================

        main = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(main)
        
        self.setWidget(main)
        self.setWidgetResizable(True)

        # coin count

        coin_count = QtWidgets.QWidget()
        coin_count_layout = QtWidgets.QHBoxLayout(coin_count)
        coin_count_layout.setContentsMargins(0, 0, 0, 0)

        padding = QtWidgets.QWidget()
        coin_count_layout.addWidget(padding)
        padding.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        coin_count_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"ITEM_COIN.png"))
        coin_count_icon = QtWidgets.QLabel()
        coin_count_icon.setPixmap(coin_count_icon_tex)
        coin_count_icon.setFixedWidth(16)
        coin_count_layout.addWidget(coin_count_icon)

        coin_count_label = QtWidgets.QLabel("Total &Coins:")
        #coin_count_label.setFixedWidth(64)
        coin_count_layout.addWidget(coin_count_label, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)

        self.coin_count_box = QtWidgets.QSpinBox()
        self.coin_count_box.setMaximum(999999)
        self.coin_count_box.textChanged.connect(partial(self.change_data, 0, 0))
        # self.coin_count_box.textChanged.connect(partial(self.change_data, current_player, stat))
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

            current_item_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"ITEM_{item[0]}.png"))
            current_item_icon = QtWidgets.QLabel()
            current_item_icon.setPixmap(current_item_icon_tex)
            current_item_icon.setFixedWidth(16)
            current_item_layout.addWidget(current_item_icon)

            current_item_name = QtWidgets.QLabel(item[1])
            current_item_layout.addWidget(current_item_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
            
            current_item_box = QtWidgets.QSpinBox()
            current_item_box.setMaximum(99)
            current_item_box.textChanged.connect(partial(self.change_data, 1, i))
            # current_item_box.textChanged.connect(partial(self.change_data, current_player, stat))
            current_item_layout.addWidget(current_item_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            item_counts_layout.addWidget(current_item, i // 4, i % 4)
            self.all_item_widget_sets.append((current_item_icon, current_item_name, current_item_box))
        
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

            current_gear_icon_tex = QtGui.QPixmap(str(FILES_DIR / f"GEAR_{gear[0]}.png"))
            current_gear_icon = QtWidgets.QLabel()
            current_gear_icon.setPixmap(current_gear_icon_tex)
            current_gear_icon.setFixedWidth(16)
            current_gear_layout.addWidget(current_gear_icon)

            current_gear_name = QtWidgets.QLabel(gear[1])
            current_gear_layout.addWidget(current_gear_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
            
            current_gear_box = QtWidgets.QSpinBox()
            current_gear_box.setMaximum(9)
            current_gear_box.textChanged.connect(partial(self.change_data, 2, i))
            # current_gear_box.textChanged.connect(partial(self.change_data, current_player, stat))
            current_gear_layout.addWidget(current_gear_box, alignment = QtCore.Qt.AlignmentFlag.AlignRight)

            gear_counts_layout.addWidget(current_gear, i // 4, i % 4)
            self.all_gear_widget_sets.append((current_gear_icon, current_gear_name, current_gear_box))
        
        main_layout.addWidget(gear_counts)

        # --------------------------------------------------------
    
    def change_data(self, data_type, stat, value):
        self.parent.set_edited(True)

        self.inventory_data[data_type][stat] = int(value, 0)
        self.set_data()
    
    def set_data(self):
        self.coin_count_box.setValue(self.inventory_data[0][0])

        for i in range(len(self.all_item_widget_sets)):
            item_widgets = self.all_item_widget_sets[i]

            item_widgets[0].setEnabled(self.inventory_data[1][i] != 0)
            item_widgets[1].setEnabled(self.inventory_data[1][i] != 0)
            item_widgets[2].setValue(self.inventory_data[1][i])

        for i in range(len(self.all_gear_widget_sets)):
            gear_widgets = self.all_gear_widget_sets[i]

            gear_widgets[0].setEnabled(self.inventory_data[2][i] != 0)
            gear_widgets[1].setEnabled(self.inventory_data[2][i] != 0)
            gear_widgets[2].setValue(self.inventory_data[2][i])
