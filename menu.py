from nukesoundeditor.controller import SoundEditorController
#import nukesoundeditor

import nuke

play = SoundEditorController()
play._nuke_setting_sound()

def create_nse_menu() -> None:
    """NSE stands for Nuke Sound Editor"""
    menubar = nuke.menu("Nuke")
    nse_menu = menubar.addMenu("Nuke Sound Editor")

    nse_menu.addCommand(
        "Settings",
        "global nuke_sound_editor;nukesoundeditor.controller()",
        "",
    )

create_nse_menu()


def start_nse_editor() -> None:
    """Starts background processes for the Node Mailer."""
    global nuke_sound_editor
    nuke_sound_editor = nukesoundeditor.controller()

#start_nse_editor()

