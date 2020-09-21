import socket

SOCKET_OPEN = 0
SOCKET_CLOSED = 1
SOCKET_FIREWALLED = 2
SOCKET_NO_SUCH_SERVICE = 3


def read_fingerprint_from_socket(socket):
    try:
        data = bytearray()
        while True:
            chunk = socket.recv(4096)
            if not chunk:
                break
            data.extend(chunk)
    except socket.timeout:
        pass
    finally:
        return data.decode('utf-8').strip() 


def tcp_connect_port(host, port, fingerprint):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # 2 seconds
        s.connect((host, port))

        if fingerprint:
            return (SOCKET_OPEN, read_fingerprint_from_socket(s))

        return SOCKET_OPEN
    except ConnectionRefusedError:
        return SOCKET_CLOSED
    except socket.timeout:
        return SOCKET_FIREWALLED


def tcp_connect_scan(host, ports, fingerprint=False):
    for port in ports:

        # Get port by service name if port is not a number
        if not str(port).isdigit():
            try:
                port = socket.getservbyname(port)
            except OSError:
                yield (port, SOCKET_NO_SUCH_SERVICE)
                continue

        result = tcp_connect_port(host, port, fingerprint)
        if isinstance(result, tuple):
            yield (port, *result)
        else:
            yield (port, result)
