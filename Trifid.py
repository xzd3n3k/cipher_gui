def trifid_encrypt(text):
    encrypted_text = ""
    square1 = [["e", "p", "s"], ["d", "u", "c"], ["v", "m", "y"]]
    square2 = [["m", ".", "z"], ["l", "k", "x"], ["n", "b", "t"]]
    square3 = [["f", "g", "o"], ["r", "i", "j"], ["h", "a", "q"]]
    squares = [square1, square2, square3]

    locations = []
    for letter in text:
        location_of_letter = ""

        for square in squares:
            temp = 0

            for listt in square:

                if letter in listt:
                    location_of_letter += str(temp)
                    location_of_letter += str(listt.index(letter))
                    locations.append(location_of_letter)
                temp += 1

    print(locations)


trifid_encrypt("hello")
