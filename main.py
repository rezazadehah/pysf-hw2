# Ceasar Cipher Encode part "1"

def cipher(char, key):
    char = (ord(char) + key - 65) % 26 + 65
    return chr(char)


def encipher(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        ciphertext += cipher(char, key)
    return ciphertext
    
#test
print (encipher("Hello", 3))
# Ceasar Cipher Decode part "2"

# Pigpen Cipher Encode part "3"
# Pigpen Cipher Decode part "4"
# Choose The Opration "5"