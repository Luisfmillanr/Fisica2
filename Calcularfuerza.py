import numpy as np

def calcular_fuerza(q1, q2, x1, y1, x2, y2):
    """
    Calcula la fuerza electrostática entre dos partículas cargadas.
    
    Parámetros:
    q1 (float): Carga de la primera partícula en μC.
    q2 (float): Carga de la segunda partícula en μC.
    x1, y1 (float): Coordenadas de la primera partícula en cm.
    x2, y2 (float): Coordenadas de la segunda partícula en cm.
    
    Retorna:
    float: Magnitud de la fuerza entre las partículas en Newtons (N).
    """
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    q1 = q1 * 1e-6  # Convertir de μC a C
    q2 = q2 * 1e-6  # Convertir de μC a C
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2) * 1e-2  # Convertir de cm a m
    F = k * abs(q1 * q2) / r**2
    return F

def solicitar_datos():
    """
    Solicita al usuario los valores de las cargas y las coordenadas.
    
    Retorna:
    tuple: Contiene los valores q1, q2, x1, y1, x2, y2.
    """
    q1 = float(input("Ingrese la carga de la primera partícula en μC: "))
    q2 = float(input("Ingrese la carga de la segunda partícula en μC: "))
    x1 = float(input("Ingrese la coordenada x de la primera partícula en cm: "))
    y1 = float(input("Ingrese la coordenada y de la primera partícula en cm: "))
    x2 = float(input("Ingrese la coordenada x de la segunda partícula en cm: "))
    y2 = float(input("Ingrese la coordenada y de la segunda partícula en cm: "))
    return q1, q2, x1, y1, x2, y2

def main():
    """
    Función principal que coordina la solicitud de datos, el cálculo y la impresión del resultado.
    """
    # Solicitar datos al usuario
    q1, q2, x1, y1, x2, y2 = solicitar_datos()
    
    # Calcular la fuerza
    fuerza = calcular_fuerza(q1, q2, x1, y1, x2, y2)
    
    # Redondear la fuerza a dos decimales
    fuerza_redondeada = round(fuerza, 2)
    
    # Imprimir el resultado
    print(f"La magnitud de la fuerza entre las partículas es: {fuerza_redondeada} N")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
