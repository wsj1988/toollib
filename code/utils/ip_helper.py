# -*- coding: utf-8 -*-

import socket
import struct
import traceback


def ip_2_int(str_ip):
    """convert from network sequence to host sequence"""
    try:
        int_ip = socket.ntohl(struct.unpack('I', socket.inet_aton(str_ip))[0])
    except:
        traceback.print_exc()
        return None
    return int_ip


def int_2_ip(int_ip):
    """convert from host sequence to network sequence"""
    try:
        str_ip = socket.inet_ntoa(struct.pack('I', socket.htonl(int_ip)))
    except:
        traceback.print_exc()
        return None
    return str_ip


if __name__ == '__main__':
    str_ip = '192.168.44.17'
    int_ip = ip_2_int(str_ip)
    print int_ip
