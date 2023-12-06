import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image

# Función para la trayectoria parabólica
def parabolico(t, x_0, y_0, vx_0, vy_0, theta):
    x = x_0 + vx_0 * np.cos(theta) * t
    y = y_0 + vy_0 * np.sin(theta) * t - 4.9 * t**2
    return x, y

# Parámetros del tiro parabólico
x_0, y_0, vx_0, vy_0, theta = 0, 1.23, 6.8, 0, 0

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(0, 3.5)
ax.set_ylim(0, 1.3)
ax.set_xlabel(r'Alcance x [m]')
ax.set_ylabel(r'Altura y [m]')
ax.set_title(r'Animación del Tiro del Dardo con $v_0=6.8[m/s]$')

# Inicializar la línea y los puntos
line, = ax.plot([], [], color='blue', linestyle='-', linewidth=2)
points, = ax.plot([], [], 'ro')

# Inicialización de la función para la animación
def init():
    line.set_data([], [])
    points.set_data([], [])
    return line, points

# Función de actualización para la animación
def update(frame):
    t = frame / 10.0
    x, y = parabolico(t, x_0, y_0, vx_0, vy_0, theta)
    line.set_data(x, y)
    points.set_data(x, y)
    return line, points

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 11), init_func=init, blit=True)

# Guardar la animación como un archivo de gif utilizando Pillow
ani.save('trayectoriavideosinlinea6.gif', writer='pillow', fps=5)

plt.show()
