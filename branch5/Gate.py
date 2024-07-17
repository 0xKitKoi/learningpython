#!/usr/bin/python3
import cgi

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<pre>
         ______________________
        < What's The Password? >
         ----------------------
                 \   ^__^
                  \  (oo)\_______
                     (__)\       )\/\\
                         ||----w |
                         ||     ||
        </pre>")
form = cgi.FieldStorage()
if form.getvalue('password'):
    password = form.getvalue('password')
    if var in ('Scuzzy', 'scuzzy'):
        print("<button class='button' onclick=\"window.location.href=S3CR37.html';\">Welcome.</button>")
    else:
        print("<p>int 0x80</p>")
print("<form method='post' action='Gate.py>'")
print("<input type='password' name='password' />")
print("<input type='submit' value'Submit' />")
print("</form>")
print("</body></html>")
