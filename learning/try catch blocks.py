try:

    number = int(input("Enter A Number: "))
    print(number)
except ValueError as err:
    print("Invalid Input")
    print(err)