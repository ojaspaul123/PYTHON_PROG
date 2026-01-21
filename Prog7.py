# Encryption Program
import random
import string
chars = string.whitespace+string.punctuation + string.digits+string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
print(f"Chars: {chars}")
print(f"Keys: {key}")
# Encrpyted
plain_text = input("Enter a message to enterupt: ")
cipher_text=""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"Original message: {plain_text} ")
print(f"Encrypted message: {cipher_text}")  

# Decrpyed
cipher_text = input("Enter a message to enterupt: ")
plain_text=""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"Original message: {cipher_text} ")
print(f"Encrypted message: {plain_text}")