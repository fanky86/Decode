# -*- coding: utf-8 -*-
import os
import sys
import time
import base64
import marshal
import zlib
from rich.console import Console
from rich.panel import Panel

# Warna terminal
console = Console()

# Header untuk file hasil enkripsi/dekripsi
HEADER = """# MR.ExceFaN
# ngapain bang ke sini
# mau recode hahaha
# usaha bang, btw follow github gw => MR.ExceFaN
# https://github.com/fanky86/Decode\n\n"""

# Fungsi untuk teks dengan animasi
def delay_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Membersihkan terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk memindahkan file hasil
def move_file(file_path):
    try:
        new_location = console.input("[cyan]• Masukkan direktori tujuan (Enter untuk tetap di lokasi saat ini): [/cyan]")
        if new_location.strip():
            os.makedirs(new_location, exist_ok=True)
            new_path = os.path.join(new_location, os.path.basename(file_path))
            os.rename(file_path, new_path)
            console.print(Panel(f"File berhasil dipindahkan ke [green]{new_location}[/green]", title="Sukses", style="green"))
        else:
            console.print(Panel("File tetap disimpan di lokasi saat ini", title="Info", style="cyan"))
    except Exception as e:
        console.print(Panel(f"Gagal memindahkan file: {e}", title="Error", style="red"))

# Fungsi Enkripsi Base16
def encrypt_base16():
    file = console.input("[cyan]• Masukkan nama file untuk dienkripsi (Base16): [/cyan]")
    fileout = console.input("[cyan]• Masukkan nama file output: [/cyan]")
    console.print(Panel("Sedang mengenkripsi file ...", title="Processing", style="yellow"))
    try:
        with open(file, 'r') as f:
            content = f.read()
        encrypted = base64.b16encode(content.encode()).decode()
        with open(fileout, 'w') as f_out:
            f_out.write(HEADER + f"import base64\nexec(base64.b16decode('{encrypted}').decode())")
        console.print(Panel(f"File berhasil dienkripsi ke [green]{fileout}[/green]", title="Sukses", style="green"))
        move_file(fileout)
    except Exception as e:
        console.print(Panel(f"Gagal mengenkripsi file: {e}", title="Error", style="red"))

# Fungsi Enkripsi Base32
def encrypt_base32():
    file = console.input("[cyan]• Masukkan nama file untuk dienkripsi (Base32): [/cyan]")
    fileout = console.input("[cyan]• Masukkan nama file output: [/cyan]")
    console.print(Panel("Sedang mengenkripsi file ...", title="Processing", style="yellow"))
    try:
        with open(file, 'r') as f:
            content = f.read()
        encrypted = base64.b32encode(content.encode()).decode()
        with open(fileout, 'w') as f_out:
            f_out.write(HEADER + f"import base64\nexec(base64.b32decode('{encrypted}').decode())")
        console.print(Panel(f"File berhasil dienkripsi ke [green]{fileout}[/green]", title="Sukses", style="green"))
        move_file(fileout)
    except Exception as e:
        console.print(Panel(f"Gagal mengenkripsi file: {e}", title="Error", style="red"))

# Fungsi Enkripsi Base64
def encrypt_base64():
    file = console.input("[cyan]• Masukkan nama file untuk dienkripsi (Base64): [/cyan]")
    fileout = console.input("[cyan]• Masukkan nama file output: [/cyan]")
    console.print(Panel("Sedang mengenkripsi file ...", title="Processing", style="yellow"))
    try:
        with open(file, 'r') as f:
            content = f.read()
        encrypted = base64.b64encode(content.encode()).decode()
        with open(fileout, 'w') as f_out:
            f_out.write(HEADER + f"import base64\nexec(base64.b64decode('{encrypted}').decode())")
        console.print(Panel(f"File berhasil dienkripsi ke [green]{fileout}[/green]", title="Sukses", style="green"))
        move_file(fileout)
    except Exception as e:
        console.print(Panel(f"Gagal mengenkripsi file: {e}", title="Error", style="red"))

# Fungsi Enkripsi Zlib
def encrypt_zlib():
    file = console.input("[cyan]• Masukkan nama file untuk dienkripsi (Zlib): [/cyan]")
    fileout = console.input("[cyan]• Masukkan nama file output: [/cyan]")
    console.print(Panel("Sedang mengenkripsi file ...", title="Processing", style="yellow"))
    try:
        with open(file, 'r') as f:
            content = f.read()
        compressed = zlib.compress(content.encode())
        with open(fileout, 'w') as f_out:
            f_out.write(HEADER + f"import zlib\nexec(zlib.decompress({repr(compressed)}).decode())")
        console.print(Panel(f"File berhasil dienkripsi ke [green]{fileout}[/green]", title="Sukses", style="green"))
        move_file(fileout)
    except Exception as e:
        console.print(Panel(f"Gagal mengenkripsi file: {e}", title="Error", style="red"))

