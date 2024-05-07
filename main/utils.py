import os

import qrcode

PHONE = os.environ.get("MY_PHONE", "+79234567898")


def generate_qr(href):
    """Функция генерации QRcode для переходов в мессенжеры."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(href + PHONE)
    qr.make(fit=True)

    directory = "main/static/assets/img"
    if not os.path.exists(directory):
        os.makedirs(directory)

    image_path = os.path.join(directory, "qr.png")
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(image_path)
