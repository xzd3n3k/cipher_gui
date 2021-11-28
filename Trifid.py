def trifid_encrypt(text, period):
    encrypted_text = ""
    text = text.lower()
    key = "abcdefghijklmno.pqrstuvwxyz"
    key = key.lower()
    sq = [[], [], []]
    pos = 0
    for x in range(3):
        for y in range(3):
            sq[x].append([])
            for z in range(3):
                sq[x][y].append(key[pos])
                pos += 1
    print(sq)
    square1 = [["e", "p", "s"], ["d", "u", "c"], ["v", "w", "y"]]
    square2 = [["m", ".", "z"], ["l", "k", "x"], ["n", "b", "t"]]
    square3 = [["f", "g", "o"], ["r", "i", "j"], ["h", "a", "q"]]
    squares = [square1, square2, square3]
    print(squares)

    locations = []
    for letter in text:
        location_of_letter = ""
        squareNumber = 0

        for square in squares:
            squareNumber += 1
            listIndex = 1

            for seznam in square:

                if letter in seznam:
                    location_of_letter += str(squareNumber)
                    location_of_letter += str(listIndex)
                    location_of_letter += str(seznam.index(letter)+1)
                    locations.append(location_of_letter)

                else:
                    pass
                listIndex += 1

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


def trifid_decrypt(text):
    decrypted_text = ""
    letters = []

    for letter in text:
        if letter != " ":
            letters.append(letter)

    print(letters)

trifid_decrypt("qjgdh jqurb mbejp s")
trifid_encrypt("ahoj", 5)