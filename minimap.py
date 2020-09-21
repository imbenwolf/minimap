""" Minimap, a mini TCP scanner """

import tcp


def main():
    for res in tcp.tcp_connect_scan("access-hat.ch", ['https', 444, 666]):
        print(res)
    return 0
