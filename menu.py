import sound_editor
import nuke

"""NSE stands for Nuke Sound Editor"""

def create_nse_menu() -> None:
    menubar = nuke.menu("Nuke")
    nse_menu = menubar.addMenu("Nuke Sound Editor")

    nse_menu.addCommand(
        "Settings",
        "global node_mailer_controller;sound_editor.open_sound_editor()",
        "",
    )

create_nse_menu()


def start_node_mailer() -> None:
    """Starts background processes for the Node Mailer."""
    global node_mailer_controller
    node_mailer_controller = sound_editor.SoundEditorController()

start_node_mailer()

