
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from lxml import etree
from core.logger import get_logger

log = get_logger(__name__)

class XMLScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        btn = QPushButton('Importer XML')
        btn.clicked.connect(self.load_xml)
        layout.addWidget(btn)
        layout.addWidget(self.text)

    def load_xml(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Choisir un fichier XML', '', 'XML (*.xml)')
        if not path:
            return
        try:
            tree = etree.parse(path)
            self.text.setPlainText(etree.tostring(tree, pretty_print=True).decode())
            log.info(f'XML importé: {path}')
        except Exception as e:
            self.text.setPlainText(str(e))
            log.error(str(e))
