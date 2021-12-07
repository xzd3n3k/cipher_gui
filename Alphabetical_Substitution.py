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

    if cipher_alphabet == "":
        cipher_alphabet = "zyxwvutsrqponmlkjihgfedcba"

    for letter in text:
        if letter in alphabet:
            decrypted_text += alphabet[cipher_alphabet.index(letter)]
        else:
            decrypted_text += letter

    return decrypted_text
