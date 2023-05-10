import pandas as pd
df = pd.read_excel('MET001.xlsx')
# Venta Vuelto TD Aprobada
def VentaVuelto():

    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['COD_PAGO'] == 2)
                     & (df['CASHBACK'] == 'S')
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Vuelto TD Aprobada")
    else:
        print("[Correcto] Venta Vuelto TD Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Vuelto TD Aprobada.xlsx')


    # Venta Vuelto TD Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['COD_PAGO'] == 2)
                     & (df['CASHBACK'] == 'S')
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Vuelto TD Reversada")
    else:
        print("[Correcto] Venta Vuelto TD Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Vuelto TD Reversada.xlsx')

    print("\n")