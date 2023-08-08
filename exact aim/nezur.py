import time
import os

art = '''\
███╗░░██╗ ███████╗ ███████╗ █╗░░░░░██╗ ██████╗░
████╗░██║ ██╔════╝ ╚══███╔╝ ██║░░░░░██║██╔══██╗                        
██╔██╗██║ █████╗░░ ░░███╔═╝ ██║░░░░░██║██████╦╝
██║╚████║ ██╔══╝░░ ███╔═╝░░ ██║░░░░░██║██╔══██╗
██║░╚███║ ███████╗ ███████╗ ╚██████╗██║██║░░██║
╚═╝░░╚══╝ ╚══════╝ ╚══════╝ ░╚═════╝╚═╝╚═╝░░╚═╝'''

print(art)
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

print("loading")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("loading  .")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("loading ..")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("loading ...")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(1)

# Open the aim.exe file
aim_path = r'C:\Users\William\Desktop\exact aim\aim.exe'
os.startfile(aim_path)
