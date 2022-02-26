import sys
import requests

print(sys.version)
print("Hello world") 
r = requests.get('https://www.google.com')
if r.status_code == 200:
    print("TLS seems OK")
else:
    print("something is off")
