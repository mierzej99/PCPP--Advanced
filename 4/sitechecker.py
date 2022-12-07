import sys
import socket

if len(sys.argv) not in [2, 3]:
    exit('Improper number of arguments')
if sys.argv[2]:
    port_number = sys.argv[2]
else:
    port_number = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], 80))