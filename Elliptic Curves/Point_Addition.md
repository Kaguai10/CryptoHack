## Deskripsi Soal
Diberikan elliptic curve pada finite field:

E: y^2 = x^3 + 497x + 1768 (mod 9739)

Titik yang diberikan:
- P = (493, 5564)
- Q = (1539, 4742)
- R = (4403, 5202)

Ditanya:
S = P + P + Q + R

---

## Dasar Teori

Untuk dua titik P(x1, y1) dan Q(x2, y2):

Jika P ≠ Q:
λ = (y2 - y1) * (x2 - x1)^(-1) mod p

Jika P = Q:
λ = (3x1^2 + a) * (2y1)^(-1) mod p

Koordinat hasil:
x3 = λ^2 - x1 - x2 mod p  
y3 = λ(x1 - x3) - y1 mod p  

---

## Langkah Penyelesaian

### 1. Hitung A = P + P
A = (2130, 2999)

### 2. Hitung B = A + Q
B = (7025, 7144)

### 3. Hitung S = B + R
S = (4215, 2162)

---

## Verifikasi

Substitusi ke kurva:
y^2 ≡ x^3 + 497x + 1768 (mod 9739)

Titik valid.

---

## Solver
`solver.py`
```python
# Elliptic Curve Parameters
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
```

Flag: crypto{4215, 2162}
