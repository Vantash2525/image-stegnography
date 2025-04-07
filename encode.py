from PIL import Image
import os

def eb(num):
    return format(num, '08b')

# Load the image from the same directory
input_path = os.path.join(os.path.dirname(__file__), "input.png")

try:
    imag = Image.open(input_path)
except FileNotFoundError:
    print("Error: 'input.png' not found in the current directory.")
    exit()

imag = imag.convert("RGBA")
pixels = imag.load()

message = input("Enter the message to be hidden:\n")

# Ensure password is at least 8 characters
while True:
    password = input("Enter the password:\n")
    if len(password) >= 8:
        break
    else:
        print("The password must be at least 8 characters. Try again.")

# Convert password to ASCII values
hide = [ord(char) for char in password]
count = 0

# Encode the message into the image
for i in hide:
    for j in hide[1:]:
        if count < len(message):
            r, g, b, a = pixels[i, j]
            pixels[i, j] = r, g, ord(message[count]), a
            count += 1
        else:
            break

# Save the image as output.png in the same directory
output_path = os.path.join(os.path.dirname(__file__), "output.png")
imag.save(output_path)
imag.show()
