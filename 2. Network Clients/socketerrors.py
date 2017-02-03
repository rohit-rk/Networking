#! /usr/bin/env python
# Error handling example

import socket, sys

host = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
	print "Strange error creating socket: %s" %e
	sys.exit(1)

# Try parsing it as a numeric port number.
try:
	port = int(port)
except valueError:
	# That didn't work, so it's probably a protocol name
	# Look it up instead.
	try: 
		port = socket.getservbyname(port, 'tcp')
	except socket.error, e:	
		print "Couldn't find our port: %s" %e
 		sys.exit(1)


try:
 	s.connect((host, port))
except socket.gaierror, e:
	print "Address related error connecting to server: %s" %e
	sys.exit(1)
except socket.error, e:
	print "Connection error: %s" %e
	sys.exit()

try:
	s.sendall("GET %s HTTP/1.0\r\n\r\n" %filename)
except socker.error. e:
	print "Error sending data: %s" %e
	sys.exit(1)

while 1:
	try:
		buf = s.recv(2048)
	except socket.error, e:
		print "Error receiving data: %s" %e
		sys.exit(1)
	if not len(buf):
		break
	sys.stdout.write(buf)
