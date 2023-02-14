def oxy_decrypt(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    lowkey = key.lower()
    for i in range(len(text)):
        lowercase = text[i].lower()
        if lowercase in alphabet:
            if text[i].isupper():
                idx = lowkey.index(lowercase)
                ciphertext += alphabet[idx].upper()
            elif text[i].islower():
                idx = lowkey.index(lowercase)
                ciphertext += alphabet[idx]
        else:
            ciphertext += text[i]
    return ciphertext
    
def oxy_encrypt(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    lowkey = key.lower()
    for i in range(len(text)):
        lowercase = text[i].lower()
        if lowercase in alphabet:
            if text[i].isupper():
                idx = alphabet.index(lowercase)
                ciphertext += lowkey[idx].upper()
            elif text[i].islower():
                idx = alphabet.index(lowercase)
                ciphertext += lowkey[idx]
        else:
            ciphertext += text[i]
    return ciphertext



