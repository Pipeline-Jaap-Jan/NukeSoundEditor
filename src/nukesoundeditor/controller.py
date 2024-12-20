from nukesoundeditor.view import SoundEditorView
from nukesoundeditor import model
from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import Qt
import nuke


class SoundEditorController:
    def __init__(self):
        self._view = SoundEditorView()
        self._connect_interface()
        self._checkbox_connect()
        self.nuke_setting_sound()
        self._save_button_connect()
        self._standard_checking()
        self._slider_control()

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
        model.set_sound_file_path(self.output)
        self._view.selection_status.setText("Sound has been selected")

    def _connect_interface(self):
        self._view.selection_button.clicked.connect(self._select_sound_file)

    def nuke_setting_sound(self):
        if model.is_render_sound_enabled():
            nuke.addAfterRender(model.render_sound)

    def _checkbox_connect(self):
        self._view.check.stateChanged.connect(self._checkbox_change)
    
    def _checkbox_change(self, state):
        if state == Qt.Checked:
            self._view.selection_status.setText("RenderSound is enabled")
            model.set_render_sound_enabled(True)
        else:
            self._view.selection_status.setText("RenderSound is disabled")
            model.set_render_sound_enabled(False)


    def _save_button_connect(self):
        self._view.save_button.clicked.connect(self.exit_app)

    def exit_app(self):
        self._view.close()

    def _standard_checking(self):
        self._view.check.setChecked(model.is_render_sound_enabled())

    def _slider_control(self):
        value = self._view.slider.value()
        self._view.slider.sliderReleased.connect(model.set_render_sound_volume(value))
        self._view.slider.sliderReleased.connect(model.render_sound)
        self._view.slider.sliderReleased.connect(print(model.render_sound_value()))
        #self._view._volume_bar(model.render_sound_value)
        self._view.slider.setSliderPosition(int(100))
        self._view.slider.valueChanged.connect(self._view.changed_value)


