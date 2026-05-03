import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QWidget, QVBoxLayout
)
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

        file_menu = menu_bar.addMenu("Fichier")
        quit_action = QAction("Quitter", self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        help_menu = menu_bar.addMenu("Aide")
        about_action = QAction("À propos", self)
        about_action.triggered.connect(
            lambda: AboutDialog(APP_VERSION).exec()
        )
        help_menu.addAction(about_action)

        # ===== Central widget =====
        central_widget = QWidget(self)
        layout = QVBoxLayout()

        quit_button = QPushButton("Quitter")
        quit_button.clicked.connect(self.close)

        layout.addStretch()
        layout.addWidget(quit_button)
        layout.addStretch()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
