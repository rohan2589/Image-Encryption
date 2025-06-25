from tkinter import filedialog, Tk, Button, Label
from PIL import Image
import os

KEY = 123  # Simple numeric key

def encrypt_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + KEY) % 256, (g + KEY) % 256, (b + KEY) % 256)

    encrypted_path = "encrypted_" + os.path.basename(image_path)
    img.save(encrypted_path)
    return encrypted_path

def decrypt_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - KEY) % 256, (g - KEY) % 256, (b - KEY) % 256)

    decrypted_path = "decrypted_" + os.path.basename(image_path)
    img.save(decrypted_path)
    return decrypted_path

# GUI Application
def choose_and_encrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        output = encrypt_image(file_path)
        status_label.config(text=f"Image encrypted: {output}")

def choose_and_decrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        output = decrypt_image(file_path)
        status_label.config(text=f"Image decrypted: {output}")

# Tkinter setup
window = Tk()
window.title("Image Encryptor Tool")
window.geometry("300x200")

Label(window, text="Simple Image Encryption Tool", font=("Arial", 12)).pack(pady=10)

Button(window, text="Encrypt Image", command=choose_and_encrypt).pack(pady=10)
Button(window, text="Decrypt Image", command=choose_and_decrypt).pack(pady=10)

status_label = Label(window, text="", fg="green")
status_label.pack(pady=10)

window.mainloop()
