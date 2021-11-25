def trifid_encrypt(text, period):  # CHECK LETTER BY LETTER EVERY POSITION
    encrypted_text = ""
    text = text.lower()
    square1 = [["e", "p", "s"], ["d", "u", "c"], ["v", "w", "y"]]
    square2 = [["m", ".", "z"], ["l", "k", "x"], ["n", "b", "t"]]
    square3 = [["f", "g", "o"], ["r", "i", "j"], ["h", "a", "q"]]
    squares = [square1, square2, square3]

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

    print(locs_to_encrypt)

trifid_encrypt("DEFEND THE EAST WALL OF THE CASTLE.", 5)

def trifid_decrypt(text):
    pass