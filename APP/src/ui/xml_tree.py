
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTreeView, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from lxml import etree

class XMLTree(QWidget):
    def __init__(self, i18n):
        super().__init__()
        self.i18n = i18n
        layout = QVBoxLayout(self)
        self.tree = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Element", "Value"]) 
        self.tree.setModel(self.model)
        btn = QPushButton(self.i18n.t('import_xml'))
        btn.clicked.connect(self.load_xml)
        layout.addWidget(btn)
        layout.addWidget(self.tree)

    def load_xml(self):
        path,_ = QFileDialog.getOpenFileName(self, 'XML', '', 'XML (*.xml)')
        if not path:
            return
        tree = etree.parse(path)
        self.model.removeRows(0, self.model.rowCount())
        self._add_element(self.model.invisibleRootItem(), tree.getroot())

    def _add_element(self, parent, element):
        item = QStandardItem(element.tag)
        value = QStandardItem(element.text.strip() if element.text else '')
        parent.appendRow([item, value])
        for child in element:
            self._add_element(item, child)
