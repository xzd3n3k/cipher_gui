def trifid_encrypt(text, period, key="epsducvwym.zlkxnbtfgorijhaq"):
    if key == "":
        key = "epsducvwym.zlkxnbtfgorijhaq"

    encrypted_text = ""
    text = text.lower()
    key = key.lower()
    squares = [[], [], []]
    pos = 0
    for x in range(3):
        for y in range(3):
            squares[x].append([])
            for z in range(3):
                squares[x][y].append(key[pos])
                pos += 1

    locations = []
    for letter in text:
        location_of_letter = ""
        square_number = 0

        for square in squares:
            square_number += 1
            list_index = 1

            for seznam in square:

                if letter in seznam:
                    location_of_letter += str(square_number)
                    location_of_letter += str(list_index)
                    location_of_letter += str(seznam.index(letter)+1)
                    locations.append(location_of_letter)

                else:
                    pass
                list_index += 1

    upper = []
    middle = []
    lower = []
    for x in range(len(locations)):
        upper.append(locations[x][0])
        middle.append(locations[x][1])
        lower.append(locations[x][2])

    lines = [upper, middle, lower]

    i = len(upper) // period
    j = len(upper) % period
    encrypted_locations = []

    stop = 0
    start = 0
    for o in range(i):

        stop += period
        for p in range(3):

            for q in range(start, stop):
                encrypted_locations.append(lines[p][q])

        start += period

    for o in range(3):
        position = (i*period)
        for p in range(j):
            encrypted_locations.append(lines[o][position])
            position += 1

    pair_count = int(len(encrypted_locations)/3)
    temp = 0
    locs_to_encrypt = []
    for i in range(pair_count):
        locs = ""
        for j in range(3):
            locs += str(encrypted_locations[temp])
            temp += 1
        locs_to_encrypt.append(locs)

    letters = []
    for element in locs_to_encrypt:
        letters.append(squares[int(element[0])-1][int(element[1])-1][int(element[2])-1])

    x = 0
    for lttr in letters:
        if (x % period == 0) and (x != 0):
            encrypted_text += " "

        encrypted_text += lttr
        x += 1

    return encrypted_text


def trifid_decrypt(text, key="epsducvwym.zlkxnbtfgorijhaq"):
    if key == "":
        key = "epsducvwym.zlkxnbtfgorijhaq"

    key = key.lower()
    text = text.lower()
    decrypted_text = ""
    letters = []
    period = 0
    lines = [[], [], []]
    squares = [[], [], []]
    pos = 0
    for x in range(3):
        for y in range(3):
            squares[x].append([])
            for z in range(3):
                squares[x][y].append(key[pos])
                pos += 1

    for letter in text:
        if letter != " ":
            period += 1
        else:
            break

    for letter in text:
        if letter != " ":
            letters.append(letter)

    locations = []
    for letter in text:
        location_of_letter = ""
        square_number = 0

        for square in squares:
            square_number += 1
            list_index = 1

            for seznam in square:

                if letter in seznam:
                    location_of_letter += str(square_number)
                    location_of_letter += str(list_index)
                    location_of_letter += str(seznam.index(letter) + 1)
                    locations.append(location_of_letter)

                else:
                    pass
                list_index += 1

    locs_to_lineup = []
    for prvek in locations:
        for x in range(3):
            locs_to_lineup.append(prvek[x])

    line_count = int(len(locs_to_lineup)/3)

    i = len(locs_to_lineup) // (period*3)
    j = len(locs_to_lineup) % (period*3)

    sqrs = []
    for x in range(i):
        sqrs.append([])

    if j > 0:
        sqrs.append([])

    psition = 0
    for x in range(i):
        for y in range(period*3):
            sqrs[x].append(locs_to_lineup[psition])
            psition += 1

    for x in range(j):
        sqrs[len(sqrs)-1].append(locs_to_lineup[psition])
        psition += 1
