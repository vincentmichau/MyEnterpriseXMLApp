import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction

from version import APP_VERSION
from ui.about_dialog import AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyEnterpriseXMLApp")
        self.resize(800, 600)

        # ===== Menu =====
        menu_bar = self.menuBar()

        help_menu = menu_bar.addMenu("Aide")

        about_action = QAction("À propos", self)
        about_action.triggered.connect(
            lambda: AboutDialog(APP_VERSION).exec()
        )

        help_menu.addAction(about_action)


def run():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
