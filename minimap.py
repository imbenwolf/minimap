""" Minimap, a mini TCP scanner """

import tcp


def main():
    for res in tcp.tcp_connect_scan("192.168.220.211", ['ssh', 444, 666], True):
        print(res)
    return 0
