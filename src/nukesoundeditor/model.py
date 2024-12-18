from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl, QSettings

audio_player = QMediaPlayer()

def render_sound():
    if not is_render_sound_enabled():
        return
    
    audio_player.setMedia(QMediaContent(QUrl.fromLocalFile(QSettings.value("NukeRenderSounde/AudioFile"))))
    audio_player.setVolume(100) #TODO: volume bar
    audio_player.play()
    #global _player
    #_player = player

def initialize_settings(path=None):
    settings = QSettings()
    if not settings.contains("NukeRenderSounde/AudioFile"):
        settings.setValue("NukeRenderSounde/AudioFile", "C:/pipeline/nuke/NukeRenderSound/rnd_okay.wav")
    if not settings.contains("NukeRenderSounde/AudioFile/Enabled"):
        settings.setValue("NukeRenderSounde/AudioFile/Enabled", "True")


def set_sound_file_path(path):
    QSettings().setValue("NukeRenderSounde/AudioFile", path)

def is_render_sound_enabled():
    return QSettings.value("NukeRenderSounde/AudioFile/Enabled") == "True"

def set_render_sound_enabled(enabled):
    QSettings().setValue("NukeRenderSounde/AudioFile/Enabled", "True" if enabled else "False")

def sound_volume(value):
    audio_player.setVolume(int(value))