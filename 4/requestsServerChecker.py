import requests
import sys

if len(sys.argv) not in [2, 3]:
    exit('Improper number of arguments',1)
if sys.argv[2]:
    try:
        port_number = int(sys.argv[2])
    except ValueError:
        exit(2)
else:
    port_number = 80


try:
    reply = requests.head()