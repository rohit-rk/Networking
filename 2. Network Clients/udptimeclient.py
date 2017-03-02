#! /usr/bin/env python
# UDP Connectionless Example 2kjj

import socket, sys, struct, time

hostname = sys.argv[1]
port = int(sys.argv[2])

host = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s. sendto('',(host, port))
print "Looking for replies; press Ctrl-C to stop."

buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print "Wrong-sized reply %d: %s" % (len(buf), buf)
    sys. exit(1)
secs = struct.unpack("1I", buf)[0]
secs -= 2208988800
print time.ctime(int(secs))
