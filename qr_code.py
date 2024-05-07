import pyqrcode
import png
from pyqrcode import QRCode
s='www.facebook.com'
url=pyqrcode.create(s)
url.svg('myqr.svg',sacle=8)
url.png('myqr.png',scale=6)

