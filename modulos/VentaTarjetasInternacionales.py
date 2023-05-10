import pandas as pd
df = pd.read_excel('MET001.xlsx')

def VentaTarjetasInternacionales(): 
    # Venta Tarjeta Internacional Aprobada
    df_temp = df.loc[(df['LOCAL_INTERNACIONAL'] == 'I')
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta Tarjeta Internacional Aprobada [Simulador, DESA]")
    else:
        print("[Correcto] Venta Tarjeta Internacional Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Tarjeta Internacional Aprobada.xlsx')

    # Venta Tarjeta Internacional Reversada
    df_temp = df.loc[(df['LOCAL_INTERNACIONAL'] == 'I')
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta Tarjeta Internacional Reversada [Simulador, DESA]")
    else:
        print("[Correcto] Venta Tarjeta Internacional Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Tarjeta Internacional Reversada.xlsx')


    print("\n")