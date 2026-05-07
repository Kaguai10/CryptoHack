from Crypto.Util.number import inverse

# Curve parameters
p = 2**255 - 19
A = 486662
B = 1

# Recover y-coordinate from x-coordinate
def recover_y(x):
    rhs = (x**3 + A*x**2 + x) % p

    # Since p % 8 == 5
    y = pow(rhs, (p + 3) // 8, p)

    if (y * y) % p != rhs:
        y = (y * pow(2, (p - 1) // 4, p)) % p

    return y

# Point addition
def point_add(P, Q):
    x1, y1 = P
    x2, y2 = Q

    if P == Q:
        return point_double(P)

    alpha = ((y2 - y1) * inverse((x2 - x1) % p, p)) % p

    x3 = (B * alpha * alpha - A - x1 - x2) % p
    y3 = (alpha * (x1 - x3) - y1) % p

    return (x3, y3)

# Point doubling
def point_double(P):
    x1, y1 = P

    alpha = (
        (3 * x1 * x1 + 2 * A * x1 + 1)
        * inverse((2 * B * y1) % p, p)
    ) % p

    x3 = (B * alpha * alpha - A - 2 * x1) % p
    y3 = (alpha * (x1 - x3) - y1) % p

    return (x3, y3)

# Montgomery Binary Algorithm
def montgomery_ladder(P, k):
    bits = bin(k)[2:]

    R0 = P
    R1 = point_double(P)

    for bit in bits[1:]:
        if bit == '0':
            R1 = point_add(R0, R1)
            R0 = point_double(R0)
        else:
            R0 = point_add(R0, R1)
            R1 = point_double(R1)

    return R0

# Generator point
Gx = 9
Gy = recover_y(Gx)
G = (Gx, Gy)

# Scalar
k = 0x1337c0decafe

# Compute Q = [k]G
Q = montgomery_ladder(G, k)

print("Q.x =", Q[0])
print(f"crypto{{{Q[0]}}}")

# crypto{49231350462786016064336756977412654793383964726771892982507420921563002378152}
