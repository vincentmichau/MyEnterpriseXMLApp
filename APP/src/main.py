from app.main import MainWindow
from PySide6.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)
w = MainWindow(); w.show(); sys.exit(app.exec())
