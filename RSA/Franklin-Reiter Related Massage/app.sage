from Crypto.Util.number import long_to_bytes
from math import gcd

n  = ...
e  = ...
c1 = ...
c2 = ...
a  = 1    # m2 = a*m1 + b
b  = ...

R = Zmod(n)['x']
x = R.gen()

f1 = x**e - c1
f2 = (a*x + b)**e - c2

def poly_gcd(f, g):
    while g:
        f, g = g, f % g
    return f.monic()

g = poly_gcd(f1, f2)
m1 = int(-g[0]) % n
print(long_to_bytes(m1))
