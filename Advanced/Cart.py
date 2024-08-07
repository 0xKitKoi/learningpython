from string import Template

class MyTemplate(Template):
    # takes Template class as a base class.
    delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=12, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))

    t = MyTemplate("#qty x #item = #price")

    total = 0

    print("Cart: ")
    for i in cart:
        print(t.substitute(i))
        total += i["price"]
    print("Total: " + str(total))

if __name__ == '__main__':
    Main()
