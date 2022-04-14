dictionary = {"a": "11",
              "b": "12",
              "c": "13",
              "d": "14",
              "e": "15",
              "f": "21",
              "g": "22",
              "h": "23",
              "i": "24",
              "j": "25",
              "k": "31",
              "l": "32",
              "m": "33",
              "n": "34",
              "o": "35",
              "p": "41",
              "q": "42",
              "r": "43",
              "s": "44",
              "t": "45",
              "u": "51",
              "v": "52",
              "w": "w",
              "x": "53",
              "y": "54",
              "z": "55"}


def polybius_encrypt(text):
    encrypted_text = ""

    for x in range(len(text)):
        if text[x] not in "abcdefghijklmnopqrstuvwxyz ":
            return "Used incorrect characters, try again!"
        else:
            if text[x] == " ":
                encrypted_text += text[x]
            else:
                encrypted_text += dictionary[text[x]]

    return encrypted_text


def polybius_decrypt(text):
    decrypted_text = ""
    key_list = list(dictionary.keys())
    value_list = list(dictionary.values())
    a = 0
    b = ""

    for character in text:

        if character not in "0123456789w ":
            return "Used incorrect characters, try again!"

        else:
            try:
                if character == " " or character == "w":
                    decrypted_text += character
                else:
                    b += character
                    a += 1

                    if ((a % 2) == 0) & (a != 0):
                        decrypted_text += key_list[value_list.index(b)]
                        b = ""
            except ValueError:
                return "Program nebyl schopen text desifrovat, pravdepodobne je text sifrovan v jine sifre nebo je to nahodne uskupeni cislic"

    return decrypted_text
