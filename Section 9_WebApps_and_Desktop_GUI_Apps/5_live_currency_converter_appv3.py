"""PyQt6 imports"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox,
)
from bs4 import BeautifulSoup
import requests


def get_currency(in_currency: str, out_currency: str) -> float:
    """a method to get the conversion rate between two currencies"""

    url: str = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    response: str = requests.get(url=url, timeout=5).text
    soup = BeautifulSoup(response, "html.parser")
    rate: str = soup.find("span", class_="ccOutputRslt").get_text()
    rate_float: float = float(rate[:-4])
    return rate_float


def show_currency() -> None:
    """a method to capitalize the input text
    and display it in the output label"""

    in_curr: str = in_combo.currentText()
    out_curr: str = out_combo.currentText()

    input_text: str = text.text()
    conversion_rate: float = get_currency(in_currency=in_curr, out_currency=out_curr)

    converted_amount: float = round(float(input_text) * conversion_rate, 2)

    msg: str = f"{input_text} {in_curr.upper()} = {converted_amount} {out_curr.upper()}"

    output_label.setText(msg)


# --------Creating the app and the window---------#
app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

# --------Creating the layouts---------#
user_interaction_Vlayout = QVBoxLayout()
currency_dd_Vlayout = QVBoxLayout()
inner_Hlayout = QHBoxLayout()
outer_Vlayout = QVBoxLayout()

currencies: list[str] = ["usd", "eur", "gbp"]

# --------Currency dd Vbox layout---------#
in_combo = QComboBox()
in_combo.addItems(currencies)
currency_dd_Vlayout.addWidget(in_combo)

label1 = QLabel(text="to")
label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
currency_dd_Vlayout.addWidget(label1)

out_combo = QComboBox()
out_combo.addItems(currencies)
currency_dd_Vlayout.addWidget(out_combo)

# --------user interaction vbox layout---------#
text = QLineEdit()
text.setPlaceholderText("0.00")
user_interaction_Vlayout.addWidget(text)

btn = QPushButton("Convert!")
user_interaction_Vlayout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)


# --------Inner vbox layout---------#
inner_Hlayout.addLayout(currency_dd_Vlayout)
inner_Hlayout.addLayout(user_interaction_Vlayout)

# --------Outer vbox layout---------#
outer_Vlayout.addLayout(inner_Hlayout)

output_label = QLabel("")
output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
outer_Vlayout.addWidget(output_label)

# --------Connecting the button to the method---------#
btn.clicked.connect(show_currency)

# --------Setting the layout and showing the window---------#
window.setLayout(outer_Vlayout)
window.show()
app.exec()
