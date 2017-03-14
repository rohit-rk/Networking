#!/usr/bin/env python
# Python Network Programming


import socket

def print_machine_info():
    '''function to provide a local machine's name and IP address'''
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)

if __name__ == '__main__':
    print_machine_info()