from pwn import xor

ct = bytes.fromhex('') # changeable depends on the chall
k = b'' # changeable depends on the chall

print(xor(ct, k).decode()) #changeable depends on the chall
