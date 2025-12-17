import marshal, codecs, binascii, zlib, bz2, pyfiglet, os, time, dis, lzma, gzip, base64
from sys import stdout
import subprocess as sp
import sys, random, base64, getpass, re
from py_compile import compile as py_compile_file
import webbrowser
import py_compile

webbrowser.open('https://t.me/KLM_J')
import pyfiglet

# Colors
R = '\x1b[1;31m'  # Red
G = '\x1b[1;32m'  # Green
Y = '\x1b[1;33m'  # Yellow
B = '\x1b[1;34m'  # Blue
P = '\x1b[1;35m'  # Purple
C = '\x1b[1;36m'  # Cyan
W = '\x1b[1;37m'  # White
D = '\x1b[0m'     # Default

a5 = '\x1b[38;5;208m'   # Orange
a7 = '\x1b[38;5;13m'    # Pink
a11 = '\x1b[38;5;8m'    # Gray
a16 = '\x1b[38;5;48m'   # Light Green
a20 = '\x1b[38;5;226m'  # Light Yellow
a40 = '\x1b[38;5;117m'  # Sky Blue

def clr():
    os.system("clear")

def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)

# Auto compile any .py file to .pyc
def auto_compile_pyc(py_file):
    if not os.path.exists(py_file):
        print(f"{R}[-] File {py_file} not found for compilation!{D}")
        return
    try:
        py_compile_file(py_file, doraise=True)
        basename = os.path.basename(py_file)
        print(f"{G}[+] Successfully compiled: {basename} → __pycache__/{basename}c √{D}")
    except Exception as e:
        print(f"{R}[-] Compilation failed: {e}{D}")

def PY_97():
    clr()
    print(a16 + '⏕' * 35)
    print(a20 + ' ➲ 1. Decode marshal')
    print(a20 + ' ➲ 2. Decode marshal (advanced)')
    print(a20 + ' ➲ 3. Decode base32')
    print(a20 + ' ➲ 4. Decode base64')
    print(a20 + ' ➲ 5. Decode base16 (hex)')
    print(a20 + ' ➲ 6. Decode base85')
    print(a20 + ' ➲ 7. Decode lambda.marshal.base64.zlib')
    print(a20 + ' ➲ 8. Decode lambda (exec → print)')
    print(a20 + ' ➲ 9. Decode emoji obfuscated')
    print(a20 + ' ➲ 10. Decode hex string')
    print(a20 + ' ➲ 11. Decompile .pyc (simple)')
    print(a20 + ' ➲ 12. Decode lzma + zlib + marshal')
    print(a20 + ' ➲ 13. Decode binascii (a2b)')
    print(a20 + ' ➲ 14. Decode zlib + base64 + marshal')
    print(a20 + ' ➲ 15. Decode gzip + marshal')
    print(a20 + ' ➲ 16. Decode codecs (rot13, etc.)')
    print(a20 + ' ➲ 17. Decompile pyc → py (pycdc style)')
    print(a20 + ' ➲ 18. Decompile pyc → py (uncompyle6 style)')
    print(a20 + ' ➲ 19. Decode lzma + marshal')
    print(a20 + ' ➲ 20. Cython (redirect)')
    print(a20 + ' ➲ 0. Exit')
    print(a16 + '⏔' * 35)

# Option 1: Simple marshal decode (extract and exec)
def option1():
    file = input(f"{R}[PY_97]{W} > Enter marshal file: ")
    try:
        with open(file, 'rb') as f:
            data = marshal.load(f)
        with open("decoded_marshal.py", "w") as f:
            f.write("# Decoded by PY_97\n")
            # We can't directly save source, so we wrap it
            f.write("import marshal\nexec(marshal.loads(" + repr(data) + "))")
        print(f"{G}[+] Saved as decoded_marshal.py")
        auto_compile_pyc("decoded_marshal.py")
    except Exception as e:
        print(f"{R}Error: {e}")

# Option 2: Advanced marshal (common pattern)
def option2():
    file = input(f"{R}[PY_97]{W} > Enter file: ")
    try:
        code = open(file).read()
        exec(code.replace("exec(marshal.loads(", "open('hasil.py','w').write('#Decoded by PY_97\\n'+__import__('uncompyle6').decompile.decompile(3.8, ").replace(")))", "), None)[1]"))
        print(f"{G}[+] Decompiled to hasil.py")
        auto_compile_pyc("hasil.py")
    except:
        print(f"{R}Failed. Make sure uncompyle6 is installed: pip install uncompyle6")

# Option 3-6: Base decodes
def decode_base(file_in, func, name):
    try:
        with open(file_in, 'rb') as f:
            data = func(f.read())
        out = f"decoded_{name}.py"
        with open(out, 'wb') as f:
            f.write(data)
        print(f"{G}[+] Saved as {out}")
        auto_compile_pyc(out)
    except Exception as e:
        print(f"{R}Error: {e}")

# Option 7: lambda + marshal + zlib + base64 (reversed)
def option7():
    file = input(f"{R}[PY_97]{W} > Enter file: ")
    try:
        content = open(file, 'r').read()
        # Extract the lambda part
        start = content.find("b64decode(__[::-1]"))
        if start == -1:
            print(f"{R}Pattern not found!")
            return
        b64_part = content[content.find("b'"):content.rfind("'))")]
        decoded = zlib.decompress(base64.b64decode(eval(b64_part)[::-1]))
        with open("decoded_complex.py", "wb") as f:
            f.write(decoded)
        print(f"{G}[+] Successfully decoded → decoded_complex.py")
        auto_compile_pyc("decoded_complex.py")
    except Exception as e:
        print(f"{R}Error: {e}")

