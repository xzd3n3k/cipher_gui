def tritheme_encrypt(text):
    text = text.lower()
    encrypted_text = ""

    shift = 0
    for letter in text:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            encrypted_text += letter

        else:
            a = ord(letter)
            for x in range(shift):
                if a == 122:
                    a = 96
                a += 1
            encrypted_text += chr(a)
            shift += 1

    return encrypted_text


def tritheme_decrypt(text):
    text = text.lower()
    decrypted_text = ""

    shift = 0
    for letter in text:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            decrypted_text += letter

        else:
            a = ord(letter)
            for x in range(shift):
                if a == 97:
                    a = 123
                a -= 1
            decrypted_text += chr(a)
            shift += 1

    return decrypted_text
