# next: file renamer using a template?

from string import Template

class MyTemplate(Template):
	delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=12, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))
    t = MyTemplate("#qty x #item = #price") 

# t = Template("$qty x $item = $price")  is replaced because we set our own delimiter.
# NoPlaceHolder match error means there wasnt a value given for the place holder. Bad placeholder means the placeholder started with an invalid character, usually a number.

    total = 0
    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total: " + str(total))

if __name__ == '__main__':
    Main()
