from Crypto.Util.number import long_to_bytes

n  = ...
e  = ...
c1 = ...
c2 = ...

def short_pad_attack(c1, c2, e, n):
    R.<x, y> = Zmod(n)[]

    f1 = x**e - c1
    f2 = (x + y)**e - c2

    res = f1.resultant(f2, x)
    
    Zy.<y> = Zmod(n)[]
    res = Zy(res)
    roots = res.roots()
    
    return [int(r) for r, _ in roots]

rs = short_pad_attack(c1, c2, e, n)

for r in rs:
    R.<x> = Zmod(n)[]
    f1 = x**e - c1
    f2 = (x + r)**e - c2
    
    def poly_gcd(f, g):
        while g: f, g = g, f % g
        return f.monic()
    
    g = poly_gcd(f1, f2)
    if g.degree() == 1:
        m1 = int(-g[0]) % n
        print(long_to_bytes(m1))
