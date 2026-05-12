import numpy as np
import matplotlib.pyplot as plt

a, b, n = 1, 2, 5
f  = lambda x: 4**x
xp = np.linspace(a, b, n+1)
dx = 1/n
T  = (f(xp[0]) + 2*np.sum(f(xp[1:-1])) + f(xp[-1])) * dx / 2

fig, ax = plt.subplots(figsize=(7, 4))
for i in range(n):
    ax.fill([xp[i], xp[i], xp[i+1], xp[i+1]],
            [0, f(xp[i]), f(xp[i+1]), 0],
            color='#B57BCC', alpha=0.45, edgecolor='black', lw=0.8)
ax.plot(np.linspace(a,b,500), f(np.linspace(a,b,500)), 'k-', lw=2,
        label=r'$f(x)=4^x$')
ax.set_title(f'Метод трапеций, n={n},  T≈{T:.4f}'); ax.legend()
plt.tight_layout(); plt.savefig('trapezoid.pdf')
