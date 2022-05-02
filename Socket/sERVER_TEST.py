import psutil
import socket
import pickle

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1250))
s.listen(1)

while True:
    clientsocket, address=s.accept()
    print(f"Connection from {address} has been established")
    #module process running

    processName = 'exe'
    listOfProcessObjects = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower():
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(type(listOfProcessObjects))
    data=pickle.dumps(listOfProcessObjects)
    clientsocket.send(data)

    #end
    break
s.close()
