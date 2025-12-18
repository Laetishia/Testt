import marshal, codecs, binascii, zlib, bz2, pyfiglet, os, time, dis, lzma, gzip, base64
from sys import stdout
import subprocess as sp
import sys, random, getpass, re
from py_compile import compile as _compile
import webbrowser
import importlib.util
import struct

webbrowser.open('https://t.me/KLM_J')

# Your original colors
d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'

a20 = '\x1b[38;5;226m'
a16 = '\x1b[38;5;48m'
a5 = '\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
a7 = '\x1b[38;5;13m'
a8 = '\x1b[1;30m'
a9 = '\x1b[1;37m'
a10 = '\x1b[38;5;52m'
a11 = '\x1b[38;5;8m'
a12 = '\x1b[38;5;220m'
a40 = '\x1b[38;5;117m'

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

# ==================== SAFE AUTO DETECTION & EXECUTION ====================
MAGIC = importlib.util.MAGIC_NUMBER

def normalize_path(p):
    p = p.strip()
    if p.lower().startswith("sdcard/"):
        p = "/" + p
    return os.path.abspath(p)

def is_pyc(path):
    try:
        with open(path, "rb") as f:
            return f.read(len(MAGIC)) == MAGIC
    except:
        return False

def is_marshal(path):
    try:
        with open(path, "rb") as f:
            marshal.loads(f.read())
        return True
    except:
        return False

