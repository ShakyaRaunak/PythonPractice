# https://www.tutorialspoint.com/python/python_cgi_programming.htm

import os

print("Content-type: text/html\r\n\r\n")
print("<font size=+1>Environment</font><r'\'br>")

for param in os.environ.keys():
    print("<b>%20s</b>: %s</br>" % (param, os.environ[param]))
