import marshal, codecs, binascii, zlib, bz2, pyfiglet, os, time, dis, lzma, gzip, base64
from sys import stdout
import subprocess as sp
import sys, random, base64, getpass, re
from py_compile import compile as _compile
# from cfonts import render, say
import webbrowser
webbrowser.open('https://t.me/KLM_J')
from rich.panel import Panel as nel
from rich import print as cetak
import pyfiglet, requests, subprocess

d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
A = "\033[1;91m"  # Red
B = "\033[1;90m"  # Gray
C = "\033[1;97m"  # White
E = "\033[1;92m"  # Green
H = "\033[1;93m"  # Yellow
K = "\033[1;94m"  # Purple
L = "\033[1;95m"  # Pink
M = "\033[1;96m"  # Blue
R = '\x1b[1;31m'  # Red
G = '\x1b[1;32m'  # Green
B = '\x1b[0;94m'  # Purple
Y = '\x1b[1;33m'  # Yellow
E = '\033[91m'  # Red
###############
a20 = '\x1b[38;5;226m'  # Light Yellow
a16 = '\x1b[38;5;48m'  # Light Green
M = '\033[2;36m'  # Blue
a5 = '\x1b[38;5;208m'  # Orange
a6 = '\x1b[38;5;5m'  # Purple
a7 = '\x1b[38;5;13m'  # Pink
a8 = '\x1b[1;30m'  # Black
a9 = '\x1b[1;37m'  # White
a10 = '\x1b[38;5;52m'  # Brown
a11 = '\x1b[38;5;8m'  # Gray
a12 = '\x1b[38;5;220m'  # Gold
a13 = '\x1b[38;5;7m'  # Silver
a40 = '\x1b[38;5;117m'  # Sky Blue

def clr():
    os.system("clear")

def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)

def running(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)
    except (KeyboardInterrupt, EOFError):
        print('Exit!')

os.system('clear')
import pyfiglet
import requests
import re
from rich.panel import Panel as Ch
from rich import print as code

a = '/033[31m'
s = '/033[32m'
d = '/033[33m'
g = '/033[34m'

def PY_97():
    print(a16 + '⏕' * 28)
    print(a20 + ' ➲ 1. Decode marshal     ')
    print(a20 + ' ➲ 2. Decode marshal 3.7    ')
    print(a20 + ' ➲ 3. Decode base32    ')
    print(a20 + ' ➲ 4. Decode base64    ')
    print(a20 + ' ➲ 5. Decode base16    ')
    print(a20 + ' ➲ 6. Decode base85    ')
    print(a20 + ' ➲ 7. Decode lambda.marshal.base64.zlib    ')
    print(a20 + ' ➲ 8. Decode lambda    ')
    print(a20 + ' ➲ 9. Decode emoji    ')
    print(a20 + ' ➲ 10. Decode hex    ')
    print(a20 + ' ➲ 11. Decode pyc    ')
    print(a20 + ' ➲ 12. Decode lzma.zlib    ')
    print(a20 + ' ➲ 13. Decode binascii    ')
    print(a20 + ' ➲ 14. Decode zlib,base    ')
    print(a20 + ' ➲ 15. Decode gzip    ')
    print(a20 + ' ➲ 16. Decode codecs    ')
    print(a20 + ' ➲ 17. Decode simple pyc    ')
    print(a20 + ' ➲ 18. Decode simple pyc2    ')
    print(a20 + ' ➲ 19. Decode lzma    ')
    print(a20 + ' ➲ 20. Cython    ')
    print(a20 + ' ➲ 0. Exit    ')
    print(a16 + '⏔' * 28)

# @U_G_GU
def ahm():
    b = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File marshal : ")
    am = ('\x1b[38;5;51m', '\x1b[38;5;63m ', '\x1b[38;5;73m2', '\x1b[38;5;83m8', '\x1b[38;5;93m0', '\x1b[38;5;103m0')
    for i in range(50):
        time.sleep(.1)
        sys.stdout.write('\rDecode marshal ...>>> ')
        sys.stdout.flush()
        print('')
    a = open(b).read()
    m = False
    k = ""
    n = 0
    for x in a:
        if x == "'" and a[n-1] == "b":
            m = True
            continue
        if x == "'" and not a[n-1] == "\\":
            break
        if m:
            k = k + a[n+1]
        n += 1
    k += "'"
    k = "b'" + k
    a = f"exec(marshal.loads({k}))"
    exec(a)

