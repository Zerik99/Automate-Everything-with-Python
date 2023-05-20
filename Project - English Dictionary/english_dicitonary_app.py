"""Version 1: English Dictionary GUI app. An app to provide the definition of a user given word."""  # docstring
import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QScrollArea,
)


# methods
def define_word() -> None:
    """Define the word typed in the input field and update the definition label"""
    in_word: str = word_input.text().lower()

    with open(
        "Project - English Dictionary/files/data.json", "r", encoding="utf-8"
    ) as file:
        words_data: dict[str, str] = json.load(file)

    get_definition(in_word=in_word, words_data=words_data)


def get_definition(in_word: str, words_data: dict[str, str]) -> None:
    """Build the definition of the word"""
    for word in words_data:
        definition: str = ""

        if word.find(in_word) == -1 or in_word != word:
            continue

        definition += f"<b>{word.capitalize()}</b>:<br>"

        for word_definition in words_data[word]:
            definition += f"{word_definition}<br><br>"

        definition += "<br>"

        print(definition)
        build_definition_labels(definition=definition)


def build_definition_labels(definition: str) -> None:
    """Build the definition labels"""
    definition_label = QLabel(definition)
    definition_label.setWordWrap(True)
    definition_label.setMinimumWidth(400)
    definition_label.setStyleSheet("font-size: 16px; margin: 10px;")
    definition_scroll.setWidget(definition_label)


# Create the app and the window
app = QApplication([])
window = QWidget()
window.setWindowTitle("English Dictionary")
window.setMaximumHeight(400)

# Create the layouts
main_layout = QVBoxLayout()
input_layout = QHBoxLayout()
definition_scroll = QScrollArea()

# Create the widgets
word_input = QLineEdit()
define_btn = QPushButton("Define")
message_label = QLabel("")

# style the widgets
word_input.setPlaceholderText("Enter a word to define")
word_input.setMinimumWidth(400)
define_btn.setFixedWidth(100)

# setup signals and slots
define_btn.clicked.connect(define_word)

# Add widgets to layouts
input_layout.addWidget(word_input, alignment=Qt.AlignmentFlag.AlignLeft)
input_layout.addWidget(define_btn, alignment=Qt.AlignmentFlag.AlignRight)
main_layout.addLayout(input_layout)
main_layout.addWidget(definition_scroll)

# set the window layout and execute the app

window.setLayout(main_layout)
window.show()
app.exec()
