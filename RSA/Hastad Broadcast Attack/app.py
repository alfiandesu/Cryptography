from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot
from sympy.ntheory.modular import crt

e =   # changeable
c1 =  # changeable
n1 =  # changeable
c2 =  # changeable
n2 =  # changeable
c3 =  # changeable
n3 =  # changeable

C = [c1, c2, c3]  # changeable 
N = [n1, n2, n3]

x, _ = crt(N, C)

m, exact = iroot(int(x), e)

if exact:
    print("Plaintext:", long_to_bytes(m))
else:
    print("Root not exact")
