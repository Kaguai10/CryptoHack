# Elliptic Curve Parameters
p = 9739

# Point P
P = (8045, 6936)

# Inverse point: (x, -y mod p)
Q = (P[0], (-P[1]) % p)

print("Q =", Q)

# crypto{8045, 2803}
