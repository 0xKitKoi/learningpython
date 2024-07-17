import sys

this = sys.argv
this.pop(0)

for i in range(1, len(this)):
    this[i] = int(this[i])

for i in this:
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        print ('fizzbuzz')
    elif int(i) % 3 == 0:
        print ('fizz')
    elif int(i) % 5 == 0:
        print ('buzz')
    else:
        print (str(i))



#for index, arg in enumerate(this, start=1):

#for i, f in enumerate(this, start=0):
#    user_input = this
#    out = ''
#    if user_input % 3 == 0:
#        out = out + 'fizz'
#    if user_input % 5 == 0:
#        out = out + 'buzz'
#    else:
#        print(user_input)
#    if out == '':
#        out = user_input
   ## print(out)
