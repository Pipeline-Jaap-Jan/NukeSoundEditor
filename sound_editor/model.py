#def pathremember():
    

def renderSound(soundpath):
    player = QMediaPlayer()
    player.setMedia(QMediaContent(QUrl.fromLocalFile(soundpath)))
    player.setVolume(100)
    player.play()
    global _player
    _player = player
