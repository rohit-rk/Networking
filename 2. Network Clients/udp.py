#! /usr/bin/env python
# UDP Example 

import socket, sys

host = sys.argv[1]
port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(port)
except ValueError:
    # That didn't work. Look it up instead.
    port = socket.getservbyname(port, 'udp')

s.connect((host,port))
print "Enter date to transmit:"
data = sys.stdin.readline().strip()
s.sendall(data)
print "Looking for replies: press Ctrl-C or Ctrl-Break to stop."

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print buf
    