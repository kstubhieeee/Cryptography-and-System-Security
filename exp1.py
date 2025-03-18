def encrypt(text, shift):
    encrypted_text = ""
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in text:
        if char.islower():
            index = lower_alphabet.index(char)
            new_index = (index + shift) % 26
            encrypted_text += lower_alphabet[new_index]
        elif char.isupper():
            index = upper_alphabet.index(char)
            new_index = (index + shift) % 26
            encrypted_text += upper_alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in text:
        if char.islower():
            index = lower_alphabet.index(char)
            new_index = (index - shift) % 26
            decrypted_text += lower_alphabet[new_index]
        elif char.isupper():
            index = upper_alphabet.index(char)
            new_index = (index - shift) % 26
            decrypted_text += upper_alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text

plain_text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))

cipher_text = encrypt(plain_text, shift)
decrypted_text = decrypt(cipher_text, shift)

print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)