#qrcodeEx1.py
import qrcode
#generating a QR code using the make() function
qr_image=qrcode.make("Welcome to KVR Python Classes")
#saving the image file
qr_image.save("kvr-img.jpg")