def a1z26_encrypt(text, separator=" ", key="abcdefghijklmnopqrstuvwxyz"):
    if key == "":
        key = "abcdefghijklmnopqrstuvwxyz"
    if separator == "":
        separator = " "

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
        separator_limit = 1
        for letter in text:
            if letter not in key:
                return "Used incorrect characters, try again!"
            position = key.find(letter)
            encrypted_text += str(position+1)
            if separator_limit < len(text):
                encrypted_text += separator
                separator_limit += 1

    else:
        encrypted_text = "Incorrect alphabet: some characters are missing or used multiple times!"

    return encrypted_text


def a1z26_decrypt(text, separator=" ", key="abcdefghijklmnopqrstuvwxyz"):
    if key == "":
        key = "abcdefghijklmnopqrstuvwxyz"
    if separator == "":
        separator = " "

    decrypted_text = ""
    keyy = "abcdefghijklmnopqrstuvwxyz"
    key_verifier_text = ""
    key_verifier = 0
    text = text.split(separator)

    for letter in key:
        if letter in key_verifier_text:
            pass
        elif letter in keyy:
            key_verifier_text += letter
            key_verifier += 1

    if key_verifier == len(keyy):
        for num in text:
            try:
                if (int(num) < 1) or (int(num) > 26):
                    return "Numbers out of range, try again!"
            except ValueError:
                return "Used incorrect characters, only numbers supported, try again!"
            num = int(num)
            decrypted_text += key[num-1]

    return decrypted_text
