import sys
from PySide6 import QtWidgets

from cheatoglobin.window import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()