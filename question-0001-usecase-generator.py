import pandas as pd
import random

def generar_caso_de_uso_limpiar_datos_clientes():
    n = random.randint(5, 8)
    df = pd.DataFrame({
        'cliente': [random.choice([" JUAN perez ", "maria GARCIA", " luis mArtinez "]) for _ in range(n)],
        'email': [random.choice(["user@gmail.com", "admin@u-tad.com", "test@yahoo.es"]) for _ in range(n)]
    })
    input_data = {'df': df.copy()}
    df_res = df.copy()
    df_res['cliente'] = df_res['cliente'].str.strip().str.title()
    df_res['dominio'] = df_res['email'].str.split('@').str[1]
    return input_data, df_res
