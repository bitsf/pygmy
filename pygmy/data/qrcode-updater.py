import qrcode
from base64 import b64encode
from io import BytesIO
import sqlite3

def lookForNull():
    print("Looking for null values")
    try:
        conn = sqlite3.connect("pygmy-update.db")
        cur = conn.cursor()
        cur.execute('SELECT id, qr_code, short_code FROM link WHERE qr_code IS NULL')
        table = cur.fetchall()
        for row in table:
            qr=generateQrCode(row[2])
            import pdb; pdb.set_trace()
            qr_code=str(qr)
            qr_code = qr_code.split("'")[1]
            print(qr_code)
            cur.execute("UPDATE link SET qr_code = '%s' WHERE link.id = %s" % (qr_code, row[0]))
        conn.commit()
        print("Affected rows " + str(cur.rowcount))
        conn.close()
    except:
        print("DB connection failed")

def generateQrCode(shorted):
    print("Generating the Qr-Code")
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=20,
        border=4,
    )
    qr.add_data("https://herme.li/" + shorted)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    qr_code = b64encode(img_byte_arr)
    return qr_code

print("Updating Qr-Codes")
lookForNull()