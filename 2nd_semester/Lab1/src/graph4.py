import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

a, b = 1, 2
f   = lambda x: 4**x

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, n in zip(axes, [5, 10, 100]):
    np.random.seed(42)
    dx  = 1/n
    xl  = np.linspace(a, b, n+1)[:-1]
    xi  = xl + np.random.rand(n) * dx
    val = np.sum(f(xi)) * dx
    for i in range(n):
        ax.add_patch(patches.Rectangle(
            (xl[i], 0), dx, f(xi[i]),
            lw=0.5, edgecolor='black', facecolor='#7BC87B', alpha=0.6))
    ax.plot(np.linspace(a,b,500), f(np.linspace(a,b,500)), 'k-', lw=2)
    ax.plot(xi, f(xi), 'ro', ms=3.5, label=r'$\xi_k$')
    ax.set_title(f'n={n},  сумма≈{val:.4f}'); ax.legend()
plt.tight_layout(); plt.savefig('random_sums.pdf')
