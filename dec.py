# -*- coding: utf-8 -*-
import os
import sys
import time
import base64
import marshal
import zlib
from py_compile import compile

# Warna terminal
red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1;93m'
blue = '\033[1;94m'
magenta = '\033[1;95m'
cyan = '\033[1;96m'
white = '\033[1;97m'
reset = '\033[0m'

# Fungsi untuk teks dengan animasi
def delay_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Membersihkan terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk memilih lokasi output
def choose_output_path(default_path):
    print(f"{yellow}Default output path: {default_path}{reset}")
    custom_path = input("Enter custom output path or press Enter to use default: ").strip()
    if not custom_path:
        custom_path = default_path
    try:
        # Memastikan folder output ada
        os.makedirs(os.path.dirname(custom_path), exist_ok=True)
    except Exception as e:
        print(f"{red}Error creating directory: {e}{reset}")
    return custom_path

# Fungsi Enkripsi
def encrypt_base16(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        encrypted = base64.b16encode(content.encode()).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_base16.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import base64\nexec(base64.b16decode('{encrypted}').decode())")
        print(f"{green}File encrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to encrypt: {e}{reset}")

def encrypt_base32(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        encrypted = base64.b32encode(content.encode()).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_base32.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import base64\nexec(base64.b32decode('{encrypted}').decode())")
        print(f"{green}File encrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to encrypt: {e}{reset}")

def encrypt_base64(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        encrypted = base64.b64encode(content.encode()).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_base64.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import base64\nexec(base64.b64decode('{encrypted}').decode())")
        print(f"{green}File encrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to encrypt: {e}{reset}")

def encrypt_marshal(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        compiled = compile(content, '<script>', 'exec')
        encrypted = marshal.dumps(compiled)
        default_output = f"{os.path.splitext(file_path)[0]}_enc_marshal.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import marshal\nexec(marshal.loads({repr(encrypted)}))")
        print(f"{green}File encrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to encrypt: {e}{reset}")

def encrypt_zlib(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        compressed = zlib.compress(content.encode())
        default_output = f"{os.path.splitext(file_path)[0]}_enc_zlib.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import zlib\nexec(zlib.decompress({repr(compressed)}).decode())")
        print(f"{green}File encrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to encrypt: {e}{reset}")

def encrypt_mzb(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        compiled = compile(content, '<script>', 'exec')
        encrypted = base64.b64encode(zlib.compress(marshal.dumps(compiled))).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_mzb.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode('{encrypted}'))))")
        print(f"{green}File encrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to encrypt: {e}{reset}")

# Fungsi Dekripsi
def decrypt_mzb(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        content = content.replace('exec(marshal.loads(zlib.decompress(base64.b64decode("', '').replace('"))))', '')
        decrypted = marshal.loads(zlib.decompress(base64.b64decode(content)))
        default_output = f"{os.path.splitext(file_path)[0]}_dec.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(decrypted.decode())
        print(f"{green}File decrypted and saved as {output_path}{reset}")
    except Exception as e:
        print(f"{red}Failed to decrypt: {e}{reset}")

# Menu Enkripsi
def encryption_menu():
    clear()
    print(f"{cyan}Encryptor Menu{reset}")
    print("[1] Encrypt Base16")
    print("[2] Encrypt Base32")
    print("[3] Encrypt Base64")
    print("[4] Encrypt Marshal")
    print("[5] Encrypt Zlib")
    print("[6] Encrypt Marshal + Zlib + Base64")
    print("[0] Back")
    choice = input("Choose an option: ")
    if choice == "1":
        encrypt_base16(input("Enter the file path: "))
    elif choice == "2":
        encrypt_base32(input("Enter the file path: "))
    elif choice == "3":
        encrypt_base64(input("Enter the file path: "))
    elif choice == "4":
        encrypt_marshal(input("Enter the file path: "))
    elif choice == "5":
        encrypt_zlib(input("Enter the file path: "))
    elif choice == "6":
        encrypt_mzb(input("Enter the file path: "))
    elif choice == "0":
        main_menu()
    else:
        print(f"{red}Invalid choice, try again.{reset}")
        encryption_menu()

# Menu Dekripsi
def decryption_menu():
    clear()
    print(f"{cyan}Decryptor Menu{reset}")
    print("[1] Decrypt Marshal + Zlib + Base64")
    print("[0] Back")
    choice = input("Choose an option: ")
    if choice == "1":
        decrypt_mzb(input("Enter the file path: "))
    elif choice == "0":
        main_menu()
    else:
        print(f"{red}Invalid choice, try again.{reset}")
        decryption_menu()

# Menu Utama
def main_menu():
    clear()
    print(f"{cyan}Python Encryption/Decryption Tool{reset}")
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
        print(f"{red}Invalid choice, try again.{reset}")
        main_menu()

# Eksekusi Utama
if __name__ == "__main__":
    main_menu()
