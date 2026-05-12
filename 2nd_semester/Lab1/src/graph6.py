import numpy as np
import matplotlib.pyplot as plt

a, b  = 1, 2
f     = lambda x: 4**x
exact = 12 / np.log(4)

def darboux(n):
    x = np.linspace(a, b, n+1); dx = 1/n
    return np.sum(f(x[:-1]))*dx, np.sum(f(x[1:]))*dx

def trapezoid(n):
    x = np.linspace(a, b, n+1); dx = 1/n
    return (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1])) * dx / 2

ns = np.arange(2, 201)
Ls, Us, Ts = zip(*[(darboux(n)[0], darboux(n)[1], trapezoid(n)) for n in ns])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(ns, Ls, label=r'$s_n$', color='#4C9BE8')
ax.plot(ns, Us, label=r'$S_n$', color='#E8734C')
ax.plot(ns, Ts, label=r'$T_n$', color='#7BC87B', ls='--')
ax.axhline(exact, color='black', ls=':', label=f'Точное = {exact:.4f}')
ax.set_xlabel('n'); ax.legend()
plt.tight_layout(); plt.savefig('convergence.pdf')
