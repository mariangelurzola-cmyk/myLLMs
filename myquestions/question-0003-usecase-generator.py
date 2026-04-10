def detectar_anomalia_presion(serie_datos):
    pass

def generar_caso_de_uso():
    # Generar 49 datos normales y 1 dato final (posible anomalía)
    base = np.random.normal(100, 5, 49)
    ultimo = np.random.uniform(80, 120)
    serie_completa = np.append(base, ultimo)
    
    media_previa = np.mean(base)
    std_previa = np.std(base)
    resultado = bool(abs(ultimo - media_previa) > 2 * std_previa)
    
    return {"serie_datos": serie_completa}, resultado
