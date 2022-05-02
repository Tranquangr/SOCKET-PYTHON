#mở các app running trong python
import subprocess
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName,Id'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
data = []
for o in proc.stdout:
    if o.rstrip():
        i=o.decode().rstrip()
        data.append(i)
print("------------------------")
for i in data:
    print(i)

