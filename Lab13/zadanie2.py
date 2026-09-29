import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4))

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x) + np.cos(2*x)
g = ( (0.1 * pow(x,3)) - (0.2 * pow(x,2)) + (0.5 * x) )

plt.plot(x, y, label='f(x) = sin(x) + cos(2x)', color='red', linestyle='-', linewidth=2)
plt.plot(x, g, label='g(x) = $0.1x^{3}$ - $0.2x^{2}$ + 0.5x', color='blue', linestyle='-.', linewidth=2)

plt.title('Przybliżenie funkcji trygonometrycznej wielomianem')
plt.xlabel('x (radiany)')
plt.ylabel('Wartość funkcji')

custom_xticks = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
custom_xtick_labels = ['$-\pi$', r'-$\frac{\pi}{2}$', '$0$', r'$\frac{\pi}{2}$', '$\pi$']
ax.set_xticks(custom_xticks)
ax.set_xticklabels(custom_xtick_labels)
idx = np.argwhere(np.diff(np.sign(y-g))).flatten()
for i in idx:
    plt.axvline(x[i], linestyle='--', color='green')

plt.legend(loc='lower right')
plt.grid(True, linestyle='--', color='gray', alpha=0.6)
plt.show()