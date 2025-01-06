from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl, QSettings

audio_player = QMediaPlayer()

def render_sound():
    if not is_render_sound_enabled():
        return
    
    audio_player.setMedia(QMediaContent(QUrl.fromLocalFile(QSettings().value("NukeRenderSound/AudioFile"))))
    audio_player.setVolume(int(QSettings().value("NukeRenderSound/AudioFile/Volume")))
    audio_player.play()

def initialize_settings(path=None):
    settings = QSettings()
    if not settings.contains("NukeRenderSound/AudioFile"):
        settings.setValue("NukeRenderSound/AudioFile", "C:/pipeline/nuke/NukeRenderSound/rnd_okay.wav")
    if not settings.contains("NukeRenderSound/AudioFile/Enabled"):
        settings.setValue("NukeRenderSound/AudioFile/Enabled", "True")
    if not settings.contains("NukeRenderSound/AudioFile/Volume"):
        settings.setValue("NukeRenderSound/AudioFile/Volume", "100")


def set_sound_file_path(path):
    QSettings().setValue("NukeRenderSound/AudioFile", path)

def is_render_sound_enabled():
    return QSettings().value("NukeRenderSound/AudioFile/Enabled") == "True"

def set_render_sound_enabled(enabled):
    QSettings().setValue("NukeRenderSound/AudioFile/Enabled", "True" if enabled else "False")

def set_render_sound_volume(volume):
    QSettings().setValue("NukeRenderSound/AudioFile/Volume", volume)

initialize_settings()