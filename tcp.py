import socket

SOCKET_OPEN = 0
SOCKET_CLOSED = 1
SOCKET_FIREWALLED = 2

def tcp_connect_port(host, port):
    try:
        socket.create_connection((host, port), 2)
        return SOCKET_OPEN
    except ConnectionRefusedError:
        return SOCKET_CLOSED
    except TimeoutError:
        return SOCKET_FIREWALLED

def tcp_connect_scan(host, ports):
    return {port: tcp_connect_port(host, port) for port in ports}