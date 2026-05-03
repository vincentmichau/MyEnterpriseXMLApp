from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from pathlib import Path
import sys


def is_portable():
    if not getattr(sys, 'frozen', False):
        return False
    app_dir = Path(sys.executable).parent
    return (app_dir / "portable.flag").exists()


class AboutDialog(QDialog):
    def __init__(self, version: str):
        super().__init__()

        self.setWindowTitle("À propos")
        self.setFixedSize(300, 220)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("<b>MyEnterpriseXMLApp</b>")
        title.setAlignment(Qt.AlignCenter)

        version_label = QLabel(f"Version : {version}")
        version_label.setAlignment(Qt.AlignCenter)

        mode = "Portable" if is_portable() else "Installée"
        mode_label = QLabel(f"Mode : {mode}")
        mode_label.setAlignment(Qt.AlignCenter)

        company_label = QLabel("© Luz Informatique")
        company_label.setAlignment(Qt.AlignCenter)

        close_button = QPushButton("Fermer")
        close_button.clicked.connect(self.close)

        layout.addWidget(title)
        layout.addWidget(version_label)
        layout.addWidget(mode_label)
        layout.addSpacing(10)
        layout.addWidget(company_label)
        layout.addStretch()
        layout.addWidget(close_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
