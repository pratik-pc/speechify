from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  
  def initUI(self):
        self.setWindowTitle('Speechify')
        self.setGeometry(100, 100, 300, 150)