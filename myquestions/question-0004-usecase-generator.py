def calcular_presion_final(presion_inicial, tasa_perdida, horas):
    pass

def generar_caso_de_uso():
    p_ini = np.random.uniform(2000, 3000)
    tasa = np.random.uniform(10, 50)
    t = np.random.uniform(1, 100)
    
    resultado = max(0.0, float(p_ini - (tasa * t)))
    
    input_data = {
        "presion_inicial": p_ini,
        "tasa_perdida": tasa,
        "horas": t
    }
    output_data = resultado
    
    return input_data, output_data
