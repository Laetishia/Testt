import marshal, codecs, binascii, zlib, bz2, pyfiglet, os, time, dis, lzma, gzip, base64
from sys import stdout
import subprocess as sp
import sys, random, base64, getpass, re
from py_compile import compile as py_compile_file
import webbrowser
webbrowser.open('https://t.me/KLM_J')
from rich.panel import Panel as nel
from rich import print as cetak
import pyfiglet, requests, subprocess

# Colors
a20 = '\x1b[38;5;226m'  # Light Yellow
a16 = '\x1b[38;5;48m'   # Light Green
a5 = '\x1b[38;5;208m'   # Orange
a7 = '\x1b[38;5;13m'    # Pink
a9 = '\x1b[1;37m'       # White
a11 = '\x1b[38;5;8m'    # Gray
a12 = '\x1b[38;5;220m'  # Gold
a40 = '\x1b[38;5;117m'  # Sky Blue
G = '\x1b[1;32m'        # Green

# Phone storage path (works on Termux/Android)
STORAGE_PATH = "/sdcard/PY_97_Decoded"  # Folder in your phone's internal storage

# Create the folder if it doesn't exist
if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH)
    print(f"[+] Created folder: {STORAGE_PATH}")

def clr():
    os.system("clear")

def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)

# Auto save .py and compile to .pyc in phone storage
def save_and_compile(py_content, filename):
    py_path = os.path.join(STORAGE_PATH, filename)
    pyc_path = py_path + "c"
    
    try:
        with open(py_path, "w", encoding="utf-8") as f:
            f.write(py_content)
        print(f"[+] Saved source: {py_path}")
        
        py_compile_file(py_path, pyc_path, doraise=True)
        print(f"[+] Compiled to .pyc: {pyc_path}")
        print(f"[✔] Both files saved in your phone storage!\n     Open File Manager → Internal Storage → PY_97_Decoded")
    except Exception as e:
        print(f"[-] Error saving/compiling: {e}")

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

# === All functions updated to save directly to phone storage ===

def ahm():
    b = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File marshal : ")
    for i in range(50):
        time.sleep(0.05)
        sys.stdout.write('\rDecoding marshal...')
        sys.stdout.flush()
    print()
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
            k += a[n+1]
        n += 1
    k += "'"
    k = "b'" + k
    code = f"exec(marshal.loads({k}))"
    exec(code)  # Runs original code
    # No source saved here (exec only)

def unmarszlib():
    files = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File marshal 3.7: ")
    bk = open(files, "r").read()
    bk = bk.replace("import", "import uncompyle6,")
    bk = bk.replace("exec(", "uncompyle6.main.decompile(3.7,")
    bk = bk.replace(")))", ")),open(\"/tmp/temp_hasil.py\",\"w\"))")
    exec(bk)
    if os.path.exists("/tmp/temp_hasil.py"):
        content = open("/tmp/temp_hasil.py").read()
        save_and_compile(content, "decoded_marshal37.py")
        os.remove("/tmp/temp_hasil.py")

def men():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File : ")
    ogge = open(file).read()
    data = ogge.replace("_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b", "_ =")
    data2 = f"""import base64\nimport zlib\n{data}\ny = _[::-1]\nd = base64.b64decode(y)\nb = zlib.decompress(d)\nprint(b)"""
    open("/tmp/temp.py", "w").write(data2)
    os.system("python /tmp/temp.py > /tmp/marshal_data.py")
    final_code = f"# Decoded by PY_97\nimport marshal\nexec(marshal.loads({open('/tmp/marshal_data.py').read()}))"
    save_and_compile(final_code, "decoded_lambda_marshal.py")
    print('[•] Decode Done √')
    for f in ["/tmp/temp.py", "/tmp/marshal_data.py"]:
        if os.path.exists(f): os.remove(f)

# Base decodes
def decode_base64_file():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File base64: ")
    decoded = base64.b64decode(open(file, "rb").read())
    save_and_compile(decoded.decode('utf-8', errors='ignore'), "decoded_base64.py")

def decode_base32_file():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File base32: ")
    decoded = base64.b32decode(open(file, "rb").read())
    save_and_compile(decoded.decode('utf-8', errors='ignore'), "decoded_base32.py")

def decode_base16_file():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File base16: ")
    decoded = base64.b16decode(open(file, "rb").read())
    save_and_compile(decoded.decode('utf-8', errors='ignore'), "decoded_base16.py")

