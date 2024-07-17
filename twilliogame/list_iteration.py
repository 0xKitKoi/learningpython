import sys

#order_of_succession = ['Isabelle', 'Grace', 'Charlotte', 'LeBron', 'Steve']
order_of_succession = sys.argv
order_of_succession.pop(0)

for index, leader in enumerate(order_of_succession, start=1):
    this = f"{index}. {leader}"
    print(this)
