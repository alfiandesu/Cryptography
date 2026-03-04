from pwn import xor

ct = bytes.fromhex('') # changeable depends on the chall
partial_key = xor(ct[:<plaintext length>], b"<plaintext>") # changeable depends on the chall

for i in range(256):
    key = partial_key + bytes([i])
    decode = xor(ct, key)
    print(decode)
