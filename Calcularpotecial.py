import numpy as np

def calcular_potencial(q, x, y):
    """
    Calcula el potencial eléctrico debido a una carga puntual.
    
    Parámetros:
    q (float): Carga en nC.
    x, y (float): Coordenadas del punto en metros.
    
    Retorna:
    float: Potencial eléctrico en voltios (V).
    """
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    q = q * 1e-9  # Convertir de nC a C
    r = np.sqrt(x**2 + y**2)  # Distancia en metros
    V = k * q / r
    return V

def solicitar_datos():
    """
    Solicita al usuario los valores de la carga y las coordenadas.
    
    Retorna:
    tuple: Contiene los valores q, x, y.
    """
    q = float(input("Ingrese la carga en nC: "))
    x = float(input("Ingrese la coordenada x en pulgadas: ")) * 0.0254  # Convertir de pulgadas a metros
    y = float(input("Ingrese la coordenada y en pulgadas: ")) * 0.0254  # Convertir de pulgadas a metros
    return q, x, y

def main():
    """
    Función principal que coordina la solicitud de datos, el cálculo y la impresión del resultado.
    """
    # Solicitar datos al usuario
    q, x, y = solicitar_datos()
    
    # Calcular el potencial
    potencial = calcular_potencial(q, x, y)
    
    # Redondear el potencial a dos decimales
    potencial_redondeado = round(potencial, 2)
    
    # Imprimir el resultado
    print(f"El potencial eléctrico en el punto P({x/0.0254:.2f}, {y/0.0254:.2f}) es: {potencial_redondeado} V")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
