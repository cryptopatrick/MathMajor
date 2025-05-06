import numpy as np
import matplotlib.pyplot as plt

# Skapa följder
n = np.arange(1, 20)

# Monoton och konvergent följd (1/n)
monoton_konvergent = 1 / n

# Monoton och divergerande följd (n)
monoton_divergent = n

# Konvergent men ej monoton följd (-1)^n / n
konvergent_ej_monoton = (-1)**n / n

# Begränsad men ej konvergent följd (-1)^n
begränsad_ej_konvergent = (-1)**n

# Plotta figurerna
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Monoton och konvergent
axs[0, 0].plot(n, monoton_konvergent, marker='o', linestyle='-', label=r'$x_k = \frac{1}{k}$')
axs[0, 0].set_title("Monoton och konvergent")
axs[0, 0].axhline(y=0, color='gray', linestyle='--')
axs[0, 0].legend()

# Monoton och divergerande
axs[0, 1].plot(n, monoton_divergent, marker='o', linestyle='-', label=r'$x_k = k$')
axs[0, 1].set_title("Monoton och divergerande")
axs[0, 1].axhline(y=0, color='gray', linestyle='--')
axs[0, 1].legend()

# Konvergent men ej monoton
axs[1, 0].plot(n, konvergent_ej_monoton, marker='o', linestyle='-', label=r'$x_k = (-1)^k / k$')
axs[1, 0].set_title("Konvergent men ej monoton")
axs[1, 0].axhline(y=0, color='gray', linestyle='--')
axs[1, 0].legend()

# Begränsad men ej konvergent
axs[1, 1].plot(n, begränsad_ej_konvergent, marker='o', linestyle='-', label=r'$x_k = (-1)^k$')
axs[1, 1].set_title("Begränsad men ej konvergent")
axs[1, 1].axhline(y=0, color='gray', linestyle='--')
axs[1, 1].legend()

plt.tight_layout()
plt.show()

