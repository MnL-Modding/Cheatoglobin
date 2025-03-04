from PySide6 import QtCore, QtGui, QtWidgets

from cheatoglobin.image import create_MObj_sprite
from cheatoglobin.player_stats_tab import PlayerStatsTab
from cheatoglobin.player_inventory_tab import PlayerInventoryTab
from cheatoglobin.player_abilities_tab import PlayerAbilitiesTab

class SaveFileTab(QtWidgets.QTabWidget):
    def __init__(self, parent, tab_parent, name, has_rom):
        super().__init__()

        self.parent = parent
        self.tab_parent = tab_parent
        self.name = name

        # ======================================================================================================================

        # category selector

        self.player_stats_tab = PlayerStatsTab(self, has_rom)
        self.player_inventory_tab = PlayerInventoryTab(self, has_rom)
        self.player_abilities_tab = PlayerAbilitiesTab(self, has_rom)

        if self.parent.has_rom:
            tab_icons = [
                QtGui.QIcon(QtGui.QIcon(create_MObj_sprite(self.parent.overlay_MObj_offsets, self.parent.overlay_MObj,  self.parent.MObj_file, 11, 2 + self.parent.rng[0], self.parent.lang))),
                QtGui.QIcon(QtGui.QIcon(create_MObj_sprite(self.parent.overlay_MObj_offsets, self.parent.overlay_MObj,  self.parent.MObj_file, 9, 24 + (self.parent.rng[1] * 6), self.parent.lang))),
                QtGui.QIcon(QtGui.QIcon(create_MObj_sprite(self.parent.overlay_MObj_offsets, self.parent.overlay_MObj,  self.parent.MObj_file, 31, 4 - (self.parent.rng[0] * 4), self.parent.lang))),
            ]
        else:
            tab_icons = [
                QtGui.QIcon(),
                QtGui.QIcon(),
                QtGui.QIcon(),
            ]
        
        self.addTab(self.player_stats_tab, tab_icons[0], "Player &Stats")
        self.addTab(self.player_inventory_tab, tab_icons[1], "&Inventory")
        self.addTab(self.player_abilities_tab, tab_icons[2], "&Badges and Abilities")
    
    def set_data(self, data):
        self.player_stats_tab.stats_data = data.player_stats
        self.player_stats_tab.set_data()
        
        self.player_inventory_tab.inventory_data = data.inventory
        self.player_inventory_tab.set_data()
        
        self.player_abilities_tab.badge_data = data.badge_data
        self.player_abilities_tab.set_data()
    
    def get_data(self):
        return_save = SaveData()
        return_save.player_stats = self.player_stats_tab.stats_data
        return_save.inventory = self.player_inventory_tab.inventory_data
        return_save.badge_data = self.player_abilities_tab.badge_data

        return return_save
    
    def set_edited(self, edited):
        if edited:
            self.tab_parent.setTabText(self.tab_parent.indexOf(self), self.name + "*")
        else:
            self.tab_parent.setTabText(self.tab_parent.indexOf(self), self.name)

class SaveData():
    def __init__(self):
        self.player_stats = [[], [], []] # mario stats, luigi stats, bowser stats
        self.inventory = [[0], [], []] # coin count, item list, gear list
        self.badge_data = [[], [0], []] # equipped badges, badge collection bitfield, meter progress
