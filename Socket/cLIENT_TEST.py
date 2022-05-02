import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1250))
print("successful connection")
print("ProcessName\t\t\t\t\t  Id\n-----------                   --")
data = []
while True:
    packet = s.recv(4096)
    if not packet: break
    data.append(packet)
data_arr = pickle.loads(b"".join(data))
for elem in data_arr:
    processID = str(elem['pid'])
    processName = elem['name']
    print(processName, end='')
    tmp = len(processName)
    i = 0
    while i < (30 - tmp):
        print(" ", end="")
        i = i + 1
    print(processID)