import requests
import sys

if len(sys.argv) not in [2, 3]:
    exit('Improper number of arguments', 1)
if sys.argv[2]:
    try:
        port_number = sys.argv[2]
    except ValueError:
        exit(2)
else:
    port_number = '80'

url = sys.argv[1] + f":{port_number}" if sys.argv[:4] == 'http' else 'http://' + sys.argv[1] + f":{port_number}"

try:
    reply = requests.head(url=url)
except requests.exceptions.ConnectTimeout:
    exit(3)
except requests.exceptions.RequestException:
    exit(4)

print(reply)
