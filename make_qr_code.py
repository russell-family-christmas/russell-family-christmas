# https://pypi.org/project/qrcode/
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data("https://russell-family-christmas.github.io/russell-family-christmas/")
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white")
img.save("site-qr-code.png")
