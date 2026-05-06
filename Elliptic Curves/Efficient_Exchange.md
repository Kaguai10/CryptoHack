## Soal
Diberikan sebuah kurva eliptik sebagai berikut:

E: y² = x³ + 497x + 1768 mod 9739
G: (1804, 5368)

Alice mengirimkan nilai berikut:

x(QA) = 4726

Diketahui bahwa kunci privat milik Bob adalah:

nB = 6534

Cipher yang diberikan adalah:

{
  "iv": "cd9da9f1c60925922377ea952afc212c",
  "encrypted_flag": "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"
}

## Solver

`Shared_Secret.py`
```python
p = 9739
a = 497
b = 1768

def inv(n): 
    return pow(n, -1, p)

def add(P, Q):
    if P == (None, None): return Q
    if Q == (None, None): return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:
        return (None, None)

    if P == Q:
        m = (3*x1*x1 + a) * inv(2*y1) % p
    else:
        m = (y2 - y1) * inv(x2 - x1) % p

    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p
    return (x3, y3)

def mul(k, P):
    R = (None, None)
    while k:
        if k & 1:
            R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R

# cari y dari x = 4726
x = 4726
for y in range(p):
    if (y*y - (x**3 + a*x + b)) % p == 0:
        QA = (x, y)
        break

S = mul(6534, QA)
print(S)
print("shared_secret =", S[0])
```

`decript.py`
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


shared_secret = 1791
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))
```

Flag: `crypto{3ff1c1ent_k3y_3xch4ng3}`
