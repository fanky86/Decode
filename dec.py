import marshal, base64

encoded_data = "..."  # Ganti dengan string encoded di script Anda
decoded_data = marshal.loads(base64.b64decode(encoded_data))

with open("decoded_script.py", "w") as f:
    f.write(decoded_data)