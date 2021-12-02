import re
import os


def caesar_encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""

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

    return encrypted_text


def caesar_decrypt(text, shift=0):
    if os.path.exists("txt_files/dictionary_extension.txt"):
        os.remove("txt_files/dictionary_extension.txt")

    else:
        pass

    text = text.lower()

    with open("txt_files/ceska_slova_databaze.txt", mode="r", encoding="utf-8") as filedict:
        dictionary = filedict.read()
        dictionary = dictionary.split()
        match = 0
        words_from_text = "ahoj"
        limit = 0
        while match < len(words_from_text) // 2:

            if limit == 1000:
                decrypted_text = "Program s jistotou nemohl desifrovat text, prosim pouzijte Decrypt with all options"
                break
            limit += 1

            match = 0
            match_words = []
            shift += 1
            decrypted_text = ""

            for letter in text:

                if letter not in "abcdefghijklmnopqrstuvwxyz":
                    decrypted_text += letter

                else:
                    a = ord(letter)

                    for x in range(shift):

                        if a == 122:
                            a = 96
                        a += 1

                    decrypted_text += chr(a)

            words_from_text = re.findall(r'\w+', decrypted_text)

            for word in words_from_text:

                a = dictionary.count(word)

                if a > 0:
                    match += 1
                    match_words.append(word)

    extension = []

    for word in words_from_text:
        a = dictionary.count(word)

        if a == 0 and len(word) > 2:
            extension.append(word)

    if len(extension) > 0:
        with open("txt_files/dictionary_extension.txt", mode="w", encoding="utf-8") as file2:
            for word in extension:
                file2.write(word)
                file2.write("\n")

    return decrypted_text


def caesar_manual_decrypt(text, shift=0):
    text = text.lower()
    dec_opts = []

    for y in range(25):
        shift += 1
        decrypted_text = ""

        for letter in text:

            if letter not in "abcdefghijklmnopqrstuvwxyz":
                decrypted_text += letter

            else:
                a = ord(letter)

                for x in range(shift):

                    if a == 122:
                        a = 96
                    a += 1

                decrypted_text += chr(a)
        dec_opts.append(str(shift) + ": " + decrypted_text)

    return dec_opts
