Regresión POS Check | Apache License 2.0
Software de generación automática de documentación para Test de Regresión en dispositivos POS
Javier Bernal | 2023
Source code: https://github.com/WrathfulNico/RegresionPOS-Check

Requisitos:
Python 3.11 o superior
numpy 1.24.3 o superior
pandas 2.0.1 o superior
openpyxl 3.1 o superior
tkcalendar 1.6.1 o superior
java SE-17 o superior para DBConnect

Regresión Check es un software que automatiza la generación de documentación y evidencias de prueba para casos de "Test de Regresión" en dispositivos de POS.
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


Descargo de responsabilidad

El software Regresión POS Check fue desarrollado por Javier Bernal como herramienta de uso interno y personal para facilitar la documentación de los casos de prueba de regresión en dispositivos POS.

El software se distribuye bajo la licencia Apache 2.0, lo que permite su uso y modificación por terceros. Sin embargo, los autores no se responsabilizan por el uso del software en entornos de producción o para fines comerciales.

El software se proporciona "tal cual", sin garantías de ningún tipo, expresas o implícitas. Los autores no se responsabilizan por ningún daño o pérdida que pueda resultar del uso del software.

El usuario es el único responsable de evaluar la idoneidad del software para sus necesidades específicas.

En particular, los autores se eximen de responsabilidad por los siguientes aspectos:

    El software puede no ser compatible con todas las versiones de Python, NumPy, Pandas, OpenPyXL, tkcalendar y Java SE.
    El software puede no funcionar correctamente con datos de prueba que no cumplan con los requisitos especificados en el archivo README.
    El software puede no detectar todos los casos de prueba de regresión.
    El software puede producir reportes o evidencias de prueba que no sean precisos o completos.
    El usuario debe realizar sus propias pruebas para asegurarse de que el software cumple con sus requisitos.