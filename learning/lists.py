# lists

l = [1, 2, 3]
# Variable data type all fit in lists
list2 = [1, "string", 4.3, True, [1, 2, 3]]
names = ["joe", "james", "boi"]
names.append("boio")
#print(list2[4])
print(names)
# Appends niggy to the first index position on the list
names.insert(0, "niggy")
print(names)
# Removing names from the list
names.remove("joe")
print(names)

#Reverse the list
names.reverse()
print(names)

#Sort the list
numbers = [6, 3, 8, 1, 0, 12]
print(numbers)
numbers.sort()
print(numbers)

#For Loop with list

for number in numbers:
    print(number)

names5 = ['Jennifer', 'Susan', 'Jane', 'Sophie']
l = []
for person in names5:
    l.append(person)
    print(l)
print([person for person in names5])

l = []
for person in names5:
    l.append(person + ' left.')
    print(l)

print([person + ' left.' for person in names5])

movies_and_ratings = {"Interstellar": 2, "Dark Knight": 8, '50 Shades': 3, "Project Almenact": 9}
l = []
for movie in movies_and_ratings:
    if movies_and_ratings[movie] > 6:
        l.append(movie)
print(l)

print( [movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6] )

################################## Slicing

insanity = ['The', 'Scuzzy', 'Will', 'Study']
print(insanity)
# Slicing from 1 to 3 means we're asking for 'Scuzzy' and 'Will'.
print(insanity[1:3])
