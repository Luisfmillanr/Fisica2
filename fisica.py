import numpy as np

def calcular_fuerza(q1, q2, x1, y1, x2, y2):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    q1 = q1 * 1e-6  # Convertir de μC a C
    q2 = q2 * 1e-6  # Convertir de μC a C
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2) * 1e-2  # Convertir de cm a m
    F = k * abs(q1 * q2) / r**2
    return F

# Datos del problema
q1 = 5  # μC
q2 = -8  # μC
x1, y1 = -2, 1  # cm
x2, y2 = 1, 5  # cm

# Calcular la fuerza
fuerza = calcular_fuerza(q1, q2, x1, y1, x2, y2)
print(f"La magnitud de la fuerza entre las partículas es: {fuerza} N")

