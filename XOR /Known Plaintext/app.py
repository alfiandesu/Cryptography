from pwn import xor

ct = bytes.fromhex('...')
partial_key = xor(ct[:<plaintext length>], b"<plaintext>")

for i in range(256):
    key = partial_key + bytes([i])
    decode = xor(ct, key)
    print(decode)
