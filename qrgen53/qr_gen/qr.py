import segno
from segno import helpers


# import json


# TODO: receive input to determine the output type
# TODO: create functions for everything
# TODO: specify the type of code (micro or regular)
# TODO: specify the "type" of QR code (wifi, link or download)
# TODO: import regex for cleaning the google drive download link
# TODO: find a way to export the image out
# TODO: make sure background color isn't the same as dots
# TODO: integrate API docs

def simple_qrcode(name, base_link, light, dark, kind):
    qr = segno.make_qr(content=base_link, error="H", boost_error=True)
    return qr.save(name + kind, dark=dark, light=light)


def wifi_qrcode(name, ssid, password, security, light, dark, kind):
    qr = helpers.make_wifi(ssid=ssid, password=password, security=security)
    return qr.save(name + kind, dark=dark, light=light)
