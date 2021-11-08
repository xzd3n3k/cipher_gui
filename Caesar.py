import re
import os


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

    return encrypted_text


def caesar_decrypt(text, shift=0):
    if os.path.exists("txt_files/ceska_slova_rozsireni.txt"):
        os.remove("txt_files/ceska_slova_rozsireni.txt")
    else:
        pass

    text = text.lower()

    with open("txt_files/ceska_slova_databaze.txt", mode="r", encoding="utf-8") as filedict:
        dictionary = filedict.read()
        dictionary = dictionary.split()

        shoda = 0
        shodna_slova = []
        shift += 1
        desifrovany_text = ""

        for pismeno in text:

            if pismeno not in "abcdefghijklmnopqrstuvwxyz":
                desifrovany_text += pismeno

            else:
                a = ord(pismeno)
                temp = 122

                for x in range(shift):

                    if a == temp:
                        a = 96
                    a += 1
                desifrovany_text += chr(a)

        slova_z_textu = re.findall(r'\w+', desifrovany_text)

        for slovo in slova_z_textu:

            a = dictionary.count(slovo)

            if a > 0:
                shoda += 1
                shodna_slova.append(slovo)

                if shoda > len(slova_z_textu) * 1 / 4:
                    print("Shoda se slovem/y", end=": ")

                    if len(shodna_slova) > 1:

                        for x in range(len(shodna_slova)):
                            if x == len(shodna_slova) - 1:
                                print(shodna_slova[x], end=".")
                            else:
                                print(shodna_slova[x], end=", ")

                    else:
                        for shodne_slovo in shodna_slova:
                            print(shodne_slovo, end=".")

                    print("\n")
                    print("Desifrovany text:", desifrovany_text)
                    print("\n")
