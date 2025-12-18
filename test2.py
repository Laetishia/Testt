import marshal
import dis
import py_compile
import importlib.util
import importlib._bootstrap_external as _bootstrap
import struct
import os
import sys

MAGIC = importlib.util.MAGIC_NUMBER


# ---------- FILE TYPE DETECTION ----------

def is_pyc(path):
    try:
        with open(path, "rb") as f:
            return f.read(4) == MAGIC
    except:
        return False


def is_py(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            f.read(512)
        return path.endswith(".py")
    except:
        return False


def is_marshal(path):
    if is_pyc(path):  # IMPORTANT: prevent false positives
        return False
    try:
        with open(path, "rb") as f:
            marshal.loads(f.read())
        return True
    except:
        return False


def detect_type(path):
    if is_pyc(path):
        return "PYC"
    if is_py(path):
        return "PY"
    if is_marshal(path):
        return "MARSHAL"
    return "UNKNOWN"


# ---------- LOAD CODE OBJECT ----------

def load_code(path, ftype):
    if ftype == "PYC":
        with open(path, "rb") as f:
            data = f.read()

        # Use CPython's internal pyc loader (correct for all versions)
        return _bootstrap._code_to_timestamp_pyc(data, path)[0]

    if ftype == "MARSHAL":
        with open(path, "rb") as f:
            return marshal.loads(f.read())

    if ftype == "PY":
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()
        return compile(source, path, "exec")

    raise ValueError("Unsupported file type")


# ---------- ACTIONS ----------

def execute_code(code):
    print("\n[+] EXECUTING FILE\n")
    exec(code, {})


def disassemble_code(code):
    print("\n[+] BYTECODE DISASSEMBLY\n")
    dis.dis(code)


def py_to_pyc(path):
    out = path + "c"
    py_compile.compile(path, cfile=out, doraise=True)
    print(f"[+] PY → PYC saved as: {out}")


def marshal_to_pyc(path, code):
    out = path + ".pyc"
    header = _bootstrap._code_to_timestamp_pyc(
        marshal.dumps(code),
        0,
        0
    )
    with open(out, "wb") as f:
        f.write(header)
    print(f"[+] MARSHAL → PYC saved as: {out}")


# ---------- INTERACTIVE MENU ----------

def menu():
    print("\n=== ACTION MENU ===")
    print("1) Detect file type")
    print("2) Execute file")
    print("3) Convert to PYC")
    print("4) Disassemble")
    print("5) Load another file")
    print("6) Exit")


def normalize_path(p):
    p = p.strip()
    if p.lower().startswith("sdcard/"):
        p = "/" + p
    return os.path.abspath(p)


def main():
    print("=== PYTHON AUTO FILE TOOL ===")
    print("(Supports very large files, PYC, marshal, PY)")

    while True:
        user_input = input("\nEnter file path: ").strip()
        if not user_input:
            continue

        path = normalize_path(user_input)

        if not os.path.isfile(path):
            print("[-] File not found")
            continue

        while True:
            ftype = detect_type(path)

            try:
                code = load_code(path, ftype)
            except Exception as e:
                print("[-] Load failed:", e)
                break

            menu()
            choice = input("Select option: ").strip()

            if choice == "1":
                print(f"[✓] Detected file type: {ftype}")

            elif choice == "2":
                execute_code(code)

            elif choice == "3":
                if ftype == "PY":
                    py_to_pyc(path)
                elif ftype == "MARSHAL":
                    marshal_to_pyc(path, code)
                else:
                    print("[-] Conversion not supported")

            elif choice == "4":
                disassemble_code(code)

            elif choice == "5":
                break

            elif choice == "6":
                print("Bye 👋")
                sys.exit(0)

            else:
                print("Invalid option")


if __name__ == "__main__":
    main()
⠿⠿⢿⡅⠀
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
