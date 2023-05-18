from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
)


def make_sentence() -> None:
    """a method to capitalize the input text and display it in the output label"""
    input_text: str = text.text()
    output_label.setText(input_text.capitalize())


app = QApplication([])
window = QWidget()
window.setWindowTitle("Sentence Builder")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Build!")
layout.addWidget(btn)

output_label = QLabel("")
layout.addWidget(output_label)

btn.clicked.connect(make_sentence)

window.setLayout(layout)
window.show()
app.exec()
