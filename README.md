______                              _                ______  _____  _____ 
| ___ \                            (_)               | ___ \|  _  |/  ___|
| |_/ / ___   __ _  _ __  ___  ___  _   ___   _ __   | |_/ /| | | |\ `--. 
|    / / _ \ / _` || '__|/ _ \/ __|| | / _ \ | '_ \  |  __/ | | | | `--. \
| |\ \|  __/| (_| || |  |  __/\__ \| || (_) || | | | | |    \ \_/ //\__/ /
\_| \_|\___| \__, ||_|   \___||___/|_| \___/ |_| |_| \_|     \___/ \____/ 
 _____  _     __/ |        _             __      _____                    
/  __ \| |   |___/        | |           /  |    |____ |                   
| /  \/| |__    ___   ___ | | __ __   __`| |        / /                   
| |    | '_ \  / _ \ / __|| |/ / \ \ / / | |        \ \                   
| \__/\| | | ||  __/| (__ |   <   \ V / _| |_ _ .___/ /                   
 \____/|_| |_| \___| \___||_|\_\   \_/  \___/(_)\____/  

Regresión POS Check | Apache License 2.0
Software de generación automática de documentación para Test de Regresión en dispositivos POS de BANCARD
Javier Bernal | 2023
Source code: https://github.com/WrathfulNico/RegresionPOS-Check

Requisitos:
Python 3.11 o superior
numpy 1.24.3 o superior
pandas 2.0.1 o superior
openpyxl 3.1 o superior
java SE-17 o superior para DBConnect

Regresión Check es un software que automatiza la generación de documentación y evidencias de prueba para casos de "Test de Regresión" en dispositivos de POS de Bancard.
Este software lee un archivo excel con las transacciones realizadas en los dispositivos de POS y filtra los diferentes casos de pruebas y combinaciones existentes según los criterios definidos por el usuario.
Luego, crea un reporte que indica si se encontraron todos los casos esperados, la cantidad de transacciones y el resultado de cada set de pruebas.
Además, cada caso de prueba exitoso genera un archivo excel donde se detallan las transacciones que corresponden a ese caso, facilitando así el análisis y la validación de las pruebas.

Como utilizar:
Al abrir el programa tendrá los botones "Ejecutar", "Parámetros", "Generar Registros" y "Salir".

El botón Ejecutar llama a la función RegresionCheck(). Esta función llama a todos los módulos involucrados en el proceso de revisión de los registros para cada caso de pruebas definido. Los módulos definidos en esa función consumen el archivo ".\\resources\\MET001.xlsx" para encontrar los registros transaccionales necesarios para validar cada caso.

El botón Parámetros llama a la clase VentanaParametros, abriendo otra ventana al lado de la principal. La función de esta ventana es poder interactuar con los filtros por los cuales se realizarán las consultas SQL a las bases de datos transaccionales. Los filtros configurables son fecha de inicio de pruebas, comercio y sucursal, y seriales de dispositivos POS.

El botón Generar Registros Ejecuta el programa DBConnect que se encuentra compilado en una archivo jar ejecutable. El mismo tiene dos clases principales, el primero consume el archivo config.properties para conectarse a las bases de datos transaccionales utilizando los parámetros de usuario, contraseña y cadena de conexión. Luego almacena los queries ".\\resources\\query.sql" y ".\\resources\\queryIC.sql"; realiza la primera consulta en ambos entornos y la última solamente en Desarrollo. Luego de almacenar los registros en variables tipo ResultSet, procede a guardarlos en 3 archivos Excels individuales.
La segunda clase procede a combinar los tres archivos en uno sólo. Luego se eliminarán los archivos residuales ya que no serán necesarios para la ejecución del programa.

El botón salir simplemente cierra el programa.