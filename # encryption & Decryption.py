# encryption & Decryption

import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#print(f"chars: {chars}")
#print(f"key: {key}")

#Encrypt

plain_text = input("Enter TExt To Encrypt: ")
cipher_text = ""

for letters in plain_text:
    index = chars.index(letters)
    cipher_text += key[index]
print(f"Original Text: {plain_text}")
print(f"Cipher Text: {cipher_text}")


#Decrypt

cipher_text = input("Enter Text To Decrypt: ")
plain_text = ""

for letters in cipher_text:
    index = key.index(letters)
    plain_text += chars[index]
print(f"Cipher Text: {cipher_text}")
print(f"Original Text: {plain_text}")


