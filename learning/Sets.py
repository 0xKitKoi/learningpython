# Sets are unordered Unique sequences of elements {}
# unordered {cannot be iterated into. %random%} Unique {cannot have duplicates}

set1 = {'blueberry', 'raspberry'}
set1.add('strawberry')
# this wont be added because its a duplicate
set1.add('blueberry')
# run this multiple times to see the random order.
print(set1)

# takes list of numbers, turns it into a set, prints it, turns it back into a list, and prints it.
list_of_numbers = [1, 1, 2, 3, 3, 4, 5, 6, 6, 9, 7, 8]
no_duplicate_set = set(list_of_numbers)
print(no_duplicate_set)
no_duplicate_list = list(no_duplicate_set)
print(no_duplicate_list)
# notice how there is no duplicate numbers printed out. That is why we would do such a thing.

#
library1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
library2 = {'Harry Potter', 'Romeo and Juliet'}
# Prints all the books in the libraries
# at_both_libraries = library1.union(library2)
# Prints the intersecting books like a ven diagram
# at_both_libraries = library1.intersection(library2)
# print(at_both_libraries)
# Prints the diffrence between the two libraries. (books not in the other library
# diff = library1.difference(library2)
