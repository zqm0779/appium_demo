# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10
@Auth ： zhangqimin
@File ：get_local_pc_ip.py
@IDE ：PyCharm

"""
import socket
import uuid
import time
import os
def get_host_ip():
    # hostname = socket.gethostname()
    # ip = socket.gethostbyname(hostname)
    # print(ip)
    try:
        my = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        my.connect(('8.8.8.8', 80))
        ipList = my.getsockname()
    finally:
        my.close()
    return ipList
#获取电脑mac地址
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

if __name__ == '__main__':
    print(get_mac_address())
    print(get_host_ip())