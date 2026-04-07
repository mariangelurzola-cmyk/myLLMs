import numpy as np
from sklearn.preprocessing import StandardScaler

def generar_caso_de_uso_escalar_caracteristicas():
    """
    Genera una matriz aleatoria y su versión escalada (media 0, var 1).
    """
    # 1. Crear matriz aleatoria de 10 filas y 3 columnas
    # Multiplicamos por 100 para que los valores no estén ya normalizados
    X = np.random.rand(10, 3) * 100

    input_data = {'X': X}

    # 2. Calcular la respuesta correcta usando StandardScaler
    scaler = StandardScaler()
    output_data = scaler.fit_transform(X)

    return input_data, output_data
