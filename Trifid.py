def trifid_encrypt(text):
    encrypted_text = ""
    square1 = [["e", "p", "s"], ["d", "u", "c"], ["v", "m", "y"]]
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

    print(locations)

    upper = []
    middle = []
    lower = []
    for x in range(len(locations)):
        upper.append(locations[x][0])
        middle.append(locations[x][1])
        lower.append(locations[x][2])

    print(upper)
    print(middle)
    print(lower)


trifid_encrypt("hello")
