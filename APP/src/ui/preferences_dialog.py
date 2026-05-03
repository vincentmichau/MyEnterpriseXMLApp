
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton
import json
from pathlib import Path

CONFIG = Path.home() / '.myenterprisexmlapp' / 'config.json'
CONFIG.parent.mkdir(exist_ok=True)

class PreferencesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Préférences')
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel('Langue'))
        self.lang = QComboBox(); self.lang.addItems(['fr', 'en'])
        layout.addWidget(self.lang)

        layout.addWidget(QLabel('Thème'))
        self.theme = QComboBox(); self.theme.addItems(['clair', 'sombre'])
        layout.addWidget(self.theme)

        save = QPushButton('Enregistrer')
        save.clicked.connect(self.save)
        layout.addWidget(save)

        self.load()

    def load(self):
        if CONFIG.exists():
            data = json.load(open(CONFIG))
            self.lang.setCurrentText(data.get('lang','fr'))
            self.theme.setCurrentText(data.get('theme','clair'))

    def save(self):
        json.dump({'lang': self.lang.currentText(), 'theme': self.theme.currentText()}, open(CONFIG,'w'))
        self.accept()
