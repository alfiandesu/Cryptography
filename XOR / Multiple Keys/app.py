from pwn import xor

k1 = bytes.fromhex('')
k2_3 = bytes.fromhex('')
ct = bytes.fromhex('')

print(xor(k1, k2_3, ct).decode)
