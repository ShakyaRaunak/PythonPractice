import os

"""
CGI scripts cannot access client HTTP headers directly, but you can access all cookies sent from the client using the 
HTTP_COOKIE environment variable. This environment variables is formatted as a series of key=value pairs delimited by semicolons.
"""

print("Content-type: text/plain\n")

if "HTTP_COOKIE" in os.environ:
    print(os.environ["HTTP_COOKIE"])
else:
    print("HTTP_COOKIE not set!")
