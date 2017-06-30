# -*- coding: utf-8 -*-

import re
import __init__
from ip_helper import ip_2_int

__init__  # Suppress PEP8 F401

REGEX = ('^((25[0-5]|2[0-4]\d|[1]?[1-9]?\d)\.){3}'
         '(25[0-5]|2[0-4]\d|[1]?[1-9]?\d)$')
CLASS_A = '10.255.255.255'
CLASS_B = '172.31.255.255'
CLASS_C = '192.168.255.255'


def is_ip(str_ip):
    """whether given dot-decimal IP is legal"""
    pattern = re.compile(REGEX)
    if pattern.match(str_ip):
        return True
    return False


def is_public_ip(str_ip):
    """whether given dot-decimal IP is public"""
    return not is_private_ip(str_ip)


def is_private_ip(str_ip):
    """
    whether given dot-decimal IP is private
    Class A: 10.0.0.0--10.255.255.255
    Class B: 172.16.0.0--172.31.255.255
    Class C: 192.168.0.0--192.168.255.255
    """
    ip = ip_2_int(str_ip)
    net_a = ip_2_int(CLASS_A) >> 24
    net_b = ip_2_int(CLASS_B) >> 20
    net_c = ip_2_int(CLASS_C) >> 16
    return ip >> 24 == net_a or ip >> 20 == net_b or ip >> 16 == net_c


if __name__ == '__main__':
    # check IP legitimacy
    illegal_ips = [
        '192.168.0',
        '256.0.0.1',
        'a.b.c.d'
    ]
    legal_ips = [
        '0.0.0.0',
        '127.0.0.1',
        '255.255.255.255'
    ]
    for ip in illegal_ips:
        result = is_ip(ip)
        assert result is False
    for ip in legal_ips:
        result = is_ip(ip)
        assert result is True
    # identify public or private IP
    private_ips = [
        '10.1.1.1',
        '172.20.1.1',
        '192.168.10.10'
    ]
    public_ips = [
        '123.58.10.10',
        '58.10.2.4'
    ]
    for ip in private_ips:
        result = is_private_ip(ip)
        assert result is True
    for ip in public_ips:
        result = is_private_ip(ip)
        assert result is False
