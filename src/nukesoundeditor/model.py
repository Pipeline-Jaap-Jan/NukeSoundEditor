from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl, QSettings

class SoundEditorModel:
    def __init__(self):
        self._initialize_settings()

    def _initialize_settings(self, path=None):
        self.mysettings = QSettings("MyCompany", "MyApp")
        if not self.mysettings.contains("lineEdit"):
            self.mysettings.setValue("lineEdit", "C:/pipeline/nuke/NukeRenderSound/rnd_okay.wav")
        if not self.mysettings.contains("enable"):
            self.mysettings.setValue("enable", "True")

    def render_sound(self):
        if not self._is_render_sound_enabled:
            return
        
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.mysettings.value("lineEdit"))))
        self.player.setVolume(100) #TODO: volume bar
        self.player.play()
        global _player
        _player = self.player

    def _set_sound_file_path(self, path):
        self.mysettings.setValue("lineEdit", path)

    def _is_render_sound_enabled(self):
        return self.mysettings.value("enable") == "True"

    def _set_render_sound_enabled(self, enable):
        self.mysettings.setValue("enable", "True" if enable else "False")