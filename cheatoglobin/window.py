import os
import sys
import struct
from random import choice
from PySide6 import QtCore, QtGui, QtWidgets
import ndspy.rom

from cheatoglobin.constants import *
from cheatoglobin.save_file_tab import SaveFileTab, SaveData

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(f"No Currently Opened File - {APP_DISPLAY_NAME}")
        self.setWindowIcon(QtGui.QIcon(str(FILES_DIR / 'cheatoglobin.ico')))

        self.lang = 1
        self.rng = choice([0, 1]), choice([0, 1])

        self.has_rom = False
        self.import_rom()

        menu_bar = self.menuBar()
        menu_bar_file = menu_bar.addMenu("&File")
        menu_bar_file.addAction(
            "&Open",
            QtGui.QKeySequence.StandardKey.Open,
            self.import_files,
        )
        menu_bar_file.addAction(
            "&Save",
            QtGui.QKeySequence.StandardKey.Save,
            self.export_files,
        )
        menu_bar_file.addAction(
            "Save &As...",
            QtGui.QKeySequence.StandardKey.SaveAs,
            self.export_files_as,
        )
        menu_bar_file.addSeparator() # -----------------------------------------
        menu_bar_file.addAction(
            "&Quit",
            QtGui.QKeySequence.StandardKey.Quit,
            QtWidgets.QApplication.quit,
        )

        # ======================================================================================================================

        # file selector

        file_tabs = QtWidgets.QTabWidget()

        self.file_1_tab = SaveFileTab(self, file_tabs, "Save Slot &1", self.has_rom)
        self.file_2_tab = SaveFileTab(self, file_tabs, "Save Slot &2", self.has_rom)

        file_tabs.addTab(self.file_1_tab, self.file_1_tab.name)
        file_tabs.addTab(self.file_2_tab, self.file_1_tab.name)

        self.setCentralWidget(file_tabs)

        QtWidgets.QMessageBox.information(
            self,
            "Choose a Save File",
            f"Please choose a Bowser's Inside Story Save File to open.",
        )

        if not self.import_files():
            sys.exit(2)
    
    def import_files(self):
        file_path, _selected_filter = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Open Save File",
            filter=NDS_SAVE_FILENAME_FILTER,
        )
        if file_path == '':
            return False
            
        self.setWindowTitle(f"{os.path.basename(file_path)} - {APP_DISPLAY_NAME}")
        self.current_path = file_path
        
        with open(file_path, 'rb') as save_file:
            if save_file.read(6) != b"MLRPG3":
                QtWidgets.QMessageBox.warning(
                    self,
                    "Invalid File",
                    f"The chosen file is not a Bowser's Inside Story Save File.",
                )
                return False
            
            slot_offsets = (0x0010, 0x0FE8)
            save_data_set = []

            for current_slot in range(2):
                current_save_slot_data = SaveData()

                # player stats data
                # ---------------------------------------------------------
                save_file.seek(slot_offsets[current_slot] + 0x0000)

                for current_player in range(3): # mario stats, luigi stats, bowser stats
                    current_save_slot_data.player_stats[current_player].extend(struct.unpack('<8hb', save_file.read(0x11)))
                    current_save_slot_data.player_stats[current_player].append(int.from_bytes(save_file.read(3), "little")) # EXP being a bitch
                    current_save_slot_data.player_stats[current_player].extend(struct.unpack('<3B', save_file.read(0x03)))
                    save_file.seek(1, 1)
                    current_save_slot_data.badge_data[0].append(int.from_bytes(save_file.read(1)))
                    save_file.seek(3, 1)

                # player inventory data
                # ---------------------------------------------------------
                save_file.seek(slot_offsets[current_slot] + 0x0054)
                
                current_save_slot_data.inventory[0][0] = int.from_bytes(save_file.read(4), "little") # coin count
                current_save_slot_data.inventory[1].extend(struct.unpack('<26b', save_file.read(0x1A))) # item counts
                ## ?? ?? ?? ?? ?? ?? ?? - nothing seems to affect anything here
                save_file.seek(7, 1)
                current_save_slot_data.inventory[2].extend(struct.unpack('<127b', save_file.read(0x7F))) # gear counts
                current_save_slot_data.badge_data[1][0] = int.from_bytes(save_file.read(1)) # badge collection bitfield
                save_file.seek(11, 1)
                ## ?? ?? ?? TT TT TT TT ?? ?? ?? ??
                ## TT = game timer (in frames)
                current_save_slot_data.badge_data[2].extend(struct.unpack('<2H', save_file.read(0x4))) # badge meters

                # ---------------------------------------------------------
            
                save_data_set.append(current_save_slot_data)
            
            self.file_1_tab.set_data(save_data_set[0])
            self.file_2_tab.set_data(save_data_set[1])

            save_file.seek(0)
            self.preserved_file = save_file.read()

        self.file_1_tab.set_edited(False)
        self.file_2_tab.set_edited(False)

        return True
        
    def export_files_as(self):
        file_path, selected_filter = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption="Save .sav File",
            dir=self.current_path,
            filter=NDS_SAVE_FILENAME_FILTER,
        )

        if file_path == '':
            return
        self.current_path = file_path

        self.export_files()
        
    def export_files(self):
        self.file_1_tab.set_edited(False)
        self.file_2_tab.set_edited(False)

        slot_offsets = (0x0010, 0x0FE8)

        with open(self.current_path, 'w+b') as save_file:
            save_file.write(self.preserved_file)
            current_save_slot_data = [self.file_1_tab.get_data(), self.file_2_tab.get_data()]
            for current_slot in range(2):
                # player stats data
                # ---------------------------------------------------------
                save_file.seek(slot_offsets[current_slot] + 0x0000)

                for current_player in range(3): # mario stats, luigi stats, bowser stats
                    save_file.write(struct.pack('<8hb', *current_save_slot_data[current_slot].player_stats[current_player][:9]))
                    save_file.write(current_save_slot_data[current_slot].player_stats[current_player][9].to_bytes(3, 'little')) # EXP being a bitch
                    save_file.write(struct.pack('<3B', *current_save_slot_data[current_slot].player_stats[current_player][10:]))
                    save_file.seek(1, 1)
                    save_file.write(current_save_slot_data[current_slot].badge_data[0][current_player].to_bytes(1))
                    save_file.seek(3, 1)

                # player inventory data
                # ---------------------------------------------------------
                save_file.seek(slot_offsets[current_slot] + 0x0054)
                
                save_file.write(struct.pack('<i', current_save_slot_data[current_slot].inventory[0][0])) # coin count
                save_file.write(struct.pack('<26b', *current_save_slot_data[current_slot].inventory[1])) # item counts
                save_file.seek(7, 1)
                save_file.write(struct.pack('<127b', *current_save_slot_data[current_slot].inventory[2])) # gear counts
                save_file.write(current_save_slot_data[current_slot].badge_data[1][0].to_bytes(1)) # badge collection bitfield
                save_file.seek(11, 1)
                save_file.write(struct.pack('<2H', *current_save_slot_data[current_slot].badge_data[2])) # badge meters

                # checksum
                # ---------------------------------------------------------
                
                save_file.seek(slot_offsets[current_slot])
                checksum = sum(struct.unpack('<761H', save_file.read(0x5F2))) % 0xFFFF
                save_file.write(struct.pack('<H', 0xFFFF - checksum))

                # backup
                # ---------------------------------------------------------

                save_file.seek(slot_offsets[current_slot])
                backup_file = save_file.read(0x5F4)
                save_file.seek(slot_offsets[current_slot] + 0x7EC)
                save_file.write(backup_file)

    def import_rom(self): # TO DO: make the user be able to import other ROMs or whatever, do what spritoglobin does
        self.has_rom = True

        path = "BISROM.nds"
        rom = ndspy.rom.NintendoDSRom.fromFile(path)

        if rom.idCode[3] == 69 or rom.idCode[3] == 80:                                                               # US-base
            self.overlay_MObj = rom.loadArm9Overlays([132])[132].data
            self.overlay_MObj_offsets = (0x20F0, 0x2E94, 0x2C80) # filedata, sprite groups, palette groups
            self.rom_base = 1
        else:                                                                                                        # JP-base
            self.overlay_MObj = rom.loadArm9Overlays([126])[126].data
            self.overlay_MObj_offsets = (0x209C, 0x2DA0, 0x2BA0) # filedata, sprite groups, palette groups
            self.rom_base = 0
        
        self.MObj_file = rom.getFileByName('MObj/MObj.dat')