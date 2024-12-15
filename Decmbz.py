import marshal, base64, zlib

# Ganti "payload" dengan data string terenkripsi
payload = input('masukan payload b"...: ')

try:
    decoded = marshal.loads(payload)
    print(decoded)
except:
    try:
        decoded = base64.b64decode(payload)
        print(decoded)
    except:
        print("Tidak bisa didekode.")
