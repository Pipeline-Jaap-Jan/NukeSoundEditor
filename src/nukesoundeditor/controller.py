from nukesoundeditor.view import SoundEditorView
import sys
from PySide2.QtWidgets import QApplication, QFileDialog


class SoundEditorController:
    def __init__(self):
        self._view = SoundEditorView()

        self._connect_interface()

    def open_interface(self):
        self._view.show()

    def _select_sound_file(self):
        select_sound_file_dialog = QFileDialog()
        select_sound_file_dialog.setNameFilter("select file (*.mp3 *.wav)")
        select_sound_file_dialog.exec_()
        if not select_sound_file_dialog.selectedFiles():
            print("You did not select a file")
            return
        
        output = select_sound_file_dialog.selectedFiles()[0]
        #renderSound(output)
        self._view.selection_status.setText("Sound has been selected")

    def _connect_interface(self):
        self._view.selection_button.clicked.connect(self._select_sound_file)

myapp = QApplication(sys.argv)

#sys.exit()
window = SoundEditorController()
window.open_interface()
myapp.exec_()
