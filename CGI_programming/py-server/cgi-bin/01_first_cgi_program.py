# https://www.tutorialspoint.com/python/python_cgi_programming.htm

"""
The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged between
the web server and a custom script. The CGI specs are currently maintained by the NCSA.
"""

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! This is my first CGI program</h2>')
print('</body>')
print('</html>')
