import qrcode

# Create a QR code
code = qrcode.make("https://google.com")
code.save("Section 28_miscellaneous/files/qr_code.png")
