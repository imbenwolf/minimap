""" Minimap, a mini TCP scanner """

import tcp

def main():
    print(tcp.tcp_connect_port("127.0.0.1", 80))
    return 0