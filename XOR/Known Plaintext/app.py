from pwn import xor

ct = bytes.fromhex('') # changable depends on the chall 
partial_key = xor(ct[:<plaintext length>], b"<plaintext>")  #changable depends on the chall

for i in range(256):
    key = partial_key + bytes([i])
    decode = xor(ct, key)
    print(decode)
