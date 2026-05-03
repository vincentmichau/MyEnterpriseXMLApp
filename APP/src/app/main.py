
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAction
from core.i18n import I18N
from ui.xml_tree import XMLTree
from version import APP_NAME

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.i18n = I18N('fr')
        self.setWindowTitle(APP_NAME)
        self.resize(900,600)

        self.xml_view = XMLTree(self.i18n)
        self.setCentralWidget(self.xml_view)

        bar = self.menuBar()
        file_menu = bar.addMenu(self.i18n.t('file'))
        quit_action = QAction(self.i18n.t('quit'), self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        help_menu = bar.addMenu(self.i18n.t('help'))
        about_action = QAction(self.i18n.t('about'), self)
        about_action.triggered.connect(lambda:None)
        help_menu.addAction(about_action)

    def change_lang(self, lang):
        self.i18n.load(lang)
