# File Sharing App using Python


import http.server # for implementing the HTTP Web servers
import socket # provides access to the BSD socket interface
import socketserver # framework for network servers
import webbrowser # to display a Web-based documents to users

import pyqrcode # to generate qrcode
from pyqrcode import QRCode

import png # convert into png format
import os # to access operating system control

PORT = 8010  # assigning the appropriate port value
os.environ['USERPROFILE']  # this finds the name of the computer user


# changing the directory to access the files desktop
# with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
os.chdir(desktop)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()


# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# converting the IP address into the form of a QRcode
# with the help of pyqrcode module

url = pyqrcode.create(link) # converts the IP address into a Qrcode
url.svg("myqr.svg", scale=8) # saves the Qrcode inform of svg
webbrowser.open('myqr.svg') # opens the Qrcode image in the web browser

# Creating the HTTP request and serving the
# folder in the PORT 8010,and the pyqrcode is generated
# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print("serving at port", PORT)
	print("Type this in your Browser", IP)
	print("or Use the QRCode")
	httpd.serve_forever()
