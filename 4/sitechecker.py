import sys
import socket

if len(sys.argv) not in [2, 3]:
    exit('Improper number of arguments',1)
if sys.argv[2]:
    try:
        port_number = int(sys.argv[2])
    except ValueError:
        exit(2)
else:
    port_number = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((sys.argv[1], port_number))
    sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
              bytes(sys.argv[1], "utf8") +
              b"\r\nConnection: close\r\n\r\n")

    reply = sock.recv(10000)
except TimeoutError:
    exit(3)
except Exception:
    exit(4)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply).split(sep='\\n')[0])

