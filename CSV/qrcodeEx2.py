import qrcode
from PIL import Image

def generate_qr_code_with_image(image_path, file_name='qr_code_with_image.png'):
    img = Image.open(image_path).resize((200, 200))
    img_byte_arr = img.tobytes()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10, border=4)
    qr.add_data(img_byte_arr)
    qr.make(fit=True).make_image(fill_color="black", back_color="white").save(file_name)

    return file_name

def read_qr_code_with_image(file_name):
    img = Image.open(file_name)
    Image.frombytes('RGB', (200, 200), qrcode.image.ImageReader().read(img)[0].data).show()

if __name__ == "__main__":
    qr_code_image = generate_qr_code_with_image('your_image.jpg')
    print("QR Code with image generated:", qr_code_image)
    Image.open(qr_code_image).show()

    input("Scan the QR code and press Enter to display the image...")
    read_qr_code_with_image(qr_code_image)