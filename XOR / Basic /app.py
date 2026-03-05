from pwn import xor

ct = bytes.fromhex('...')
k = b'...' 

print(xor(ct, k).decode())
