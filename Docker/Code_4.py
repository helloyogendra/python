import socket
import platform
import os

cmd = 'hostname'

print('Executing a Python Script inside a Docker Container::')
print(f'Following output is produced by a Docker Container where Hostname is : {os.system(cmd)}')
print(f'Computer Name is : {platform.node()}')
print(f'Operating System is : {platform.system()}')
print(f'Machine Type is : {platform.machine()}')
print(f'IP Address is : {socket.gethostbyname(socket.gethostname())}')