def unmarszlib():
    try:
        files = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File marshal 3.7: ")
    except:
        exit("")
    if len(files) == 0:
        exit("")
    try:
        bk = open(files, "r").read()
    except IOError:
        print("File not found")
        exit()
    bk = bk.replace("import", "import uncompyle6,")
    bk = bk.replace("exec(", "uncompyle6.main.decompile(3.7,")
    bk = bk.replace(")))", ")),open(\"hasil.py\",\"w\"))")
    exec(bk)

def exit():
    print('Goodbye!')
    sys.exit()

def ex():
    print('Goodbye!')
    sys.exit()

def men():
    file = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File : ")
    ogge = str(open(file, "r").read())
    data = ogge.replace("_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b", "_ =")
    data2 = f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """
    open("PY_97.py", "w").write(data2)
    os.system("python PY_97.py > PY_97.py")
    PY_97 = str(open("PY_97.py", "r").read())
    data3 = f"""#Decode By  @ZZKGZ\nimport marshal\nexec(marshal.loads({PY_97}))"""
    open("PY_97.py", "w").write(data3)
    print("marshal-magic PY_97.py -m normal -o PY_97.py")
    print('')
    print('\n')
    print('[•] Decode Done √')

# (decode lambda+ emoji)
# PY_97
def lamb():
    print("------------------------------------------")
    file_nme = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File Lambda : ")
    print("------------------------------------------")
    try:
        with open(file_nme, 'r') as file:
            Hussein = file.read()
            NB_JG = Hussein.replace("exec", "print")
        with open(file_nme, 'w') as file:
            file.write(NB_JG)
        print("The first step completed successfully ✅")
        os.system("clear")
        subprocess.run(['python3', f'{file_nme}'])
    except FileNotFoundError:
        print("The file was not found. Please select from the list below 👇🏻")
        os.system("ls")
    except Exception as e:
        print(f"Error: {e}")

# PY_97
def emoji():
    file_name = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File emoji: ")
    try:
        with open(file_name, 'r') as file:
            Hussein = file.read()
            NB_JG = Hussein.replace("exec", "print")
        with open(file_name, 'w') as file:
            file.write(NB_JG)
        print("The first step completed successfully ✅")
        os.system("clear")
        subprocess.run(['python3', f'{file_name}'])
    except FileNotFoundError:
        print("The file was not found. Please select from the list below 👇🏻")
        os.system("ls")
    except Exception as e:
        print(f"Error: {e}")

