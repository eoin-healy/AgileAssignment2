def helworld():
    while True:
        num=int(input("Enter a number: "))
        if num % 2 == 0:
            cal = num // 2
            print("Your number is a divided of 2")
        else:
            print("This is not good!")

helworld()
