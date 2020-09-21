import socket

SOCKET_OPEN = 0
SOCKET_CLOSED = 1
SOCKET_FIREWALLED = 2
SOCKET_NO_SUCH_SERVICE = 3


def tcp_connect_port(host, port, fingerprint=False):
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
    for port in ports:
        
        # Get port by service name if port is not a number
        if not str(port).isdigit():
            try:
                port = socket.getservbyname(port)
            except OSError:
                yield (port, SOCKET_NO_SUCH_SERVICE)
                continue

        yield (port, tcp_connect_port(host, port))
