from nukesoundeditor.view import SoundEditorView
from nukesoundeditor.model import SoundEditorModel
#import sys
from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import Qt
import nuke


class SoundEditorController:
    def __init__(self):
        self._view = SoundEditorView()
        self._model = SoundEditorModel()
        self._connect_interface()
        self._nuke_setting_sound()

    def open_interface(self):
        self._view.show()

    def _select_sound_file(self):
        select_sound_file_dialog = QFileDialog()
        select_sound_file_dialog.setNameFilter("select file (*.mp3 *.wav)")
        select_sound_file_dialog.exec_()
        if not select_sound_file_dialog.selectedFiles():
            self._view.selection_status.setText("You did not select a file")
            return
        
        self.output = select_sound_file_dialog.selectedFiles()[0]
        self._model._settings(self.output)
        self._view.selection_status.setText("Sound has been selected")
        self.path = self._model.mysettings.value("lineEdit")

    def _connect_interface(self):
        self._view.selection_button.clicked.connect(self._select_sound_file)

    def _nuke_setting_sound(self):
        nuke.addAfterRender(self._model.render_sound)

    def _checkbox_connect(self):
        self._view.check.stateChanged.connect(self._checkbox_change)
    
    def _checkbox_change(self, state):
        if state == Qt.Checked:
            self._view.selection_status.setText("RenderSound is enabled")

        else:
            self._view.selection_status.setText("RenderSound is disabled")





#myapp = QApplication(sys.argv)

#window = SoundEditorController()
#window.open_interface()
#myapp.exec_()