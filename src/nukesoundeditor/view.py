from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QCheckBox

class SoundEditorView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(300,300,500,400)
        self.layout = self._create_layout()
        self.setLayout(self.layout)

    def _create_layout(self):
        self._create_button()
        self._create_checkbox()
        self._create_save_button()
        #self._create_sound_file_selection_dialog()

        editor_layout = QVBoxLayout()
        editor_layout.addWidget(self.selection_button)
        editor_layout.addWidget(self.check)
        editor_layout.addWidget(self.selection_status)
        editor_layout.addWidget(self.save_button)
        #editor_layout.addWidget(self.select_sound_file_dialog)
        return editor_layout

    def _create_button(self):
        self.selection_button = QPushButton("Select Audio File", self)

    def _create_checkbox(self):
        self.selection_status = QLabel()
        self.check = QCheckBox("RenderSound", self)
        self.check.setChecked(True)

    def _create_save_button(self):
        self.save_button = QPushButton("Save & Quit", self)








