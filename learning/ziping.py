# takes each elememt from the lists and pairs them together. the six will be cut off.
list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five', 'six']
zipped = list(zip(list1, list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

# for (l1, l2) in zip(list1, list2):
#    print(l1)
#    print(l2)

items = ['Apple', 'Banana', 'Orange']
counts = [2, 6, 4]
prices = [0.99, 0.25, 0.50]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = 'I Bought ' + count + ' ' + item  + 's at ' + (price) + ' cents each.'
    sentences.append(sentence)
print(sentences)