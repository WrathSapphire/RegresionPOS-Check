import pandas as pd
df = pd.read_excel('MET001.xlsx')

def OpSinTarjeta(): 
    # Venta Operaciones Sin Tarjeta Aprobada   
    df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                     & (df['DISPOSITIVO'] == 'POS')
                     & (df['MARCA'] == 'ENT')
                     & (df['PRODUCTO'] == 'PMO')
                     & (df['METODO'] == '  ') 
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]
    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Op. Sin Tarjeta Aprobada [DESA]")
    else:
        print("[Correcto] Op. Sin Tarjeta Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Op Sin Tarjeta Aprobada.xlsx')

    # Venta Operaciones Sin Tarjeta Reversada   
    df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                     & (df['DISPOSITIVO'] == 'POS')
                     & (df['MARCA'] == 'ENT')
                     & (df['PRODUCTO'] == 'PMO')
                     & (df['METODO'] == '  ') 
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Op. Sin Tarjeta Reversada [DESA]")
    else:
        print("[Correcto] Op. Sin Tarjeta Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Op Sin Tarjeta Reversada.xlsx')
    print ("\n")