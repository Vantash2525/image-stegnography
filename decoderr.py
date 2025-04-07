from PIL import Image
import os

# Load the image from the same directory
input_path = os.path.join(os.path.dirname(__file__), "output.png")

try:
    img = Image.open(input_path)
except FileNotFoundError:
    print("Error: 'output.png' not found in the current directory.")
    exit()

img = img.convert("RGBA")
pixels = img.load()

# Get password and validate length
while True:
    password = input("Enter the password used for encoding:\n")
    if len(password) >= 8:
        break
    else:
        print("The password must be at least 8 characters long.")

# Extract the message using the password
hide = [ord(char) for char in password]        
decoded_message = ""

for i in hide:
    for j in hide[1:]:
        r, g, b, a = pixels[i, j]
        decoded_message += chr(b)

print("Decoded message:", decoded_message)
