#!/usr/bin/python3
import cgi

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1>Hello Program</h1>")

form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1> Hello " + name + "!</h1><br />")
if form.getvalue("happy"):
    print("<p> woot </p>")
if form.getvalue("sad"):
    print("<p> it do be like that tho </p>")

print("<form method='post' action='test.py'>")
print("<p>Name: <input type='text' name='name'/></p>")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='submit' value='Submit' />")
print("</form>")
print("</body></html>")
