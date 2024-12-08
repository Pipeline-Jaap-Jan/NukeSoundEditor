from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl
from PySide2.QtCore import QSettings

class SoundEditorModel:
    def __init__(self):
        self._settings()

    def render_sound(self):
        player = QMediaPlayer()
        player.setMedia(QMediaContent(QUrl.fromLocalFile(self.mysettings.value("lineEdit"))))
        player.setVolume(100)
        player.play()
        global _player
        _player = player

    def _settings(self, path=None):
        self.mysettings = QSettings("MyCompany", "MyApp")
        if path is not None or not self.mysettings.contains("lineEdit"):
            self.mysettings.setValue("lineEdit", path or "C:/Users/Jaap-Jan.vandeGeest/Documents/GitHub/core/nuke/NukeRenderSound/rnd_okay.wav")



#nuke.addAfterRender(renderSound)

#def pathremember():
