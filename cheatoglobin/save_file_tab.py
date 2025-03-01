from PySide6 import QtCore, QtGui, QtWidgets

from cheatoglobin.player_stats_tab import PlayerStatsTab
from cheatoglobin.player_inventory_tab import PlayerInventoryTab

class SaveFileTab(QtWidgets.QTabWidget):
    def __init__(self, parent, tab_parent, name):
        super().__init__()

        self.parent = parent
        self.tab_parent = tab_parent
        self.name = name

        # ======================================================================================================================

        # category selector

        self.player_stats_tab = PlayerStatsTab(self)
        self.player_inventory_tab = PlayerInventoryTab(self)
        
        self.addTab(self.player_stats_tab, "Player Stats")
        self.addTab(self.player_inventory_tab, "Inventory")
    
    def set_data(self, data):
        self.player_stats_tab.stats_data = data.player_stats
        self.player_stats_tab.set_data()
        
        self.player_inventory_tab.inventory_data = data.inventory
        self.player_inventory_tab.set_data()
    
    def get_data(self):
        return_save = SaveData()
        return_save.player_stats = self.player_stats_tab.stats_data
        return_save.inventory = self.player_inventory_tab.inventory_data

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