from pwn import xor

flag = bytes.fromhex('...')
for i in range(128):
    decode = (xor(flag, i))
    if b'...' in decode:
        print(f"{decode}")
