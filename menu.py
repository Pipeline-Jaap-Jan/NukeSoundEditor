from nukesoundeditor.controller import SoundEditorController
import nuke

def _create_nse_menu() -> None:
    """NSE stands for Nuke Sound Editor"""
    menubar = nuke.menu("Nuke")
    nse_menu = menubar.addMenu("Nuke Sound Editor")

    nse_menu.addCommand(
        "Settings",
        "start_nse_editor()",
        "",
    )

def start_nse_editor() -> None:
    global nuke_sound_editor
    nuke_sound_editor = SoundEditorController()
    nuke_sound_editor.open_interface()
    nuke_sound_editor.nuke_setting_sound()

play = SoundEditorController()
play.nuke_setting_sound()

_create_nse_menu()
