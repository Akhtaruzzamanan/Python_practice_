reapit = True

while reapit:
    number = int(input("Please insert a number for square or qube: "))

    options = input("What you want? type 's' for square or 'q' for qube: ")
    if options == 's':
        square = number * number
        print(square)
    elif options == 'q':
        qube = number * number * number
        print(qube)
    else:
        print("Please provide a valid options")
        break
    want_repeat = input("want reapeat type 'y' or exit 'e': ")
    if want_repeat == 'y':
        reapit
    elif want_repeat == 'e':
        reapit = False
    else:
        print("Please provide a valid options")
        break 