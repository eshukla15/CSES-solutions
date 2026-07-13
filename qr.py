import qrcode

# Data you want to encode
data = "https://supermom-unselect-drone.ngrok-free.dev/api-explorer"


# Generate the QR code
img = qrcode.make(data)

# Save as PNG
img.save("my_qr_code.png")