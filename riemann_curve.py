"""
Author: Paul Moran
Riemann Zeta function real and imaginary parts
15/08/2024
"""
import numpy as np
import matplotlib.pyplot as plt
#The next library contains the zeta(), zetazero(), and siegelz() functions
from mpmath import *
import cmath

A,B = [], []

for i in np.arange(0, 50,0.05):
    re_zeta = zeta(0.5 + 1j*i)
    A.append(re_zeta.real)
    B.append(re_zeta.imag)

plt.xlabel("Re Zeta(1/2 + it)")
plt.ylabel("Im Zeta(1/2 + it)")
plt.plot(A,B)
plt.show()

