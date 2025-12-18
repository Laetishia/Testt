import marshal
import dis
import py_compile
import importlib.util
import struct
import os

MAGIC = importlib.util.MAGIC_NUMBER


# ---------- FILE TYPE DETECTION ----------

def is_pyc(path):
    try:
        with open(path, "rb") as f:
            return f.read(len(MAGIC)) == MAGIC  # Safer length check
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


# ---------- LOAD CODE OBJECT ----------

def load_code(path, ftype):
    if ftype == "PYC":
        with open(path, "rb") as f:
            f.seek(16)  # Skip standard pyc header (more reliable than read(16))
            return marshal.loads(f.read())

    if ftype == "MARSHAL":
        with open(path, "rb") as f:
            return marshal.loads(f.read())

    if ftype == "PY":
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()
        return compile(source, path, "exec")

    raise ValueError("Unsupported file")


# ---------- ACTIONS ----------

def execute_code(code):
    print("\n[+] EXECUTING FILE\n")
    exec(code, {})


def disassemble_code(code):
    print("\n[+] BYTECODE DISASSEMBLY (READABLE)\n")
    dis.dis(code)


def py_to_pyc(path):
    out = path + "c"
    py_compile.compile(path, cfile=out, doraise=True)
    print(f"[+] PY → PYC saved as: {out}")


def marshal_to_pyc(path, code):
    out = path + ".pyc"
    with open(out, "wb") as f:
        f.write(MAGIC)
        f.write(struct.pack("<I", 0))  # Timestamp 0 (little-endian, standard)
        f.write(struct.pack("<I", 0))  # Size 0 (optional in newer Python)
        f.write(marshal.dumps(code))
    print(f"[+] MARSHAL → PYC saved as: {out}")


# ---------- INTERACTIVE MENU ----------

def menu():
    print("\n=== ACTION MENU ===")
    print("1) Detect file type")
    print("2) Execute file")
    print("3) Convert to PYC")
    print("4) Disassemble (readable)")
    print("5) Load another file")
    print("6) Exit")


def normalize_path(user_input):
    """Helper to make Android paths easier: auto-add /sdcard/ if input looks relative and starts with 'sdcard/'"""
    path = user_input.strip()
    if path.lower().startswith("sdcard/"):
        path = "/" + path
    return os.path.abspath(path)  # Expand and normalize


def main():
    print("=== PYTHON AUTO FILE TOOL ===")
    print("(Tip: Use full paths like /sdcard/filename.py or just sdcard/filename.py)")

    while True:
        user_input = input("\nEnter file path: ").strip()
        if not user_input:
            continue

        path = normalize_path(user_input)

        if not os.path.isfile(path):
            print("[-] File not found. Try with /sdcard/ prefix.")
            continue

        while True:
            ftype = detect_type(path)

            try:
                code = load_code(path, ftype)
            except Exception as e:
                print("[-] Failed to load file:", e)
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
                elif ftype == "PYC":
                    print("[-] Already a PYC file")
                else:
                    print("[-] Conversion not supported")

            elif choice == "4":
                disassemble_code(code)

            elif choice == "5":
                break

            elif choice == "6":
                print("Bye 👋")
                return

            else:
                print("Invalid option")


if __name__ == "__main__":
    main()
