
import sys, requests
from PySide6.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from ui.about_dialog import AboutDialog
from ui.preferences_dialog import PreferencesDialog
from ui.xml_screen import XMLScreen
from version import APP_VERSION, UPDATE_URL

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MyEnterpriseXMLApp')
        self.resize(900,600)

        self.setCentralWidget(XMLScreen())

        bar = self.menuBar()
        file = bar.addMenu('Fichier')
        pref = QAction('Préférences',self); pref.triggered.connect(self.open_prefs)
        quit = QAction('Quitter',self); quit.triggered.connect(self.close)
        file.addActions([pref, quit])

        helpm = bar.addMenu('Aide')
        about = QAction('À propos',self); about.triggered.connect(lambda: AboutDialog().exec())
        update = QAction('Vérifier mises à jour',self); update.triggered.connect(self.check_update)
        helpm.addActions([about, update])

    def open_prefs(self):
        PreferencesDialog().exec()

    def check_update(self):
        try:
            latest = requests.get(UPDATE_URL, timeout=5).json()['tag_name']
            if latest != APP_VERSION:
                QMessageBox.information(self,'Mise à jour',f'Nouvelle version disponible: {latest}')
            else:
                QMessageBox.information(self,'Mise à jour','Vous êtes à jour')
        except Exception:
            QMessageBox.warning(self,'Mise à jour','Impossible de vérifier les mises à jour')


def run():
    app = QApplication(sys.argv)
    w = MainWindow(); w.show()
    sys.exit(app.exec())
