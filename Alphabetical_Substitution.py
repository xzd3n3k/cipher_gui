def alphabetical_substitution_encrypt(text, alphabet="abcdefghijklmnopqrstuvwxyz",
                                      cipher_alphabet="zyxwvutsrqponmlkjihgfedcba"):
    encrypted_text = ""

    if alphabet == "":
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    if cipher_alphabet == "":
        cipher_alphabet = "zyxwvutsrqponmlkjihgfedcba"

    for letter in text:
        if letter in alphabet:
            encrypted_text += cipher_alphabet[alphabet.index(letter)]
        else:
            encrypted_text += letter

    return encrypted_text


def alphabetical_substitution_decrypt(text, alphabet="abcdefghijklmnopqrstuvwxyz",
                                      cipher_alphabet="zyxwvutsrqponmlkjihgfedcba"):
    decrypted_text = ""

    if alphabet == "":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    else:
        control_alp = "abcdefghijklmnopqrstuvwxyz"
        for letter in control_alp:
            if alphabet.count(letter) != 1:
                return "Wrong alphabet, some characters are special, missing or used multiple times!"

    if cipher_alphabet == "":
        cipher_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    else:
        control_alp = "zyxwvutsrqponmlkjihgfedcba"
        for letter in control_alp:
            if cipher_alphabet.count(letter) != 1:
                return "Wrong alphabet, some characters are special, missing or used multiple times!"

    for letter in text:
        if letter in alphabet:
            decrypted_text += alphabet[cipher_alphabet.index(letter)]
        else:
            decrypted_text += letter

    return decrypted_text
