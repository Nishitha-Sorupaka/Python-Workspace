#qrcodeEx2.py
import qrcode
#generating a QR code using the make() function
url="https://www.youtube.com/"
qr_image=qrcode.make(url)
#saving the image file
qr_image.save("url.jpg")