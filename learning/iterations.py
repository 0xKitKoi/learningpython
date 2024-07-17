from tqdm import tqdm
from time import sleep


for letters in "Hacker":
    print(letters)


friends = ["Jim", "Karen", "Kevin"]
for friends in friends:
    print(friends)

for index in range(10):
    print(index)


for index in range(len(friends)):
    print(friends[index])


for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")



for i in tqdm(range(10)):
    sleep(0.9)
