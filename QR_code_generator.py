# install libraries 
#create a function
# save the qr code as an image#
# run the function

def generate_qrcode(data):
   
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Controls how many pixels each “box” of the QR code is
        border=4,  # The thickness of the border (minimum is 4)
    )

    qr.add_data(data)
    qr.make(fit=True)  
    img = qr.make_image(fill_color="red", back_color="blue")
    img.save("qr_code_image.png")

url = input("Enter the URL: ")

generate_qrcode(url)
