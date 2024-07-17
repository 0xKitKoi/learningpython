import random

print("\nYou're here becuase you can't decide. You're too reliant on me.\n")
print("You're about to leave your decision up to random chance.\n")
print("You should've immediatly thought that this is a load of horseshit.\n")
print("Think for yourself. Stop being a sheep. Grow a pair of balls.\n")
print("....sigh, fine.\n")
choices = []
numChoices = int(input("\nHow many options are there? --> "))

def main():
    for i in range(numChoices):
        choices.append(input("\nOption " + str(i) + " --> "))
    decision = random.randrange(0, numChoices)
    print("\nOption " + str(decision) + " was chosen. " + choices[decision] + ". Stay Focused.\n")

if __name__ == '__main__':
    main()
