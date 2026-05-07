from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

p = 310717010502520989590157367261876774703
a = 2
b = 3

E = EllipticCurve(GF(p), [a, b])

G = E(
    179210853392303317793440285562762725654,
    105268671499942631758568591033409611165
)

A = E(
    280810182131414898730378982766101210916,
    291506490768054478159835604632710368904
)

B = E(
    272640099140026426377756188075937988094,
    51062462309521034358726608268084433317
)

iv = bytes.fromhex("07e2628b590095a5e332d397b8a59aa7")
ct = bytes.fromhex(
    "8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af"
)

print("[+] curve order =", E.order())

# factor curve order
fac = factor(E.order())
print("[+] factors =", fac)

# solve discrete log in subgroup
n = discrete_log(A, G, operation='+')

print("[+] private key =", n)

# shared secret
S = n * B
shared_secret = int(S[0])

print("[+] shared secret =", shared_secret)

# derive AES key
sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode())
key = sha1.digest()[:16]

cipher = AES.new(key, AES.MODE_CBC, iv)

flag = unpad(cipher.decrypt(ct), 16)

print(flag.decode())

# crypto{n07_4ll_curv3s_4r3_s4f3_curv3s}
