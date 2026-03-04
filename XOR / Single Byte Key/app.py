from pwn import xor

flag = bytes.fromhex('') # changable depends on the chall
for i in range(128):
    decode = (xor(flag, i))
    if b'' in decode: # changeable depends on the chall
        print(f"{decode}")