# (decode base )
# PY_97
def decode_base64_file():
    decode_base64 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base64:  ")
    with open(decode_base64, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b64decode(encoded_data)
    with open("Decode_base64.py", 'wb') as file:
        file.write(decoded_data)
    print("The file has been decoded and the decoded text saved in Decode_base64.py.")

# PY_97
def decode_base16_file():
    decode_base16 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base16:  ")
    with open(decode_base16, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b16decode(encoded_data)
    with open("Decode_base16.py", 'wb') as file:
        file.write(decoded_data)
    print("The file has been decoded and the decoded text saved in Decode_base16.py.")

# PY_97
def decode_base32_file():
    decode_base32 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base32:  ")
    with open(decode_base32, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b32decode(encoded_data)
    with open("Decode_base32.py", 'wb') as file:
        file.write(decoded_data)
    print("The file has been decoded and the decoded text saved in Decode_base32.py.")

# PY_97
def decode_base85_file():
    decode_base85 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base85:  ")
    with open(decode_base85, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b85decode(encoded_data)
    with open("Decode_base85.py", 'wb') as file:
        file.write(decoded_data)
    print("The file has been decoded and the decoded text saved in Decode_base85.py.")

# PY_97
def decode_hex():
    filename = input("Enter the name of the encoded file: ")
    with open(filename, "rb") as f:
        encoded_data = f.read().hex()
        decoded_data = bytes.fromhex(encoded_data)
        decoded_filename = f"{filename}_decoded.py"
    with open(decoded_filename, "wb") as f:
        f.write(decoded_data)
    print(f"File {filename} decoded successfully and saved as {decoded_filename}")

# PY_97
def lzm_zlb():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU    *_*')

# @PY_97
def zlb():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU  *_*')

# PY_97
def lzm():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU  *_*')

# PY_97
def cods():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU   *_*')

# PY_97
def binasci():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU  *_*')

# PY_97
def gzp_base():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU  *_*')

# PY_97
def zlib_base():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU   *_*')

# PY_97
def smple_pyc():
    clr()
    Ty = input(a9 + 'input your file : ')
    Tr = input(a12 + 'output your file : ')
    com = f'pycdc {Ty} > {Tr}'
    os.system(com)
    slow(G + '  by @U_G_GU  *_*')

# PY_97
def smple_pyc2():
    clr()
    Ty = input('input your file : ')
    Tr = input('output your file : ')
    com = f'uncompyle6 {Ty} > {Tr}'
    os.system(com)
    slow('  by @U_G_GU  *_*')

# PY_97
def gzp():
    clr()
    file = input(a9 + 'input your file : ')
    filer = input(a12 + 'output your file : ')
    com = f'marshal-magic {file} -o {filer} '
    os.system(com)
    slow(G + '  by @U_G_GU  *_*')

# PY_97
def cython():
    webbrowser.open('https://t.me/PY_97')
    lzm()

print(f'''{a5}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
　　⡠⠚⠁　⣀⡠⠒⠚⡄⠑　⠈⠳⡄⠀⠀⠀
　⢀⡞⠁⠠⠦　　　⠸⠠⠀　⢀⠤⠜⣆⠀⠀
⢀⡎　　⠡⡀　⠐⠂　⠈　　⣁⠀⣀⣸⡆⠀
⢸⠀⡤⡀　⡧　　　⠠⠤　⠨　　　⢧⠀
　⠘⡆⡄　 ⣿⣿⣿🔥⣿⣿⡆　⣼⣿🔥⣿⡏⠀
　　⢻⠀⠇　⠙⢿⣿⣿⡿⢿⠁ ⠻⠿⠿⢿⡅⠀
⠀⠀⢈⡷⢼⠈⢈⣀⠠　⠐⠊⢀⣾⡟⣦⠤⠼⠁⠀
　　⠘⣆⠅⣽⠉⠘⡆⠆　⢀⠛⠓⡁⢻⠀⠀⠀⠀
　　　⢺⠐⠙⢦⢀⡧⣈⣘⣈⣀⣢⣣⣾
⠀⠀⠀
''')  

print(a40 + pyfiglet.figlet_format("GlitchbyAnne"))

while True:
    try:
        PY_97()
        choice = input(f"\n{a7}[ PY_97 ] ➜ Select : ")

        if choice == "1":
            ahm()
        elif choice == "2":
            unmarszlib()
        elif choice == "3":
            decode_base32_file()
        elif choice == "4":
            decode_base64_file()
        elif choice == "5":
            decode_base16_file()
        elif choice == "6":
            decode_base85_file()
        elif choice == "7":
            men()
        elif choice == "8":
            lamb()
        elif choice == "9":
            emoji()
        elif choice == "10":
            decode_hex()
        elif choice == "11":
            smple_pyc()
        elif choice == "12":
            lzm_zlb()
        elif choice == "13":
            binasci()
        elif choice == "14":
            zlib_base()
        elif choice == "15":
            gzp()
        elif choice == "16":
            cods()
        elif choice == "17":
            smple_pyc()
        elif choice == "18":
            smple_pyc2()
        elif choice == "19":
            lzm()
        elif choice == "20":
            cython()
        elif choice == "0":
            ex()
        else:
            print(a5 + "Invalid option!")

        input(a11 + "\nPress Enter to continue...")
        clr()

    except KeyboardInterrupt:
        print("\nInterrupted by user!")
        sys.exit()
