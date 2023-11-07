from PyQt5.QtWidgets import QComboBox

class Dropdown(QComboBox):
  def __init__(self, audiorec, parent=None):
    super().__init__(parent)
    self.audiorec = audiorec
    self.addItem("Hindi")
    self.addItem("Bengali")
    self.addItem("Spanish")
    