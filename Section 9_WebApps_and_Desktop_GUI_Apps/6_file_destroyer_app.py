"""File Destroyer App"""
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QFileDialog,
)


# app functionality
def open_files():
    """Select the file(s) to be destroyed"""
    global filenames  # global variable to store the filenames... Not the best practice.
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")

    set_selected_files_label()


def set_selected_files_label():
    """Set the selected files label"""
    msg: str = ""
    for filename in filenames:
        msg += Path(filename).name + "\n"
    selected_files.setText(f"Selected Files:\n{msg}")


def destroy_files():
    """Destroy the selected file(s)"""
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as file:
            file.write(b"")
        path.unlink()
    selected_files.setText("No Files Selected")


# Create the app and the window
app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

# Create the layouts
layout = QVBoxLayout()

# Create the widgets
description = QLabel(
    "Select the files you want to destory. \
    The files will be <font color ='red'>permanently</font> deleted."
)
open_btn = QPushButton("Open File(s)")
open_btn.setToolTip("Click to select the file(s) you want to destroy")
open_btn.setFixedWidth(150)

destroy_button = QPushButton("Destroy File(s)")
destroy_button.setToolTip("Click to destroy the selected file(s)")
destroy_button.setFixedWidth(150)

selected_files = QLabel("No Files Selected")

# Add functionality to the widgets
open_btn.clicked.connect(open_files)
destroy_button.clicked.connect(destroy_files)

# Add widgets to layouts
layout.addWidget(description, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(destroy_button, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(selected_files, alignment=Qt.AlignmentFlag.AlignLeft)

# set the window layout and execute the app
window.setLayout(layout)
window.show()
app.exec()
