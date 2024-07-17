digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# :3 means from index position 0 all the way to index position 3, not including 3. so [0, 1, 2]
print(digits[:3])
# this prints out the list from index 5 all the way to the end, including the end.
print(digits[5:])

# Striding jumps a index position depending on the number you give it
# This will print from index position 1 all the way to 10, but skipping the second index position.
# So: [0, 2, 4, 6, 8] gets printed.
print(digits[0:10:2])

# Striding can be negative, meaning backwars strides. like so
# This will print the whole list but in reverse.
print(digits[::-1])

# indexing, slicing, and striding can be used in iterations
for i in range(len(digits)):
    print(digits[0:i])

# in every iteration, its will print the current index position with the number of iterations in the loop plus 3,
# so the output will be [0, 1, 2] [3, 4, 5] etc etc
for i in range(len(digits)):
    print(digits[i:i+3])

# Lets make the last loop better. Hard coding numbers isn't good practice.
window_size = 4
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])