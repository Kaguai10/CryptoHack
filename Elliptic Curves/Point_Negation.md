## Point Negation

### Deskripsi
Diberikan elliptic curve:

```
E: y^2 = x^3 + 497x + 1768 (mod 9739)
```

dan titik:

```
P = (8045, 6936)
```
Diminta mencari titik Q sehingga:

```
P + Q = O
```

### Analisis
Dalam elliptic curve, berlaku bahwa:

```
P + (-P) = O
```

Sehingga Q adalah invers dari P. Untuk titik P(x, y), inversnya adalah:

```
(x, y) → (x, -y mod p)
```

### Perhitungan

```
Q = (8045, -6936 mod 9739)

-6936 mod 9739 = 9739 - 6936 = 2803
```

Maka Hasil-nya Ialah `Q = (8045, 2803)`


### Solver
`solver.py`
```python
# Elliptic Curve Parameters
p = 9739

# Point P
P = (8045, 6936)

# Inverse point: (x, -y mod p)
Q = (P[0], (-P[1]) % p)

print("Q =", Q)
```
flag: `crypto{8045, 2803}`