# Fungsi Enkripsi Marshal + Zlib + Base64
def encrypt_mzb():
    file = console.input("[cyan]• Masukkan nama file untuk dienkripsi (Marshal + Zlib + Base64): [/cyan]")
    fileout = console.input("[cyan]• Masukkan nama file output: [/cyan]")
    console.print(Panel("Sedang mengenkripsi file ...", title="Processing", style="yellow"))
    try:
        with open(file, 'r') as f:
            content = f.read()
        compiled = compile(content, "dg", "exec")
        marshaled = marshal.dumps(compiled)
        compressed = zlib.compress(marshaled)
        encoded = base64.b64encode(compressed).decode()
        with open(fileout, 'w') as f_out:
            f_out.write(HEADER + f"import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode('{encoded}'))))")
        console.print(Panel(f"File berhasil dienkripsi ke [green]{fileout}[/green]", title="Sukses", style="green"))
        move_file(fileout)
    except Exception as e:
        console.print(Panel(f"Gagal mengenkripsi file: {e}", title="Error", style="red"))

# Fungsi Dekripsi Marshal + Zlib + Base64
def decrypt_mzb():
    file = console.input("[cyan]• Masukkan nama file untuk didekripsi (Marshal + Zlib + Base64): [/cyan]")
    fileout = console.input("[cyan]• Masukkan nama file output: [/cyan]")
    console.print(Panel("Sedang mendekripsi file ...", title="Processing", style="yellow"))
    try:
        with open(file, 'r') as f:
            content = f.read().replace('exec(marshal.loads(zlib.decompress(base64.b64decode("', '').replace('"))))', '')
        decrypted = marshal.loads(zlib.decompress(base64.b64decode(content)))
        with open(fileout, 'w') as f_out:
            f_out.write(HEADER + decrypted.decode())
        console.print(Panel(f"File berhasil didekripsi ke [green]{fileout}[/green]", title="Sukses", style="green"))
        move_file(fileout)
    except Exception as e:
        console.print(Panel(f"Gagal mendekripsi file: {e}", title="Error", style="red"))

# Fungsi Menu Enkripsi
def encryption_menu():
    clear()
    console.print(Panel("Encryptor Menu\n\n[1] Encrypt Base16\n[2] Encrypt Base32\n[3] Encrypt Base64\n[4] Encrypt Marshal\n[5] Encrypt Zlib\n[6] Encrypt Marshal + Zlib + Base64\n[0] Kembali", title="Menu", style="cyan"))
    choice = console.input("[cyan]• Pilih opsi: [/cyan]")
    if choice == "1":
        encrypt_base16()
    elif choice == "2":
        encrypt_base32()
    elif choice == "3":
        encrypt_base64()
    elif choice == "4":
        encmarshal()
    elif choice == "5":
        encrypt_zlib()
    elif choice == "6":
        encrypt_mzb()
    elif choice == "0":
        main_menu()
    else:
        console.print(Panel("Opsi tidak valid, coba lagi.", title="Error", style="red"))
        encryption_menu()

# Fungsi Menu Dekripsi
def decryption_menu():
    clear()
    console.print(Panel("Decryptor Menu\n\n[1] Decrypt Base16\n[2] Decrypt Base32\n[3] Decrypt Base64\n[4] Decrypt Zlib\n[5] Decrypt Marshal\n[6] Decrypt Marshal + Zlib + Base64\n[0] Kembali", title="Menu", style="cyan"))
    choice = console.input("[cyan]• Pilih opsi: [/cyan]")
    if choice == "1":
        decrypt_base16()
    elif choice == "2":
        decrypt_base32()
    elif choice == "3":
        decrypt_base64()
    elif choice == "4":
        decrypt_zlib()
    elif choice == "5":
        decmarshal()
    elif choice == "6":
        decrypt_mzb()
    elif choice == "0":
        main_menu()
    else:
        console.print(Panel("Opsi tidak valid, coba lagi.", title="Error", style="red"))
        decryption_menu()

# Fungsi Utama
def main_menu():
    clear()
    console.print(Panel("Python Encryption/Decryption Tool\n\n[1] Encryption Menu\n[2] Decryption Menu\n[0] Exit", title="Welcome", style="cyan"))
    choice = console.input("[cyan]• Pilih opsi: [/cyan]")
    if choice == "1":
        encryption_menu()
    elif choice == "2":
        decryption_menu()
    elif choice == "0":
        sys.exit()
    else:
        console.print(Panel("Opsi tidak valid, coba lagi.", title="Error", style="red"))
        main_menu()

# Eksekusi Utama
if __name__ == "__main__":
    main_menu()
