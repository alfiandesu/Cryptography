from Crypto.Util.number import long_to_bytes

c1 = ...
c2 = ...
e1 = ...
e2 = ...
n = ...

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def common_modulus_attack(c1, c2, e1, e2, n):
    g, s1, s2 = extended_gcd(e1, e2)

    if g != 1:
        raise ValueError("e1 and e2 not coprime")

    if s1 < 0:
        c1 = pow(c1, -1, n)
        s1 = -s1
    if s2 < 0:
        c2 = pow(c2, -1, n)
        s2 = -s2

    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return m

m = common_modulus_attack(c1, c2, e1, e2, n)
print(f"Result: {long_to_bytes(m)}")
