from pwn import xor

k1 = bytes.fromhex('')   # changeable, depends on the chall
k2_3 = bytes.fromhex('') # changeable, depends on the chall
ct = bytes.fromhex('')   # changeable, depends on the chall

print(xor(k1, k2_3, ct).decode)
