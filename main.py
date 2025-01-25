import qrcode

# Read the program as a string
with open("ascii_art.py", "r") as f:
    program = f.read()

# Create the QR code
qr = qrcode.QRCode(
    version=None,  # Automatically adjusts size
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(program)
qr.make(fit=True)

# Save the QR code as an image
img = qr.make_image(fill="black", back_color="white")
img.save("ascii_art_qr.png")
print("QR code saved as 'ascii_art_qr.png'")
