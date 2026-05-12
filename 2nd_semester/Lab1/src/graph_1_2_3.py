import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

a, b= 1, 2
n = int(input('Введите число разбиений: '))
f  = lambda x: 4**x
dx = 1/n
xp = np.linspace(a, b, n+1)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, side, color, label in zip(
        axes, ['left', 'right'], ['#4C9BE8', '#E8734C'],
        [f'Нижняя сумма $s_{n}$', f'Верхняя сумма $S_{n}$']):
    for i in range(n):
        h = f(xp[i]) if side == 'left' else f(xp[i+1])
        ax.add_patch(patches.Rectangle(
            (xp[i], 0), dx, h,
            lw=0.8, edgecolor='black', facecolor=color, alpha=0.55))
    ax.plot(np.linspace(a,b,500), f(np.linspace(a,b,500)), 'k-', lw=2,
            label=r'$f(x)=4^x$')
    ax.set_title(label); ax.legend()
plt.tight_layout(); plt.savefig('darboux_n5.pdf')
