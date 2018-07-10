# https://www.tutorialspoint.com/python/python_cgi_programming.htm
# Simple URL Example:POST Method

# http://localhost:8000/cgi-bin/03_hello_get.py?first_name=Raunak&last_name=Shakya

# Import modules for CGI handling
import cgi

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from text fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

# Get data from checkbox fields
if form.getvalue('python'):
    python_flag = "ON"
else:
    python_flag = "OFF"

if form.getvalue('java'):
    java_flag = "ON"
else:
    java_flag = "OFF"

# Get data from radio fields
if form.getvalue('gender'):
    gender = form.getvalue('gender')
else:
    gender = "Not set"

# Get data from dropdown field
if form.getvalue('education'):
    education = form.getvalue('education')
else:
    education = "Not entered"

# Get the filename
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
    message = 'The file "' + fileitem.filename + '" was uploaded successfully!'
else:
    message = 'No file was uploaded'

# Get data from textarea field
if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "Not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Form handling app</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("<p>CheckBox Python is : %s</p>" % python_flag)
print("<p>CheckBox JAVA is : %s</p>" % java_flag)
print("<p>Selected Gender is : %s</p>" % gender)
print("<p>Entered Text Content is %s</p>" % text_content)
print("<p>Education level is %s</p>" % education)
print("<p>%s</p>" % (message))
print("</body>")
print("</html>")
