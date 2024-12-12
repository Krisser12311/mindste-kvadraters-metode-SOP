import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definer værdier for a og b
a = np.linspace(-10, 10, 500)  # Højere opløsning for 4K
b = np.linspace(-10, 10, 500)
a, b = np.meshgrid(a, b)

# Definer funktionen
f = 44*a*b - 68*b + 4*b**2 - 416*a + 162*a**2 + 316

# Opret plot
fig = plt.figure(figsize=(16, 9), dpi=300)  # 16:9 og 300 DPI for 4K-kvalitet
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(a, b, f, cmap='viridis', edgecolor='none')

# Tilføj funktionsforskriften som tekst på grafen
function_label = r"$f(a, b) = 44ab - 68b + 4b^2 - 416a + 162a^2 + 316$"
ax.text2D(0.05, 0.95, function_label, transform=ax.transAxes, fontsize=12, color='black')

# Juster kamera vinklen
ax.view_init(elev=20, azim=-60)  # Sænker kameraet lidt og justerer vinklen

# Tilføj akse- og farvebjælke
ax.set_xlabel('a', fontsize=12)
ax.set_ylabel('b', fontsize=12)
ax.set_zlabel('f(a, b)', fontsize=12)

# Gem grafen som et 4K-billede
plt.savefig("3d_function_plot_4k_with_function_label.png", dpi=300, bbox_inches='tight')
plt.close()

print("Grafen er gemt som '3d_function_plot_4k_with_function_label.png'")
