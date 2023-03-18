import qrcode

qr = qrcode.QRCode(version=7,
                   error_correction=qrcode.ERROR_CORRECT_L,
                   box_size=12,
                   border=2)

pdfUrl = "https://qardlesspdfs.blob.core.windows.net/pdfs/FLCB214-7420.pdf"
qr.add_data(pdfUrl)
qr.make(fit=True)

img = qr.make_image(fill='Black', back_color='White')
img.save("qrCode.png")



