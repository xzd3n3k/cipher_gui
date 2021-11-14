def tritheme_encrypt(text):
    text = text.lower()
    encrypted_text = ""

    letter_count = 0
    for letter in text:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            pass

        else:
            letter_count += 1

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
