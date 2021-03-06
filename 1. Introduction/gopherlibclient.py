#! /usr/bin/env python 
# High-Level Gopher Client 

import gopherlib, sys

host = sys.argv[1]
file = sys.argv[2]

f = gopherlib.send_selector(file, host)
for line in f.readlines():
	sys.stdout.write(line)
