import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.ui.ui_output.main_window import Ui_MainWindow

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


window_width = 1200
window_height = 700


def initWindow() -> QApplication:
    app = QApplication(sys.argv)
    window = QMainWindow()
    start_x = (app.primaryScreen().size().width() - window_width)/2
    start_y = (app.primaryScreen().size().height() - window_height)/2
    window.setGeometry(start_x, start_y, window_width, window_height)
    window.setWindowTitle("Flappy Bird AI")

    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initWindow()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