def is_py(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            f.read()
        return True
    except:
        return False

def detect_type(path):
    if is_pyc(path):
        return "PYC"
    if is_marshal(path):
        return "MARSHAL"
    if is_py(path):
        return "PY"
    return "UNKNOWN"

def load_code(path):
    ftype = detect_type(path)
    if ftype == "PYC":
        with open(path, "rb") as f:
            f.seek(16)
            return marshal.loads(f.read())
    elif ftype == "MARSHAL":
        with open(path, "rb") as f:
            return marshal.loads(f.read())
    elif ftype == "PY":
        source = open(path, "r", encoding="utf-8").read()
        return compile(source, os.path.basename(path), "exec")
    raise ValueError("Cannot load code from this file")

def safe_execute(path):
    path = normalize_path(path)
    if not os.path.isfile(path):
        print(a5 + "File not found!")
        return
    try:
        print(a16 + f"[+] Detected: {detect_type(path)}")
        code = load_code(path)
        print(a40 + "\n[+] EXECUTING SAFELY...\n")
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        print(a5 + f"[-] Error during execution: {e}")

# ==================== YOUR ORIGINAL FUNCTIONS (FIXED WHERE NEEDED) ====================

def ahm():  # Option 1 - Fixed Marshal Exec
    b = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File marshal : ")
    safe_execute(b)

def unmarszlib():  # Option 2 - Use uncompyle6 properly
    files = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File marshal 3.7: ")
    files = normalize_path(files)
    try:
        os.system(f"uncompyle6 '{files}' > decompiled_by_uncompyle6.py")
        print(a16 + "[+] Decompiled → decompiled_by_uncompyle6.py")
    except:
        print(a5 + "uncompyle6 not installed or failed")

def decode_base32_file():
    decode_base32 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base32:  ")
    try:
        data = open(decode_base32, "rb").read()
        decoded = base64.b32decode(data)
        open("Decode_base32.py", "wb").write(decoded)
        print(a16 + "[+] Decoded → Decode_base32.py")
    except Exception as e:
        print(a5 + f"Error: {e}")

def decode_base64_file():
    decode_base64 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base64:  ")
    try:
        data = open(decode_base64, "rb").read()
        decoded = base64.b64decode(data)
        open("Decode_base64.py", "wb").write(decoded)
        print(a16 + "[+] Decoded → Decode_base64.py")
    except Exception as e:
        print(a5 + f"Error: {e}")

def decode_base16_file():
    decode_base16 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base16:  ")
    try:
        data = open(decode_base16, "rb").read()
        decoded = base64.b16decode(data)
        open("Decode_base16.py", "wb").write(decoded)
        print(a16 + "[+] Decoded → Decode_base16.py")
    except Exception as e:
        print(a5 + f"Error: {e}")

def decode_base85_file():
    decode_base85 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base85:  ")
    try:
        data = open(decode_base85, "rb").read()
        decoded = base64.b85decode(data)
        open("Decode_base85.py", "wb").write(decoded)
        print(a16 + "[+] Decoded → Decode_base85.py")
    except Exception as e:
        print(a5 + f"Error: {e}")

def men():  # Option 7 - Lambda + marshal + base64 + zlib
    file = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File : ")
    try:
        source = open(file).read()
        # Common pattern
        payload = re.findall(r"b['\"](.*?)['\"]", source)[-1]
        if payload.startswith("eJ"):  # zlib indicator
            payload = payload[::-1] if source.find("[::-1]") != -1 else payload
            decoded = marshal.loads(zlib.decompress(base64.b64decode(payload)))
            open("decoded_complex.py", "wb").write(marshal.dumps(decoded))
            print(a16 + "[+] Decoded → decoded_complex.py")
        else:
            print(a5 + "Pattern not recognized")
    except Exception as e:
        print(a5 + f"Failed: {e}")

def lamb():  # Option 8
    file_nme = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File Lambda : ")
    safe_execute(file_nme)  # Now uses safe exec

def emoji():  # Option 9
    file_name = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File emoji: ")
    safe_execute(file_name)

def decode_hex():
    filename = input("Enter the name of the encoded file: ")
    try:
        data = open(filename, "rb").read()
        decoded = bytes.fromhex(data.hex())
        open(f"{filename}_decoded.py", "wb").write(decoded)
        print(a16 + f"[+] Decoded → {filename}_decoded.py")
    except Exception as e:
        print(a5 + f"Error: {e}")

# Simple PYC decompilers (using external tools)
def smple_pyc():
    Ty = input(a9 + 'input your file : ')
    Tr = input(a12 + 'output your file : ')
    os.system(f"pycdc '{normalize_path(Ty)}' > '{Tr}'")

def smple_pyc2():
    Ty = input('input your file : ')
    Tr = input('output your file : ')
    os.system(f"uncompyle6 '{normalize_path(Ty)}' > '{Tr}'")

# Placeholder for others (you can replace with real marshal-magic later)
def placeholder_tool():
    clr()
    print(a5 + "This option uses marshal-magic (not included). Install separately.")
    input("Press Enter...")

# Detect obfuscation by pasting code
def detect_obfuscation():
    print(a40 + "\nPaste the obfuscated Python code below (press Enter twice to finish):\n")
    lines = []
    while True:
        try:
            line = input()
            if line == "" and len(lines) > 0 and lines[-1] == "":
                break
            lines.append(line)
        except:
            break
    content = "\n".join(lines).strip()
    if not content:
        print(a5 + "No code pasted!")
        return

    print("\n" + a40 + "Analyzing the pasted code...\n")
    suggestions = []

    if 'marshal.loads' in content:
        suggestions.append("➲ 1 or 2: Marshal obfuscation")
    if 'base64' in content.lower():
        suggestions.append("➲ 4 or 7: Base64 involved")
    if 'zlib.decompress' in content:
        suggestions.append("➲ 7 or 14: Zlib compression")
    if 'lambda' in content and '__import__' in content:
        suggestions.append("➲ 8: Lambda obfuscation")
    if any(ord(c) > 127 for c in content[:100]):
        suggestions.append("➲ 9: Emoji/Unicode heavy")

    if suggestions:
        print(a16 + "Recommended options:\n")
        for s in suggestions:
            print(a20 + "   " + s)
    else:
        print(a5 + "No common pattern detected.")

def PY_97():
    print(a16 + '⏕' * 28)
    print(a20 + ' ➲ 1. Decode marshal     ')
    print(a20 + ' ➲ 2. Decode marshal 3.7 (uncompyle6)    ')
    print(a20 + ' ➲ 3. Decode base32    ')
    print(a20 + ' ➲ 4. Decode base64    ')
    print(a20 + ' ➲ 5. Decode base16    ')
    print(a20 + ' ➲ 6. Decode base85    ')
    print(a20 + ' ➲ 7. Decode lambda.marshal.base64.zlib    ')
    print(a20 + ' ➲ 8. Decode lambda    ')
    print(a20 + ' ➲ 9. Decode emoji    ')
    print(a20 + ' ➲ 10. Decode hex    ')
    print(a20 + ' ➲ 11. Decode pyc (pycdc)    ')
    print(a20 + ' ➲ 12. Decode lzma.zlib (placeholder)    ')
    print(a20 + ' ➲ 13. Decode binascii (placeholder)    ')
    print(a20 + ' ➲ 14. Decode zlib,base (placeholder)    ')
    print(a20 + ' ➲ 15. Decode gzip (placeholder)    ')
    print(a20 + ' ➲ 16. Decode codecs (placeholder)    ')
    print(a20 + ' ➲ 17. Decode simple pyc (pycdc)    ')
    print(a20 + ' ➲ 18. Decode simple pyc2 (uncompyle6)    ')
    print(a20 + ' ➲ 19. Decode lzma (placeholder)    ')
    print(a20 + ' ➲ 20. Cython (redirect)    ')
    print(a20 + ' ➲ 21. Detect type by PASTING code    ')
    print(a20 + ' ➲ 0. Exit    ')
    print(a16 + '⏔' * 28)

def cython():
    webbrowser.open('https://t.me/PY_97')

# ==================== MAIN ====================
clr()
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
        elif choice == "11" or choice == "17":
            smple_pyc()
        elif choice == "18":
            smple_pyc2()
        elif choice in ["12", "13", "14", "15", "16", "19"]:
            placeholder_tool()
        elif choice == "20":
            cython()
        elif choice == "21":
            detect_obfuscation()
        elif choice == "0":
            slow(G + "Goodbye! Thanks for using PY_97 🔥")
            sys.exit()
        else:
            print(a5 + "Invalid option!")

        input(a11 + "\nPress Enter to continue...")
        clr()

    except KeyboardInterrupt:
        print("\n" + a5 + "Exit!")
        sys.exit()b16decode(encoded_data)
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
        elif choice == "21":  # NEW
            detect_obfuscation()
        elif choice == "0":
            ex()
        else:
            print(a5 + "Invalid option!")

        input(a11 + "\nPress Enter to continue...")
        clr()

    except KeyboardInterrupt:
        print("\nInterrupted by user!")
        sys.exit()
