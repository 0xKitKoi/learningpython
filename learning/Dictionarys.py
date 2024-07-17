# Dictionary has bananas with the value of 5, and oranges with the value of 3, and finally printing the index of bananas.
groceries = {'bananas': 5, 'oranges': 3}

print(groceries.get('bananas'))
print(groceries.get('hello'))

contacts = {
    'Joe': 1234567,
    'Jane': 9876543
}

print(contacts['Joe'])

contacts2 = {
    'Joe': ['123-4557', 'email@email2.com']
    'Jane': ['987-6543', 'email2@email2.com']
}
print(contacts2['Jane'])

contacts3 = {
    'jacob': {'phone': '123-4567', 'email': 'email@emaill3.com'},
    'david': {'phone': '987-6543', 'email': 'email@emaill3.com'}
}
print(contacts3['jacob']

sentence = "I like the name shawn because the name shawn is the best"
word_counts = {
    'I': 1,
    'like': 1,
    'the': 3
}
print(word_counts)
word_counts['shawn'] = 2
print(word_counts)

print(word_counts.pop())
print(word_counts.popitem())
print(word_counts)