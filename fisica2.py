import numpy as np

def calcular_potencial(q, x, y):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    q = q * 1e-9  # Convertir de nC a C
    r = np.sqrt(x**2 + y**2)  # Distancia en metros
    V = k * q / r
    return V

# Datos del problema
q = 3  # nC
x = 20 * 0.0254  # Convertir de pulgadas a metros
y = 12 * 0.0254  # Convertir de pulgadas a metros

# Calcular el potencial
potencial = calcular_potencial(q, x, y)
print(f"El potencial eléctrico en el punto P(20, 12) es: {potencial} V")