def decode_base85_file():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File base85: ")
    decoded = base64.b85decode(open(file, "rb").read())
    save_and_compile(decoded.decode('utf-8', errors='ignore'), "decoded_base85.py")

def decode_hex():
    file = input("Enter hex encoded file: ")
    decoded = bytes.fromhex(open(file, "rb").read().hex())
    save_and_compile(decoded.decode('utf-8', errors='ignore'), "decoded_hex.py")

# Lambda & Emoji
def lamb():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File Lambda: ")
    content = open(file).read().replace("exec", "print")
    open(file, "w").write(content)
    os.system(f"python3 {file}")
    save_and_compile(open(file).read(), "decoded_lambda_final.py")

def emoji():
    file = input("\x1b[1;31m[PY_97] \033[1;97m> Enter File emoji: ")
    content = open(file).read().replace("exec", "print")
    open(file, "w").write(content)
    os.system(f"python3 {file}")
    save_and_compile(open(file).read(), "decoded_emoji_final.py")

# Marshal-magic based decodes
def run_marshal_magic(input_file, output_name):
    output_py = os.path.join(STORAGE_PATH, output_name)
    cmd = f"marshal-magic '{input_file}' -o '{output_py}'"
    os.system(cmd)
    slow(G + '  by @U_G_GU    *_*')
    if os.path.exists(output_py):
        auto_compile(output_py)  # Extra compile just in case

def auto_compile(py_file):
    if py_file.endswith(".py"):
        pyc = py_file + "c"
        try:
            py_compile_file(py_file, pyc, doraise=True)
            print(f"[+] Extra .pyc created: {pyc}")
        except: pass

# Simple pyc decompilers
def smple_pyc():
    inp = input(a9 + 'Input .pyc file: ')
    out = os.path.join(STORAGE_PATH, "decompiled_pycdc.py")
    os.system(f"pycdc '{inp}' > '{out}'")
    slow(G + '  by @U_G_GU  *_*')
    auto_compile(out)

def smple_pyc2():
    inp = input('Input .pyc file: ')
    out = os.path.join(STORAGE_PATH, "decompiled_uncompyle.py")
    os.system(f"uncompyle6 '{inp}' > '{out}'")
    slow('  by @U_G_GU  *_*')
    auto_compile(out)

# Placeholder for marshal-magic options
def lzm_zlb(): run_marshal_magic(input(a9 + 'Input file: '), "decoded_lzma_zlib.py")
def binasci(): run_marshal_magic(input(a9 + 'Input file: '), "decoded_binascii.py")
def zlib_base(): run_marshal_magic(input(a9 + 'Input file: '), "decoded_zlib_base.py")
def gzp(): run_marshal_magic(input(a9 + 'Input file: '), "decoded_gzip.py")
def cods(): run_marshal_magic(input(a9 + 'Input file: '), "decoded_codecs.py")
def lzm(): run_marshal_magic(input(a9 + 'Input file: '), "decoded_lzma.py")

def cython():
    webbrowser.open('https://t.me/PY_97')
    lzm()

def ex():
    print('Goodbye! Files saved in /sdcard/PY_97_Decoded')
    sys.exit()

# Banner
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
print(a7 + "\n         All decoded files saved to your phone storage!\n         → Internal Storage → PY_97_Decoded\n")

while True:
    try:
        PY_97()
        choice = input(f"\n{a7}[ PY_97 ] ➜ Select : ")

        if choice == "1": ahm()
        elif choice == "2": unmarszlib()
        elif choice == "3": decode_base32_file()
        elif choice == "4": decode_base64_file()
        elif choice == "5": decode_base16_file()
        elif choice == "6": decode_base85_file()
        elif choice == "7": men()
        elif choice == "8": lamb()
        elif choice == "9": emoji()
        elif choice == "10": decode_hex()
        elif choice == "11": smple_pyc()
        elif choice == "12": lzm_zlb()
        elif choice == "13": binasci()
        elif choice == "14": zlib_base()
        elif choice == "15": gzp()
        elif choice == "16": cods()
        elif choice == "17": smple_pyc()
        elif choice == "18": smple_pyc2()
        elif choice == "19": lzm()
        elif choice == "20": cython()
        elif choice == "0": ex()
        else: print(a5 + "Invalid option!")

        input(a11 + "\nPress Enter to continue...")
        clr()

    except KeyboardInterrupt:
        print("\nGoodbye! Check your phone storage → PY_97_Decoded folder")
        sys.exit()
