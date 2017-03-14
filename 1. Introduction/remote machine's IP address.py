#!/usr/bin/env python
# Python Network Programming

import socket

def get_remote_machine_info():
    '''function to provide a remote machine's IP address'''
    remote_host = 'www.python.org'
    try:
        print("IP address: %s" %socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print("%s: %s" %(remote_host, err_msg))    

if __name__ == '__main__':
    get_remote_machine_info()