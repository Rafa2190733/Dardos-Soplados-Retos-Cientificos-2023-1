import matplotlib.pyplot as plt
import numpy as np

def parabolico(t, x_0, y_0, vx_0, vy_0, theta):
    x = x_0 + vx_0 * np.cos(theta) * t
    y = y_0 + vy_0 * np.sin(theta) * t - 4.9 * t**2
    # Detener el cálculo cuando la altura sea menor o igual a cero
    mask = y > 0
    return [x[mask], y[mask]]

# Valores iniciales
x_0, y_0, vx_0, vy_0, theta = 0, 1.23, 6.8, 0, 0

# Calcular el tiempo de caída y el alcance máximo
t_caida = np.sqrt(y_0 / 4.9)
x_alcance = x_0 + vx_0 * np.cos(theta) * t_caida

# Calcular las posiciones x e y hasta que la altura sea menor o igual a cero
time = np.linspace(0, 1, 25)
data = np.array(parabolico(time, x_0, y_0, vx_0, vy_0, theta))

# Graficar los puntos utilizando plt.scatter()
plt.scatter(data[0, :], data[1, :], label='Tiro del dardo', color='red', marker='o')
plt.xlabel(r'Alcance x [m]')
plt.ylabel(r'Altura y [m]')
plt.title(r'Tiro del dardo')
plt.legend()

# Añadir el cuadro de texto para el alcance máximo a la izquierda del punto
plt.text(x_alcance - 1, 0, f't_caida: {t_caida:.2f}s\nx_max: {x_alcance:.2f}m',
         bbox=dict(facecolor='white', alpha=0.7))

# Añadir la línea que conecta los puntos
plt.plot(data[0, :], data[1, :], color='blue', linestyle='-', linewidth=2)

# Añadir la ecuación de la trayectoria en x e y con parámetros específicos
plt.text(0.1, 0.6, f'$y = {y_0:.2f} - 4.9 t^2$',
         fontsize=12, color='green')

plt.text(0.1, 0.5, f'$x = {vx_0:.2f} t$',
         fontsize=12, color='purple')

plt.grid()
plt.show()



print(data)
