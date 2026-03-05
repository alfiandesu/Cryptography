from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot
from sympy.ntheory.modular import crt

e = 
c1 = 
n1 = 
c2 = 
n2 = 
c3 = 
n3 = 


def third_root(n):
    m, valid = iroot(n, e)
    if valid:
        print("Plaintext :", long_to_bytes(m))
    else:
        print("Unable to find the third root of :", n)

C = [c1, c2, c3]
N = [n1, n2, n3]

for c in C:
    third_root(c)

x, modulus_total = crt(N, C) 

print("Found CRT")
third_root(int(x))
