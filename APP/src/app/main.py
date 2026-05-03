from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction
import sys

from core.i18n import I18N
from ui.xml_tree import XMLTree
from version import APP_NAME


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.i18n = I18N('fr')
        self.setWindowTitle(APP_NAME)
        self.resize(1000, 700)

        self.xml_view = XMLTree(self.i18n)
        self.setCentralWidget(self.xml_view)

        bar = self.menuBar()

        self.file_menu = bar.addMenu(self.i18n.t('file'))
        quit_action = QAction(self.i18n.t('quit'), self)
        quit_action.triggered.connect(self.close)
        self.file_menu.addAction(quit_action)

        self.help_menu = bar.addMenu(self.i18n.t('help'))
        about_action = QAction(self.i18n.t('about'), self)
        self.help_menu.addAction(about_action)


def run():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
