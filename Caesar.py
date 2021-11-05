def caesar_encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""

    for word in text:
        if word not in "abcdefghijklmnopqrstuvwxyz":
            encrypted_text += word
        else:
            a = ord(word)
            for x in range(shift):
                if a == 122:
                    a = 96
                a += 1
            encrypted_text += chr(a)
    print("##############HOTOVO##############")
    print("Sifrace uspesne dokoncena!")
    print("Sila sifrovani je:", shift)
    print("Zasifrovany text:", encrypted_text)
    print("##################################")

    """if save == "a":
        file_name = input("Jak se tento textovy soubor ma jmenovat? (bez diakritiky, bez mezer, bez specialnich "
                          "znaku): ")
        file_name += ".txt"
        print("\n")

        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(encrypted_text)"""

    return encrypted_text


def caesar_decrypt():
    return "ahoj"
