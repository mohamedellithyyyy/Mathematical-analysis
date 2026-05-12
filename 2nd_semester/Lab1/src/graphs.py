import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

text = input(
    "Введите номер графика:\n"
    "1 — Суммы Дарбу\n"
    "2 — Случайные суммы Римана\n"
    "3 — Метод трапеций\n"
    "4 — Сходимость методов\n"
)

# =========================
# 1–3 DARBOUX GRAPH
# =========================
def graph1():
    a, b = 1, 2
    n = int(input('Введите число разбиений: '))
    f = lambda x: 4**x

    dx = (b - a) / n
    xp = np.linspace(a, b, n + 1)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    for ax, side, color, label in zip(
        axes,
        ['left', 'right'],
        ['#4C9BE8', '#E8734C'],
        [f'Нижняя сумма $s_n$', f'Верхняя сумма $S_n$']
    ):
        for i in range(n):
            h = f(xp[i]) if side == 'left' else f(xp[i + 1])
            ax.add_patch(patches.Rectangle(
                (xp[i], 0), dx, h,
                lw=0.8, edgecolor='black',
                facecolor=color, alpha=0.55
            ))

        x = np.linspace(a, b, 500)
        ax.plot(x, f(x), 'k-', lw=2, label=r'$f(x)=4^x$')
        ax.set_title(label)
        ax.legend()

    plt.tight_layout()
    plt.savefig(f'g_darboux_n{n}.pdf')
    plt.show()


# =========================
# 4 RANDOM RIEMANN
# =========================
def graph2():
    a, b = 1, 2
    f = lambda x: 4**x

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    for ax, n in zip(axes, [5, 10, 100]):
        np.random.seed(42)
        dx = (b - a) / n

        xl = np.linspace(a, b, n + 1)[:-1]
        xi = xl + np.random.rand(n) * dx
        val = np.sum(f(xi)) * dx

        for i in range(n):
            ax.add_patch(patches.Rectangle(
                (xl[i], 0), dx, f(xi[i]),
                lw=0.5, edgecolor='black',
                facecolor='#7BC87B', alpha=0.6
            ))

        x = np.linspace(a, b, 500)
        ax.plot(x, f(x), 'k-', lw=2)
        ax.plot(xi, f(xi), 'ro', ms=3.5)
        ax.set_title(f'n={n}, сумма≈{val:.4f}')

    plt.tight_layout()
    plt.savefig('random_sums.pdf')
    plt.show()


# =========================
# 5 CONVERGENCE
# =========================
def graph3():
    a, b = 1, 2
    f = lambda x: 4**x
    exact = 12 / np.log(4)

    def darboux(n):
        x = np.linspace(a, b, n + 1)
        dx = (b - a) / n
        return np.sum(f(x[:-1])) * dx, np.sum(f(x[1:])) * dx

    def trapezoid(n):
        x = np.linspace(a, b, n + 1)
        dx = (b - a) / n
        return (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1])) * dx / 2

    ns = np.arange(2, 201)
    Ls, Us, Ts = zip(*[
        (darboux(n)[0], darboux(n)[1], trapezoid(n)) for n in ns
    ])

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ns, Ls, label='s_n')
    ax.plot(ns, Us, label='S_n')
    ax.plot(ns, Ts, label='T_n', ls='--')
    ax.axhline(exact, ls=':', label=f'Точное = {exact:.4f}')

    ax.set_xlabel('n')
    ax.legend()

    plt.tight_layout()
    plt.savefig('convergence.pdf')
    plt.show()


# =========================
# MENU CONTROL
# =========================
if text == "1":
    graph1()

elif text == "2":
    graph2()

elif text == "3":
    graph2()  # trapezoid not separated in your code, can merge later

elif text == "4":
    graph3()

else:
    print("Неверный выбор")