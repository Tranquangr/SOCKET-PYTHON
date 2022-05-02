import os
import signal
import pyautogui
import socket
import psutil
import subprocess

def Sreenshot():
    while True:
        content2 = clientsocket.recv(1024).decode()
        myScreenshot = pyautogui.screenshot()
        i = content2
        if i == "1":
            myScreenshot.save("111.png")
            os.system('start 111.png')
        elif i == "2":
            photo_to_send = myScreenshot.tobytes()
            size = len(photo_to_send)
            clientsocket.send(bytes(str(size), 'utf-8'))
            clientsocket.send(photo_to_send)
        content3 = clientsocket.recv(1024).decode()
        if content3 != "yes":
            break


def Process_running():
    while True:
        content2 = clientsocket.recv(1024).decode()
        i = content2
        print("mày có chạy vào đây ko ??")
        if i == "1":
            processName = ''
            listOfProcessObjects = []
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name'])
                    # Check if process name contains the given name string.
                    if processName.lower() in pinfo['name'].lower():
                        listOfProcessObjects.append(pinfo)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            data = str(listOfProcessObjects)
            clientsocket.send(data.encode())
        if i == "2":
            content3=int(clientsocket.recv(1024).decode())
            os.kill(content3,signal.SIGTERM)
        if i == "3":
            content4=clientsocket.recv(1024).decode()
            os.system(content4)
        content5 = clientsocket.recv(1024).decode()
        print(content5)
        if content5 != "yes":
            break

def App_running():
    while True:
        content2 = clientsocket.recv(1024).decode()
        i = content2
        if i == "1":
            cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName,Id'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            data = []
            for o in proc.stdout:
                if o.rstrip():
                    i = o.decode().rstrip()
                    data.append(i)
            data = str(listOfProcessObjects)
            clientsocket.send(data.encode())
        if i == "2":
            content3=int(clientsocket.recv(1024).decode())
            os.kill(content3,signal.SIGTERM)
        if i == "3":
            content4=clientsocket.recv(1024).decode()
            os.system(content4)
        content5 = clientsocket.recv(1024).decode()
        print(content5)
        if content5 != "yes":
            break


if (__name__=="__main__"):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1274))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
        while True:
            print("Lạy mày chạy đi để tao check")
            func_tion = clientsocket.recv(1024).decode()
            if func_tion == "1":
                Sreenshot()
            if func_tion == "2":
                os.system("shutdown /s /t 1")
            if func_tion == "3":
                Process_running()
            if func_tion == "4":
                App_running()
            if func_tion == "5":
                break
        s.close()
