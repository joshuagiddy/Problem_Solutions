def number_check():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                exit("Invalid input")
            elif number > 512:
                print("Beep")
            else:
                print("Boop")
        except ValueError:
            print("Invalid input")


number_check()