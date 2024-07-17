def getInterger(prompt):
    result = int(input(prompt))
    return result
def Main():
    print("Started")
    # calls the getInterger function and stores it into the output variable
    output = getInterger("Please enter a number: -> ")
    # calles the fuction again. with this method you can use the same function for diffrent tasks.
    output2 = getInterger("Enter another interger. -> ")
    print(output)
if __name__ == "__main__":
    Main()