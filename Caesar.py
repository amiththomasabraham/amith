text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for char in text:
    if char.isalpha():
        encrypted += chr((ord(char) + shift - 97) % 26 + 97)
    else:
        encrypted += char

print("Encrypted:", encrypted)
