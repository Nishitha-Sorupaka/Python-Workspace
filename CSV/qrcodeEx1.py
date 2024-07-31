import qrcode
#generating a QR code using the make() function
#url="https://www.google.co.in/"

url = "file:\\\C:\\Users\\nishi\\OneDrive\\Desktop\\cat.jpg"
img="file:\\\C:\\Users\\nishi\\OneDrive\\Desktop\\cat.jpg"
qr_image=qrcode.make(url)
#saving the image file
qr_image.save("shoaib-img2.jpg")