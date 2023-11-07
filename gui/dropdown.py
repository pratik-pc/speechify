from PyQt5.QtWidgets import QComboBox

language_codes = {
  'Hindi': 'hi-IN',
  'Spanish': 'es-ES',
  'French': 'fr-FR'
}

class Dropdown(QComboBox):
  def __init__(self, audiorec, parent=None):
    super().__init__(parent)
    self.audiorec = audiorec
    self.addItem("Hindi")
    self.addItem("French")
    self.addItem("Spanish")
    self.activated.connect(self.on_activated)


  def on_activated(self):
    self.audiorec.language_code = language_codes[self.currentText()]
    