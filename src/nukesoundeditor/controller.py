from sound_editor.view import SoundEditorView
import sys
from PySide2.QtWidgets import QApplication


class SoundEditorController:
    def __init__(self):
        self._view = SoundEditorView()

    def open_interface(self):
        self._view.show()


myapp = QApplication(sys.argv)

myapp.exec_()
sys.exit()
window = SoundEditorController()
window.open_interface()