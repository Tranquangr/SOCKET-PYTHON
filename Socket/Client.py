import socket
import pyautogui
from PIL import Image


def Sreenshot():
    while True:
        content2 = input(" Show(1) or Save(2): ")
        i = content2
        s.send(content2.encode())
        if i == "2":
            size = int(s.recv(10).decode('utf-8'))
            the_photo = s.recv(size)
            width, height = pyautogui.size()
            img_to_save = Image.frombytes("RGB", ((width, height)), the_photo)
            img_to_save.save("screenshot_save_server.png")
        loop = input("Continue Sreenshot (yes)?: ")
        if loop != "yes":
            s.send(loop.encode())
            break

def Process_running():
    while True:
        content2 = input("Show_Process_Server(1) or Kill_Process_Server(2) or Open_Process_Server(3): ")
        i = content2
        s.send(content2.encode())
        if i == "1":
            print("ProcessName\t\t\t\t\t  Id\n-----------                   --")
            data = s.recv(8192)
            data_arr = data.decode('utf-8')
            data_arr = eval(data_arr)
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
        elif i == "2":
            content3 = input("Input Process_ID you want kill: ")
            s.send(content3.encode())
        elif i== "3":
            content4 = input("Input name_Process you want open: ") + 'exe'
            s.send(content4.encode())
        loop = input("Continue Process_running (yes)?: ")
        if loop != "yes":
            s.send(loop.encode())
            break

def App_running():
    while True:
        content2 = input("Show_App_Server(1) or Kill_App_Server(2) or Open_App_Server(3): ")
        i = content2
        s.send(content2.encode())
        if i == "1":
            data = s.recv(8192)
            data_arr = data.decode('utf-8')
            data_arr = eval(data_arr)
            for i in data_arr
                print(i)
        elif i == "2":
            content3 = input("Input App_ID you want kill: ")
            s.send(content3.encode())
        elif i== "3":
            content4 = input("Input name_App you want open: ") + 'exe'
            s.send(content4.encode())
        loop = input("Continue App_running (yes)?: ")
        if loop != "yes":
            s.send(loop.encode())
            break

if (__name__=="__main__"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1274))
    print("Successful connection")
    while True:
        func_tion = input("""1. Sreenshot
2. Shutdow
3. Process Running
4. App Running
5. Exit
---Which type do you want to?--- """)
        s.send(func_tion.encode())
        if func_tion == "1":
            Sreenshot()
        if func_tion == "3":
            Process_running()
        if func_tion == "4"
            App_running()
        if func_tion == "5":
            break

