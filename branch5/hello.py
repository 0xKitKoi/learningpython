#!/usr/bin/python3
print("Content-type:text/httml\r\n\r\n")
print("<html><body>")
print("<h1>It Works!</h1>")
for i in range(5):
    print("<h2> Hello, World! " + str(i) + "</h2>")
print("</body></html>")