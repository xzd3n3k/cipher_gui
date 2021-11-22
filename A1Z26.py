def a1z26_encrypt(text, separator=" ", key="abcdefghijklmnopqrstuvwxyz"):
    encrypted_text = ""
    keyy = "abcdefghijklmnopqrstuvwxyz"
    key_verifier_text = ""
    key_verifier = 0
    text = text.replace(" ", "")

    for letter in key:
        if letter in key_verifier_text:
            pass
        elif letter in keyy:
            key_verifier_text += letter
            key_verifier += 1

    if key_verifier == len(keyy):
        for letter in text:
            position = key.find(letter)
            encrypted_text += str(position+1)
            encrypted_text += separator

    else:
        encrypted_text = "Incorrect alphabet: some characters are missing or used multiple times!"

    return encrypted_text


def a1z26_decrypt(text, separator=" ", key="abcdefghijklmnopqrstuvwxyz"):
    decrypted_text = ""
    keyy = "abcdefghijklmnopqrstuvwxyz"
    key_verifier_text = ""
    key_verifier = 0
    text = text.split(separator)
    text.pop()

    for letter in key:
        if letter in key_verifier_text:
            pass
        elif letter in keyy:
            key_verifier_text += letter
            key_verifier += 1

    if key_verifier == len(keyy):
        for num in text:
            num = int(num)
            decrypted_text += key[num-1]

    return decrypted_text
