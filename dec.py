# -*- coding: utf-8 -*-
import os
import sys
import time
import base64
import marshal
import zlib
from py_compile import compile

# ANSI Color Codes
colors = {
    'red': '\033[1;91m',
    'green': '\033[1;92m',
    'yellow': '\033[1;93m',
    'blue': '\033[1;94m',
    'magenta': '\033[1;95m',
    'cyan': '\033[1;96m',
    'white': '\033[1;97m',
    'reset': '\033[0m',
}

# Displaying text with delay
def delay_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Encryption Functions
def encrypt_base64(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    encrypted = base64.b64encode(content.encode()).decode()
    output_path = f"{os.path.splitext(file_path)[0]}_enc_base64.py"
    with open(output_path, 'w') as f:
        f.write(f"import base64\nexec(base64.b64decode('{encrypted}').decode())")
    print(f"File encrypted and saved as {output_path}")

def encrypt_zlib(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    compressed = zlib.compress(content.encode())
    output_path = f"{os.path.splitext(file_path)[0]}_enc_zlib.py"
    with open(output_path, 'w') as f:
        f.write(f"import zlib\nexec(zlib.decompress({repr(compressed)}).decode())")
    print(f"File encrypted and saved as {output_path}")

# Decryption Functions
def decrypt_base64(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    decrypted = base64.b64decode(content).decode()
    output_path = f"{os.path.splitext(file_path)[0]}_dec.py"
    with open(output_path, 'w') as f:
        f.write(decrypted)
    print(f"File decrypted and saved as {output_path}")

def decrypt_zlib(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    decompressed = zlib.decompress(eval(content))
    output_path = f"{os.path.splitext(file_path)[0]}_dec.py"
    with open(output_path, 'w') as f:
        f.write(decompressed.decode())
    print(f"File decrypted and saved as {output_path}")

# Menu Functions
def encryption_menu():
    clear()
    print(f"{colors['cyan']}Encryption Menu{colors['reset']}")
    print("[1] Encrypt Base64")
    print("[2] Encrypt Zlib")
    print("[0] Back")
    choice = input("Choose an option: ")
    if choice == "1":
        file_path = input("Enter the file path: ")
        encrypt_base64(file_path)
    elif choice == "2":
        file_path = input("Enter the file path: ")
        encrypt_zlib(file_path)
    elif choice == "0":
        main_menu()
    else:
        print("Invalid choice, try again.")
        encryption_menu()

def decryption_menu():
    clear()
    print(f"{colors['cyan']}Decryption Menu{colors['reset']}")
    print("[1] Decrypt Base64")
    print("[2] Decrypt Zlib")
    print("[0] Back")
    choice = input("Choose an option: ")
    if choice == "1":
        file_path = input("Enter the file path: ")
        decrypt_base64(file_path)
    elif choice == "2":
        file_path = input("Enter the file path: ")
        decrypt_zlib(file_path)
    elif choice == "0":
        main_menu()
    else:
        print("Invalid choice, try again.")
        decryption_menu()

def main_menu():
    clear()
    print(f"{colors['cyan']}Python Encryption/Decryption Tool{colors['reset']}")
    print("[1] Encryption Menu")
    print("[2] Decryption Menu")
    print("[0] Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        encryption_menu()
    elif choice == "2":
        decryption_menu()
    elif choice == "0":
        sys.exit()
    else:
        print("Invalid choice, try again.")
        main_menu()

# Main Execution
if __name__ == "__main__":
    main_menu()
