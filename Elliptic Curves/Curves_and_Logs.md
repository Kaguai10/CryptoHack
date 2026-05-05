## Deskripsi Challenge

Challenge ini menggunakan konsep **Elliptic Curve Diffie-Hellman (ECDH)**. Diberikan sebuah kurva eliptik:

```text
E: y² = x³ + 497x + 1768 mod 9739
```

Dengan public key Alice:

```text
QA = (815, 3190)
```

Dan secret integer Bob:

```text
nB = 1829
```

Tujuan challenge adalah menghitung shared secret:

```text
S = [nB]QA
```

Setelah itu, ambil koordinat `x` dari hasil shared secret, ubah menjadi string, lalu hash menggunakan SHA1. Hasil hexdigest SHA1 adalah flag.

## Analisis

Pada ECDH, shared secret dapat dihitung dari private key salah satu pihak dan public key pihak lainnya. Karena private key Bob sudah diketahui, kita tidak perlu mencari private key Alice.

Maka cukup hitung:

```text
S = [1829](815, 3190)
```

Perhitungan dilakukan menggunakan operasi scalar multiplication pada elliptic curve. Operasi ini terdiri dari point addition dan point doubling dalam modulo `p = 9739`.

Dalam operasi elliptic curve, pembagian dilakukan menggunakan modular inverse. Di Python, modular inverse dapat dihitung dengan:

```python
pow(x, -1, p)
```

Solver menggunakan metode **double-and-add** agar proses scalar multiplication lebih efisien.

## Hasil Perhitungan

Setelah dilakukan scalar multiplication:

```text
S = [1829](815, 3190)
```

Didapatkan shared secret:

```text
S = (7929, 707)
```

Koordinat `x` dari shared secret adalah:

```text
7929
```

Kemudian nilai tersebut diubah menjadi string:

```text
"7929"
```

Lalu dihitung SHA1-nya:

```text
SHA1("7929") = 80e5212754a824d3a4aed185ace4f9cac0f908bf
```

## Solver
`solver.py`
```python
#!/usr/bin/env python3
import hashlib

p = 9739
a = 497
b = 1768

QA = (815, 3190)
nB = 1829


def inverse_mod(k, p):
    return pow(k, -1, p)


def point_add(P, Q):
    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = ((3 * x1 * x1 + a) * inverse_mod(2 * y1, p)) % p
    else:
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


def scalar_mult(k, P):
    result = None
    addend = P

    while k > 0:
        if k & 1:
            result = point_add(result, addend)

        addend = point_add(addend, addend)
        k >>= 1

    return result


def main():
    shared_secret = scalar_mult(nB, QA)
    x = shared_secret[0]
    flag = hashlib.sha1(str(x).encode()).hexdigest()

    print(f"Shared secret: {shared_secret}")
    print(f"x coordinate: {x}")
    print(f"Flag: {flag}")


if __name__ == "__main__":
    main()
```

Flag: `crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}`
