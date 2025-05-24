import numpy as np
import matplotlib.pyplot as plt

# Parametry elipsy
a = 3       # półoś główna
b = 1.5     # półoś mniejsza
theta = np.radians(120)  # kąt obrotu elipsy

# Generowanie punktów elipsy
t = np.linspace(0, 2 * np.pi, 400)
x = a * np.cos(t)
y = b * np.sin(t)

# Obrót elipsy
x_rot = x * np.cos(theta) - y * np.sin(theta)
y_rot = x * np.sin(theta) + y * np.cos(theta)

# Generowanie linii nachylonej o 120° przechodzącej przez środek
line_length = 2.5  # długość linii (od -line_length do +line_length)
x_line = np.linspace(-line_length, line_length, 100)
slope = np.tan(theta)
y_line = slope * x_line

# Rysowanie
plt.figure(figsize=(6,6))
plt.plot(x_rot, y_rot)
plt.plot(x_line, y_line, 'r--')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("Elipsa polaryzacji i linia nachylona o 120°")
plt.show()


# Aktualizacja kąta nachylenia do 130 stopni
theta = np.radians(120)  # nowy kąt obrotu elipsy

# Ponowne obliczenie obrotu elipsy
x_rot = x * np.cos(theta) - y * np.sin(theta)
y_rot = x * np.sin(theta) + y * np.cos(theta)

# Nowa linia nachylona o 130°
slope = np.tan(theta)
y_line = slope * x_line

# Rysowanie zaktualizowanego wykresu
plt.figure(figsize=(6,6))
plt.plot(x_rot, y_rot)
plt.plot(x_line, y_line, 'r--')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("Elipsa polaryzacji i linia nachylona o 120°")
plt.show()

# Zmieniamy proporcje elipsy, by bardziej przypominała okrąg
a = 2
b = 1.6

# Generowanie punktów nowej elipsy
x = a * np.cos(t)
y = b * np.sin(t)

# Obrót elipsy o 130°
x_rot = x * np.cos(theta) - y * np.sin(theta)
y_rot = x * np.sin(theta) + y * np.cos(theta)

# Rysowanie zaktualizowanego wykresu
plt.figure(figsize=(6,6))
plt.plot(x_rot, y_rot)
plt.plot(x_line, y_line)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("Elipsa polaryzacji i linia nachylona o 130°")
plt.show()
