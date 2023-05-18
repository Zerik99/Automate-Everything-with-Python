from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
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
    """a method to capitalize the input text and display it in the output label"""

    input_text: str = text.text()
    conversion_rate: float = get_currency("usd", "eur")
    converted_amount: float = round(float(input_text) * conversion_rate, 2)
    output_label.setText(str(converted_amount))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert!")
layout.addWidget(btn)

output_label = QLabel("")
layout.addWidget(output_label)

btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()
