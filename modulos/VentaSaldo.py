import pandas as pd
df = pd.read_excel('MET001.xlsx')
def VentaSaldo():
    # Venta Saldo TD Banda Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 2)
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Saldo TD Banda Aprobada")
    else:
        print("[Correcto] Venta Saldo TD Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TD Banda Aprobada.xlsx')

    # Venta Saldo TD Banda Reversada

    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 2)
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Saldo TD Banda Reversada")
    else:
        print("[Correcto] Venta Saldo TD Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TD Banda Reversada.xlsx')


    # Venta Saldo TC Banda Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 1)
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Saldo TC Banda Aprobada")
    else:
        print("[Correcto] Venta Saldo TC Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TC Banda Aprobada.xlsx')


    # Venta Saldo TC Banda Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 1)
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Saldo TC Banda Reversada")
    else:
        print("[Correcto] Venta Saldo TC Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TC Banda Reversada.xlsx')
    #########################################################################################################
    #########################################################################################################

    # Venta Saldo TD Chip Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 2)
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Saldo TD Chip Aprobada")
    else:
        print("[Correcto] Venta Saldo TD Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TD Chip Aprobada.xlsx')


    # Venta Saldo TD Chip Reversada

    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 2)
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Saldo TD Chip Reversada")
    else:
        print("[Correcto] Venta Saldo TD Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TD Chip Reversada.xlsx')


    # Venta Saldo TC Chip Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 1)
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Saldo TC Chip Aprobada")
    else:
        print("[Correcto] Venta Saldo TC Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TC Chip Aprobada.xlsx')


    # Venta Saldo TC Chip Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 1)
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Saldo TC Chip Reversada")
    else:
        print("[Correcto] Venta Saldo TC Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TC Chip Reversada.xlsx')


    #########################################################################################################
    #########################################################################################################

    # Venta Saldo TD CTLS Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 2)
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Saldo TD CTLS Aprobada")
    else:
        print("[Correcto] Venta Saldo TD CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TD CTLS Aprobada.xlsx')


    # Venta Saldo TD CTLS Reversada

    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 2)
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Saldo TD CTLS Reversada")
    else:
        print("[Correcto] Venta Saldo TD CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TD CTLS Reversada.xlsx')


    # Venta Saldo TC CTLS Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 1)
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]
    if df_temp.empty:
        print("[Falta] Venta Saldo TC CTLS Aprobada")
    else:
        print("[Correcto] Venta Saldo TC CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TC CTLS Aprobada.xlsx')


    # Venta Saldo TC CTLS Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'VMTE')
                     & (df['COD_PAGO'] == 1)
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta Saldo TC CTLS Reversada")
    else:
        print("[Correcto] Venta Saldo TC CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta Saldo TC CTLS Reversada.xlsx')

    print("\n")