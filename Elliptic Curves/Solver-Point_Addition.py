p = 9739
a = 497

O = None  # Point at infinity


# Modular inverse
def inv_mod(x, p):
    return pow(x, -1, p)


# Point addition
def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P)
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # P != Q
    if P != Q:
        lam = ((y2 - y1) * inv_mod(x2 - x1, p)) % p
    else:
        # Doubling
        lam = ((3 * x1 * x1 + a) * inv_mod(2 * y1, p)) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


# Given points
P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

# S = P + P + Q + R
A = point_add(P, P)
B = point_add(A, Q)
S = point_add(B, R)

print("S =", S)

# Flag: crypto{4215, 2162}
