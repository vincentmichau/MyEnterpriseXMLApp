
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from version import APP_VERSION, APP_COMPANY

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('À propos')
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('<b>MyEnterpriseXMLApp</b>'), alignment=Qt.AlignCenter)
        layout.addWidget(QLabel(f'Version: {APP_VERSION}'), alignment=Qt.AlignCenter)
        layout.addWidget(QLabel(APP_COMPANY), alignment=Qt.AlignCenter)
        btn = QPushButton('Fermer'); btn.clicked.connect(self.accept)
        layout.addWidget(btn, alignment=Qt.AlignCenter)