# Option 8 & 9: exec → print for lambda/emoji
def replace_exec_to_print(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
        new_content = content.replace("exec(", "print(").replace("exec (", "print(")
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"{G}[+] Replaced exec → print. Now run: python {file}")
        auto_compile_pyc(file)
    except Exception as e:
        print(f"{R}Error: {e}")

# Option 10: Hex decode
def option10():
    file = input(f"{R}[PY_97]{W} > Enter hex file: ")
    try:
        with open(file, 'r') as f:
            hex_data = f.read().strip()
        bytes_data = bytes.fromhex(hex_data)
        with open("decoded_hex.py", "wb") as f:
            f.write(bytes_data)
        print(f"{G}[+] Saved as decoded_hex.py")
        auto_compile_pyc("decoded_hex.py")
    except Exception as e:
        print(f"{R}Error: {e}")

# Option 11 & 17-18: .pyc decompile (requires pycdc or uncompyle6)
def decompile_pyc(file, output):
    try:
        result = subprocess.run(['uncompyle6', file], capture_output=True, text=True)
        if result.returncode == 0:
            with open(output, 'w') as f:
                f.write(result.stdout)
            print(f"{G}[+] Decompiled to {output}")
            auto_compile_pyc(output)
        else:
            print(f"{R}Failed. Install uncompyle6: pip install uncompyle6")
    except:
        print(f"{R}uncompyle6 not available.")

# Main loop
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
        choice = input(f"\n{a7}[PY_97] ➜ Select: {W}")

        if choice == "1": option1()
        elif choice == "2": option2()
        elif choice == "3": decode_base(input("Enter base32 file: "), base64.b32decode, "base32")
        elif choice == "4": decode_base(input("Enter base64 file: "), base64.b64decode, "base64")
        elif choice == "5": decode_base(input("Enter base16 file: "), base64.b16decode, "base16")
        elif choice == "6": decode_base(input("Enter base85 file: "), base64.b85decode, "base85")
        elif choice == "7": option7()
        elif choice == "8": replace_exec_to_print(input("Enter lambda file: "))
        elif choice == "9": replace_exec_to_print(input("Enter emoji file: "))
        elif choice == "10": option10()
        elif choice in ["11", "17", "18"]:
            f = input("Enter .pyc file: ")
            decompile_pyc(f, "decompiled.py")
        elif choice == "12":
            # lzma + zlib + marshal
            try:
                file = input("Enter file: ")
                data = open(file,'rb').read()
                data = marshal.loads(zlib.decompress(lzma.decompress(data)))
                with open("decoded_lzma_zlib.py","wb") as f: f.write(data)
                print(f"{G}[+] Saved as decoded_lzma_zlib.py")
                auto_compile_pyc("decoded_lzma_zlib.py")
            except: print(f"{R}Failed decode")
        elif choice == "13":
            try:
                file = input("Enter file: ")
                code = open(file).read()
                decoded = binascii.a2b_uu(code) or binascii.a2b_base64(code) or binascii.a2b_hex(code)
                open("decoded_binascii.py","wb").write(decoded)
                auto_compile_pyc("decoded_binascii.py")
            except: print(f"{R}Failed")
        elif choice == "14":  # zlib + base64 + marshal
            try:
                file = input("Enter file: ")
                data = marshal.loads(zlib.decompress(base64.b64decode(open(file,'rb').read())))
                open("decoded_zlib_base.py","wb").write(data)
                print(f"{G}[+] Done → decoded_zlib_base.py")
                auto_compile_pyc("decoded_zlib_base.py")
            except: print(f"{R}Failed")
        elif choice == "15":  # gzip
            try:
                file = input("Enter gzip file: ")
                data = gzip.decompress(open(file,'rb').read())
                open("decoded_gzip.py","wb").write(data)
                auto_compile_pyc("decoded_gzip.py")
            except: print(f"{R}Failed")
        elif choice == "16":  # codecs (rot13 common)
            try:
                file = input("Enter file: ")
                code = open(file).read()
                decoded = codecs.decode(code, 'rot13')
                open("decoded_codecs.py","w").write(decoded)
                auto_compile_pyc("decoded_codecs.py")
            except: print(f"{R}Failed")
        elif choice == "19":
            try:
                file = input("Enter lzma file: ")
                data = marshal.loads(lzma.decompress(open(file,'rb').read()))
                open("decoded_lzma.py","wb").write(data)
                auto_compile_pyc("decoded_lzma.py")
            except: print(f"{R}Failed")
        elif choice == "20":
            webbrowser.open('https://t.me/PY_97')
        elif choice == "0":
            slow(f"{G}Goodbye! Thanks for using PY_97 ~ @GlitchbyAnne")
            exit()
        else:
            print(f"{R}Invalid option!")

        input(f"\n{a11}Press Enter to continue...{D}")
        clr()

    except KeyboardInterrupt:
        print(f"\n{G}Exited by user.{D}")
        break
    except Exception as e:
        print(f"{R}Unexpected error: {e}{D}")
        input("Press Enter...")
