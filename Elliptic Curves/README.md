The use of elliptic curves for public-key cryptography was first suggested in 1985. After resisting decades of attacks, they started to see widespread use from around 2005, providing several benefits over previous public-key cryptosystems such as RSA.

Smaller EC keys offer greater strength, with a 256-bit EC key having the same security level as a 3072-bit RSA key. Furthermore, several operations using those keys (including signing) can be more efficient both time- and memory-wise. Finally, since ECC is more complex than RSA, it has the welcome effect of encouraging developers to make use of trusted libraries rather than rolling their own.

This course is aimed to give you an intuition for the trapdoor function behind ECC; dip your toes into the mathematical structure underlying it; and have you breaking popular schemes like ECDSA.
