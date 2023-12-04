import qrcode
from qrcode.image.svg import SvgImage
from base64 import b64encode
from io import BytesIO
import sqlite3

def lookForNull():
    print('Looking for null values')
    try:
        conn = sqlite3.connect('pygmy.db')
        cur = conn.cursor()
        cur.execute('SELECT id, qr_code, short_code FROM link')
        table = cur.fetchall()
        for row in table:
            qr_code = generateQrCode(row[2])
            print("Generated code, b64: %s" % qr_code)
            cur.execute("UPDATE link SET qr_code = '%s' WHERE link.id = %s" % (qr_code, row[0]))
        conn.commit()
        print('Affected rows ' + str(len(table)))
        conn.close()
    except:
        print('DB connection failed')


def generateQrCode(shorted):
    print('Generating the Qr-Code')
    qr = qrcode.QRCode(
            version=None,
            box_size=20,
            border=1,
            image_factory=SvgImage
        )
    qr.add_data(shorted)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black")

    # Convert bytes to base64 string
    qr_string = str(b64encode(img.to_string())).split("'")[1]

    return qr_string

print('Updating Qr-Codes')
lookForNull()