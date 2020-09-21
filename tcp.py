import socket

SOCKET_OPEN = 0
SOCKET_CLOSED = 1
SOCKET_FIREWALLED = 2


def tcp_connect_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # 2 seconds
        s.connect((host, port))
        return SOCKET_OPEN
    except ConnectionRefusedError:
        return SOCKET_CLOSED
    except socket.timeout:
        return SOCKET_FIREWALLED


def tcp_connect_scan(host, ports):
    return ((port, tcp_connect_port(host, port)) for port in ports)
