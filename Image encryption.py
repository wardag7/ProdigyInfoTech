from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size

    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)

    encrypted_img = Image.new(img.mode, (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size

    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)

    decrypted_img = Image.new(img.mode, (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")

# Example usage with the provided image path:
image_path = r"C:\Users\Wajahat Khan\Desktop\ProdigyInfoTech\image.jpeg"
encryption_key = 50

# Encrypt the image
encrypt_image(image_path, encryption_key)

# Decrypt the image
decrypt_image("encrypted_image.png", encryption_key)
