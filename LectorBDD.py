'''
    Desarillador:
                    jub1101 - Juan Moromenacho                

    Orden:
        El código proporcionado es un programa destinado a la interaccion con una base de datos.
        Ofrece opciones para imprimir tablas y ver datos organizados, ingresar valores adicionales en la base de 
        datos, y opciones para salir del programa, . 
        Es una herramienta conveniente para explorar y administrar datos de manera rapido.

        El prgrama fue desarollado por jub1101 y cnlund/Nico Luna, jub1101 se encargo del desarollo del pryecto y cnlund
        en la correcion de errores para el ingreso de datos y fue crucial en la 

    EJECUTAR Comanndo de Ejecucion de instalacion de librerias:
        pip install -r Comando_Instalacion/requirements.txt

'''



#
#   Librerias necesarias 
#
import pyodbc
import msvcrt
import os
import subprocess
import shutil
from colorama import Fore, Style
import random

#
#
#
# Pregunta al usuario si quiere ingresar su propio nombre o utilizar el nombre predeterminado
while True:
    # Pregunta al usuario si quiere ingresar su propio nombre o utilizar el nombre predeterminado
    opcion = input(f"{Fore.LIGHTYELLOW_EX}¿Deseas ingresar tu propio nombre? (1/0): {Style.RESET_ALL}").strip().lower()
    # Si elige "Sí", solicita el nombre al usuario
    if opcion == "1":
        nombreServer = input("Ingresa tu nombre de servidor: ")
        # Configura la cadena de conexión
        connection_string = f'Driver=ODBC Driver 17 for SQL Server;Server={nombreServer};Trusted_Connection=yes;'
        try:
            # Conecta a SQL Server
            conn = pyodbc.connect(connection_string)
            # Crea un cursor
            cursor = conn.cursor()
            # Consulta para obtener los nombres de las bases de datos
            query = "SELECT name FROM sys.databases WHERE database_id > 4"  # Excluye bases de datos del sistema
            # Ejecuta la consulta
            cursor.execute(query)
            # Recorre los resultados y agrega los nombres a la lista
            databaseNames = [row[0] for row in cursor.fetchall()]
            # Cierra el cursor y la conexión
            cursor.close()
            conn.close()
            break
        except pyodbc.Error as e:
            print(f"Error: {e}")
    elif opcion == "0":
        nombreServer = "DESKTOP-F5TMUR9"
        break
    else:
        print("Opción no válida. Por favor, responde '1' o '0'.")
# Configura la cadena de conexión
connection_string = f'Driver=ODBC Driver 17 for SQL Server;Server={nombreServer};Trusted_Connection=yes;'
databaseNames = []                  # Crear una lista para almacenar los nombres de las bases de datos
try:
    # Conecta a SQL Server
    conn = pyodbc.connect(connection_string)
    # Crea un cursor
    cursor = conn.cursor()
    # Consulta para obtener los nombres de las bases de datos
    query = "SELECT name FROM sys.databases WHERE database_id > 4"  # Excluye bases de datos del sistema
    # Ejecuta la consulta
    cursor.execute(query)
    # Recorre los resultados y agrega los nombres a la lista
    for row in cursor.fetchall():
        databaseNames.append(row[0])
    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()
except pyodbc.Error as e:
    print(f"Error: {e}")
# Imprimir los nombres de las bases de datos 
print(f"""  
██{Fore.LIGHTRED_EX}▓    ▓{Style.RESET_ALL}█████  ▄████▄  ▄▄▄█████{Fore.YELLOW}▓ ▒{Style.RESET_ALL}█████   ██▀███   ▄▄▄▄   ▓█████▄ ▓█████▄ 
{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}██{Fore.YELLOW}▒    {Style.RESET_ALL}{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}█   ▀ {Fore.YELLOW}▒{Style.RESET_ALL}██▀ ▀█{Fore.YELLOW}  ▓  {Style.RESET_ALL}██{Fore.YELLOW}▒ ▓▒▒{Style.RESET_ALL}██{Fore.YELLOW}▒  {Style.RESET_ALL}██{Fore.YELLOW}▒▓{Style.RESET_ALL}██ {Fore.YELLOW}▒ {Style.RESET_ALL}██{Fore.YELLOW}▒▓{Style.RESET_ALL}█████▄ {Fore.YELLOW}▒{Style.RESET_ALL}██▀ ██▌{Fore.YELLOW}▒{Style.RESET_ALL}██▀ ██▌
{Fore.YELLOW}▒{Style.RESET_ALL}██{Fore.YELLOW}▒    ▒{Style.RESET_ALL}███   {Fore.YELLOW}▒{Style.RESET_ALL}{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}█    ▄{Fore.YELLOW} ▒ ▓{Style.RESET_ALL}██{Fore.YELLOW}░ ▒░▒{Style.RESET_ALL}██{Fore.YELLOW}░  {Style.RESET_ALL}██{Fore.YELLOW}▒▓{Style.RESET_ALL}██ {Fore.YELLOW}░{Style.RESET_ALL}▄█ {Fore.YELLOW}▒▒{Style.RESET_ALL}██▒ ▄██{Fore.YELLOW}░{Style.RESET_ALL}██   █▌{Fore.YELLOW}░{Style.RESET_ALL}██   █▌
{Fore.YELLOW}▒{Style.RESET_ALL}██{Fore.YELLOW}▒    ▒▓{Style.RESET_ALL}█  ▄ {Fore.YELLOW}▒{Style.RESET_ALL}{Fore.LIGHTRED_EX}▓▓{Style.RESET_ALL}▄ ▄██{Fore.YELLOW}▒░ ▓{Style.RESET_ALL}██{Fore.YELLOW}▓ ░ ▒{Style.RESET_ALL}██   ██{Fore.YELLOW}░▒{Style.RESET_ALL}██▀▀█▄  {Fore.YELLOW}▒{Style.RESET_ALL}██░█▀  ░▓{Style.RESET_ALL}█▄   ▌{Fore.YELLOW}░▓{Style.RESET_ALL}█▄   ▌
{Fore.YELLOW}░{Style.RESET_ALL}██████{Fore.YELLOW}▒░▒{Style.RESET_ALL}████{Fore.YELLOW}▒▒ {Style.RESET_ALL}{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}███▀{Fore.YELLOW} ░  ▒{Style.RESET_ALL}██{Fore.YELLOW}▒ ░ ░ {Style.RESET_ALL}████{Fore.YELLOW}▓▒░░{Style.RESET_ALL}██▓ ▒██{Fore.YELLOW}▒░▓{Style.RESET_ALL}█  ▀█{Fore.YELLOW}▓░▒{Style.RESET_ALL}████{Fore.YELLOW}▓ ░▒{Style.RESET_ALL}████▓ 
{Fore.YELLOW}░ ▒░▓  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▒▓{Style.RESET_ALL}███▀{Fore.YELLOW}▒ ▒▒▓  ▒  ▒▒▓  ▒ 
{Fore.YELLOW}░ ░ ▒  ░ ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░▒░▒   ░  ░ ▒  ▒  ░ ▒  ▒ {Style.RESET_ALL}
{Fore.YELLOW}  ░ ░      ░   ░          ░      ░ ░ ░ ▒    ░░   ░  ░    ░  ░ ░  ░  ░ ░  ░ {Style.RESET_ALL}
{Fore.YELLOW}    ░  ░   ░  ░░ ░                   ░ ░     ░      ░         ░       ░    {Style.RESET_ALL}
{Fore.YELLOW}               ░                                         ░  ░       ░   {Style.RESET_ALL}{Fore.GREEN}Vercion: 1.01{Style.RESET_ALL}   
{Fore.GREEN}Autor: Jub1101{Style.RESET_ALL}


{Fore.MAGENTA}[:] Seleccione la base de datos [::]{Style.RESET_ALL}
""")
for i, name in enumerate(databaseNames, 1):
    print(f"{Fore.RED}[{i}.]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{name}{Style.RESET_ALL}")
# Solicitar al usuario que ingrese un número
while True:
    try:
        max_numero = len(databaseNames)
        seleccion = int(input(f"\n\n {Fore.GREEN}Seleccione un número de base de datos (1 al {max_numero}): {Style.RESET_ALL}"))
        if 1 <= seleccion <= max_numero:
            nombreDatabase = databaseNames[seleccion - 1]
            break
        else:
            print(f"{Fore.GREEN}Número fuera de rango. Por favor, seleccione un número entre 1 y {max_numero}.{Style.RESET_ALL}")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")



#
#   Establecer la conexión a la base de datos
#
coneccion = f"""Driver=ODBC Driver 17 for SQL Server;
Server={nombreServer};
Database={nombreDatabase};
Trusted_Connection=yes;"""

print(coneccion)

conn = pyodbc.connect(coneccion)
cursor = conn.cursor()



#
#   Funciones
#
#Funciones Guerfanas
def vienvenida (nombreServer, nombreDatabase):      #Imprime la Vienvenida
    mensaje = f"""
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║                            {Fore.LIGHTYELLOW_EX}DETALLES DEL INGRESO{Style.RESET_ALL}                                ║ 
        ║                           {Fore.LIGHTYELLOW_EX}-----------------------{Style.RESET_ALL}                              ║ 
        ║                                                                                ║        
        ║   {Fore.LIGHTMAGENTA_EX}Nombre del server{Style.RESET_ALL}                            {Fore.LIGHTMAGENTA_EX}Nombre de la base de Datos{Style.RESET_ALL}      ║    
        ║   {nombreServer}                              {nombreDatabase}                  
        ║                                                                                ║
        ║                                                                                ║
        ║                __________________                                              ║
        ║               |   version 1.2    |                                             ║
        ║               |__________________|                                             ║
        ║       (●'◡'●)/                                                                   
        ╚════════════════════════════════════════════════════════════════════════════════╝"""

    # Obtener el ancho de la terminal
    terminal_width = shutil.get_terminal_size().columns
    # Imprimir el mensaje centrado horizontalmente
    print(mensaje.center(terminal_width))
def imprimirEncabezado():                           #Imprimir Cabesilla
# Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    # Obtener el ancho de la terminal
    terminal_width = shutil.get_terminal_size().columns

# Mensaje a imprimir
    # Mensaje a imprimir
    message = f"""
██{Fore.LIGHTRED_EX}▓    ▓{Style.RESET_ALL}█████  ▄████▄  ▄▄▄█████{Fore.YELLOW}▓ ▒{Style.RESET_ALL}█████   ██▀███   ▄▄▄▄   ▓█████▄ ▓█████▄ 
{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}██{Fore.YELLOW}▒    {Style.RESET_ALL}{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}█   ▀ {Fore.YELLOW}▒{Style.RESET_ALL}██▀ ▀█{Fore.YELLOW}  ▓  {Style.RESET_ALL}██{Fore.YELLOW}▒ ▓▒▒{Style.RESET_ALL}██{Fore.YELLOW}▒  {Style.RESET_ALL}██{Fore.YELLOW}▒▓{Style.RESET_ALL}██ {Fore.YELLOW}▒ {Style.RESET_ALL}██{Fore.YELLOW}▒▓{Style.RESET_ALL}█████▄ {Fore.YELLOW}▒{Style.RESET_ALL}██▀ ██▌{Fore.YELLOW}▒{Style.RESET_ALL}██▀ ██▌
{Fore.YELLOW}▒{Style.RESET_ALL}██{Fore.YELLOW}▒    ▒{Style.RESET_ALL}███   {Fore.YELLOW}▒{Style.RESET_ALL}{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}█    ▄{Fore.YELLOW} ▒ ▓{Style.RESET_ALL}██{Fore.YELLOW}░ ▒░▒{Style.RESET_ALL}██{Fore.YELLOW}░  {Style.RESET_ALL}██{Fore.YELLOW}▒▓{Style.RESET_ALL}██ {Fore.YELLOW}░{Style.RESET_ALL}▄█ {Fore.YELLOW}▒▒{Style.RESET_ALL}██▒ ▄██{Fore.YELLOW}░{Style.RESET_ALL}██   █▌{Fore.YELLOW}░{Style.RESET_ALL}██   █▌
{Fore.YELLOW}▒{Style.RESET_ALL}██{Fore.YELLOW}▒    ▒▓{Style.RESET_ALL}█  ▄ {Fore.YELLOW}▒{Style.RESET_ALL}{Fore.LIGHTRED_EX}▓▓{Style.RESET_ALL}▄ ▄██{Fore.YELLOW}▒░ ▓{Style.RESET_ALL}██{Fore.YELLOW}▓ ░ ▒{Style.RESET_ALL}██   ██{Fore.YELLOW}░▒{Style.RESET_ALL}██▀▀█▄  {Fore.YELLOW}▒{Style.RESET_ALL}██░█▀  ░▓{Style.RESET_ALL}█▄   ▌{Fore.YELLOW}░▓{Style.RESET_ALL}█▄   ▌
{Fore.YELLOW}░{Style.RESET_ALL}██████{Fore.YELLOW}▒░▒{Style.RESET_ALL}████{Fore.YELLOW}▒▒ {Style.RESET_ALL}{Fore.LIGHTRED_EX}▓{Style.RESET_ALL}███▀{Fore.YELLOW} ░  ▒{Style.RESET_ALL}██{Fore.YELLOW}▒ ░ ░ {Style.RESET_ALL}████{Fore.YELLOW}▓▒░░{Style.RESET_ALL}██▓ ▒██{Fore.YELLOW}▒░▓{Style.RESET_ALL}█  ▀█{Fore.YELLOW}▓░▒{Style.RESET_ALL}████{Fore.YELLOW}▓ ░▒{Style.RESET_ALL}████▓ 
{Fore.YELLOW}░ ▒░▓  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▒▓{Style.RESET_ALL}███▀{Fore.YELLOW}▒ ▒▒▓  ▒  ▒▒▓  ▒ 
{Fore.YELLOW}░ ░ ▒  ░ ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░▒░▒   ░  ░ ▒  ▒  ░ ▒  ▒ {Style.RESET_ALL}
{Fore.YELLOW}  ░ ░      ░   ░          ░      ░ ░ ░ ▒    ░░   ░  ░    ░  ░ ░  ░  ░ ░  ░ {Style.RESET_ALL}
{Fore.YELLOW}    ░  ░   ░  ░░ ░                   ░ ░     ░      ░         ░       ░    {Style.RESET_ALL}
{Fore.YELLOW}               ░                                         ░  ░       ░   {Style.RESET_ALL}{Fore.GREEN}Vercion: 1.01{Style.RESET_ALL}   
{Fore.GREEN}Autor: Jub1101{Style.RESET_ALL}
    -------------------------------------------------------------------------------------------
    
    """        

    # Calcular el espaciado para centrar horizontalmente
    text_width = max(len(line) for line in message.split('\n'))
    padding = (terminal_width - text_width) // 2

    # Imprimir el mensaje con el espaciado adecuado
    for line in message.split('\n'):
        print(' ' * padding + line)
def pausar():                                       #Pausar pantalla
    print("\n\nPresiona una tecla para continuar...")
    msvcrt.getch()
def imprimirTablasNombres():                        #Imprime los nombres de las tabla [1.1] 
        # Obtener el nombre de todas las tablas
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tablas = [row[0] for row in cursor.fetchall()]
        tablas.remove("sysdiagrams")

        # Dividir las tablas en dos columnas
        mitad = len(tablas) // 2
        columna1 = tablas[:mitad]
        columna2 = tablas[mitad:]
        # Calcular el ancho máximo para cada columna
        anchoMaximoTabla = max(max(len(tabla) for tabla in columna1), max(len(tabla) for tabla in columna2))
        # Obtener el ancho de la terminal
        terminalAncho = shutil.get_terminal_size().columns
        # Calcular el margen izquierdo para centrar horizontalmente
        margenIzquierdo = (terminalAncho - (anchoMaximoTabla + 2) * 2) // 2

        # Imprimir las tablas en dos columnas con cuadros ASCII centrados
        for tabla1, tabla2 in zip(columna1, columna2):
            print(f"{' ' * margenIzquierdo}╔{'═' * (anchoMaximoTabla + 2)}╗  ╔{'═' * (anchoMaximoTabla + 2)}╗")
            print(f"{' ' * margenIzquierdo}║ {tabla1:<{anchoMaximoTabla}} ║  ║ {tabla2:<{anchoMaximoTabla}} ║")
            print(f"{' ' * margenIzquierdo}╚{'═' * (anchoMaximoTabla + 2)}╝  ╚{'═' * (anchoMaximoTabla + 2)}╝")
        # Si hay un número impar de tablas, imprimir la última tabla en una columna
        if len(tablas) % 2 != 0:                    
            ultima_tabla = tablas[-1]
            print(f"{' ' * margenIzquierdo}╔{'═' * (anchoMaximoTabla + 2)}╗\t")
            print(f"{' ' * margenIzquierdo}║ {ultima_tabla:<{anchoMaximoTabla}} ║")
            print(f"{' ' * margenIzquierdo}╚{'═' * (anchoMaximoTabla + 2)}╝  ")
def imprimirTablasNombreColumna():                  #Imprime los nombres y los nombres de columnas de las tabla [1.2]
    # Obtener el nombre de todas las tablas
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    tablas = [row[0] for row in cursor.fetchall()]
    tablas.remove("sysdiagrams")

    # Dividir las tablas en dos columnas
    n = 10      #Espacio dentro de las tablas 
    mitad = len(tablas) // 2
    columna1 = tablas[:mitad]
    columna2 = tablas[mitad:]

    # Obtener las columnas para cada tabla
    columnas_por_tabla = {}
    for tabla in tablas:
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabla}'")
        columnas = [row[0] for row in cursor.fetchall()]
        columnas_por_tabla[tabla] = columnas
    # Calcular el ancho máximo para cada columna
    anchoMaximoTabla = max(max(len(tabla) for tabla in columna1), max(len(tabla) for tabla in columna2))
    anchoMaximoColumna = max(max(len(columna) for columna in columnas_por_tabla[tabla]) for tabla in tablas)
    # Obtener el ancho de la terminal
    terminalAncho = shutil.get_terminal_size().columns
    # Calcular el margen izquierdo para centrar horizontalmente
    margenIzquierdo = (terminalAncho - (anchoMaximoColumna + 2) * 2) // 2

    # Imprimir las tablas y sus columnas en cuadros ASCII centrados
    for tabla1, tabla2 in zip(columna1, columna2):
        # Cuadro ASCII para la tabla1
        print(f"{' ' * margenIzquierdo}╔{'═' * (anchoMaximoTabla + n)}╗  ╔{'═' * (anchoMaximoTabla + n)}╗")
        print(f"{' ' * margenIzquierdo}║{tabla1:^{anchoMaximoTabla + n}}║  ║{tabla2:^{anchoMaximoTabla + n}}║")
        print(f"{' ' * margenIzquierdo}╠{'═' * (anchoMaximoTabla + n)}╣  ╠{'═' * (anchoMaximoTabla + n)}╣")
        columnas_tabla1 = columnas_por_tabla[tabla1]
        columnas_tabla2 = columnas_por_tabla[tabla2]
        max_columnas = max(len(columnas_tabla1), len(columnas_tabla2))
        for i in range(max_columnas):
            columna1 = columnas_tabla1[i] if i < len(columnas_tabla1) else ''
            columna2 = columnas_tabla2[i] if i < len(columnas_tabla2) else ''
            print(f"{' ' * margenIzquierdo}║ {columna1:<{anchoMaximoColumna}} ║  ║ {columna2:<{anchoMaximoColumna}} ║")
            
        print(f"{' ' * margenIzquierdo}╚{'═' * (anchoMaximoTabla + n)}╝  ╚{'═' * (anchoMaximoTabla + n)}╝\n")

    # Si hay un número impar de tablas, imprimir la última tabla en un cuadro ASCII separado
    if len(tablas) % 2 != 0:
        ultimaTabla = tablas[-1]
        print(f"{' ' * margenIzquierdo}╔{'═' * (anchoMaximoTabla + n)}╗  ")
        print(f"{' ' * margenIzquierdo}║{ultimaTabla:^{anchoMaximoTabla+n}}║  ")
        print(f"{' ' * margenIzquierdo}╠{'═' * (anchoMaximoTabla + n)}╣  ")
        
        columnasUltimaTabla = columnas_por_tabla[ultimaTabla]
        for columna in columnasUltimaTabla:
            print(f"{' ' * margenIzquierdo}║ {columna:<{anchoMaximoColumna}} ║  ")                
        print(f"{' ' * margenIzquierdo}╚{'═' * (anchoMaximoTabla + n)}╝  ")
def imprimirTablaEscojida(opcion):                  #Imprime la tabla escojida con sus valores [1.3]
    #
    # Consulta para imprimir la tabla antes de la inserción
    #
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    tablaElegida = opcionesMenuDeTablas[(opcion-1)]        
    # Obtener los nombres de las columnas y los valores de la tabla elegida
    columns = [column.column_name for column in cursor.columns(table=tablaElegida)]
    cursor.execute(f"SELECT * FROM {tablaElegida}")
    rows = cursor.fetchall()



    if rows:
        # Calcular el ancho máximo de la columna de nombres y valores
        anchoMaximoColumna = max(len(column) for column in columns)
        anchoMaximoFila = max(len(str(value)) for row in rows for value in row)
        # Calcular el ancho total de la terminal
        anchoTerminal = shutil.get_terminal_size().columns
        # Calcular la posición central para alinear la tabla horizontalmente
        posicionCentral = (anchoTerminal - anchoMaximoColumna - anchoMaximoFila - 6) // 2  # Considera los bordes y espacios

        # Imprimir la tabla con los nombres de columna y los valores de las filas
        bordeSuperior = f"╔{'═' * (anchoMaximoColumna + 2)}╦{'═' * (anchoMaximoFila + 2)}╗"
        bordeIntermedio = f"╠{'═' * (anchoMaximoColumna + 2)}╬{'═' * (anchoMaximoFila + 2)}╣"
        bordeInferior = f"╚{'═' * (anchoMaximoColumna + 2)}╩{'═' * (anchoMaximoFila + 2)}╝"
        espaciosVacios = " " * (posicionCentral - 1)  # Ajusta la posición central
        print(f"{espaciosVacios}{bordeSuperior}")
        print(f"{espaciosVacios}║ {tablaElegida:^{anchoMaximoColumna}} ║ {'Value':^{anchoMaximoFila}} ║")
        print(f"{espaciosVacios}{bordeIntermedio}")
        for row in rows:
            for column, value in zip(columns, row):
                print(f"{espaciosVacios}║ {column:^{anchoMaximoColumna}} ║ {str(value):<{anchoMaximoFila}} ║")
            print(f"{espaciosVacios}{bordeIntermedio}")
        print(f"{espaciosVacios}{bordeInferior}")        
    else:
         # Obtener el ancho de la terminal
        terminalWidth = shutil.get_terminal_size().columns
        mensagueDeVacio = f"La tabla {tablaElegida} no tiene valores"
        # Calcular el número de caracteres en el texto
        numeroCaracteres = len(mensagueDeVacio)
        numeroCaracteres =  ((numeroCaracteres // 3)+1)
        # Mensaje a imprimir
        
        message = f"""
        {Fore.LIGHTMAGENTA_EX}╔ {f"{Fore.LIGHTMAGENTA_EX} = {Style.RESET_ALL}" *(numeroCaracteres)} {Fore.LIGHTMAGENTA_EX}╗{Style.RESET_ALL}    
        {Fore.LIGHTMAGENTA_EX}║{Style.RESET_ALL}  {mensagueDeVacio} {Fore.LIGHTMAGENTA_EX} ║{Style.RESET_ALL}  
        {Fore.LIGHTMAGENTA_EX}╚ {f"{Fore.LIGHTMAGENTA_EX} = {Style.RESET_ALL}" *(numeroCaracteres)} {Fore.LIGHTMAGENTA_EX}╝{Style.RESET_ALL}        

        """
        
        # Calcular el espaciado para centrar horizontalmente
        textWidth = len(message.split('\n')[2])
        padding = (terminalWidth - textWidth) // 2 - 35  # 4 espacios adicionales antes del centrado
        # Imprimir el mensaje con el espaciado adecuado
        for line in message.split('\n'):
            print(' ' * padding + ' ' * 4 + line)  
def ingresoDatosaTabla():                           #Ingresa la tabla escojida [2.1]
    global funciono
    #Nombre de tabla a la que hacer la insecion
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    NombredetablaElegida = opcionesMenuDeTablas[(opcionEscojidaValores-1)]
    # Obtener los nombres de las columnas y los tipos de datos de la tabla seleccionada
    columns_query = f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{NombredetablaElegida}'"
    cursor.execute(columns_query)
    columns = cursor.fetchall()
    
    # Solicitar al usuario los valores para cada columna    -   INPUT
    valores = []
    for column in columns:
        columnaNombre = column[0]
        columnaTipo = column[1]         
        textoDeError    = f" El valor ingresado en la columa {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} no es del tipo {Fore.BLUE}'{columnaTipo}'{Style.RESET_ALL}"  
        if(columnaTipo=='int' ):
            while True:
                try:
                    valor = int(input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.BLUE}'{columnaTipo}'{Style.RESET_ALL}: " ))
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}
                         {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")   
        elif(columnaTipo=='float' ):
            while True:
                try:
                    valor = float(input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.LIGHTYELLOW_EX}'{columnaTipo}'{Style.RESET_ALL}: " ))
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}
                         {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")   
        elif(columnaTipo=='nchar' ):
            while True:
                try:
                    valor = int(input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.LIGHTYELLOW_EX}'{columnaTipo}'{Style.RESET_ALL}: " ))
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.MAGENTA}X{Style.RESET_ALL}
                         {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")   
        elif(columnaTipo=='numeric' ):
            while True:
                try:
                    valor = input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.LIGHTMAGENTA_EX}'{columnaTipo}'{Style.RESET_ALL}: ")
                    valor = int(valor) if "." not in valor else float(valor)  # Intenta convertir a int, si no es posible, convierte a float
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}
                        {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")
        elif(columnaTipo=='varchar'):            
            while True:
                try:
                    valor = str(input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.RED}'{columnaTipo}'{Style.RESET_ALL}: " ))
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}
                         {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")
        elif(columnaTipo=='text'):
            while True:
                try:
                    valor = str(input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.YELLOW}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.RED}'{columnaTipo}'{Style.RESET_ALL}: " ))
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}
                         {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")
        elif(columnaTipo=='char'):
            while True:
                try:
                    valor = str(input(f"\n\n\t\t\t\t😀  Ingrese el valor para la columna {Fore.LIGHTCYAN_EX}{columnaNombre}{Style.RESET_ALL} de tipo {Fore.RED}'{columnaTipo}'{Style.RESET_ALL}: " ))
                    break
                except ValueError:
                    # Calcular el número de caracteres en el texto
                    numeroCaracteres = len(textoDeError)-10
                    print(f"""  
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}
                         {textoDeError}                          
                        {Fore.RED}X{Style.RESET_ALL} {f"{Fore.LIGHTMAGENTA_EX}={Style.RESET_ALL}" *(numeroCaracteres)} {Fore.RED}X{Style.RESET_ALL}""")
        
        """PUNTO DE MEJORA -  
                Ingresar n valores a la tabla hasta decir basta"""
        valores.append(valor)
    
    #
    valoresNormalizados = ""        
    for i, elemento in enumerate(valores):
        if isinstance(elemento, str):
            valoresNormalizados += f"'{elemento}'"
        else:
            valoresNormalizados += str(elemento)        
        if i < len(valores) - 1:
            valoresNormalizados += ", "
    # Generar la consulta de inserción
    insertQuery = f"insert into {NombredetablaElegida}({', '.join(column[0] for column in columns)}) values ({valoresNormalizados});"
    # Ver Como se escribe la insercion
    print(f"""
          --------------------------------
          {Fore.LIGHTYELLOW_EX}La insercion se vera asi: 
          {insertQuery}{Style.RESET_ALL}
          """)
    print(f"""\n\n\t\t\t\t ⁉ 😮 ¿Estás seguro de que quieres guardar los siguientes valores? 🚨🚨⁉:""")
    #Imprime los nombre de las columnas con los valores ingresados por el usurio
    for i, column in enumerate(columns):
        columnaNombre = column[0]
        valorIngresado = valores[i]
        print(f"\t\t\t\t\t- {columnaNombre}: {valorIngresado}")
    #Valida y pregunta si guardar o no
    while True:
        guardar = input(f"""\n\n\t\t\t\t ⁉ 😳 {Fore.BLUE}Respuesta [{Fore.GREEN}s{Style.RESET_ALL}{Fore.BLUE}/{Style.RESET_ALL}{Fore.RED}n{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL}  {Fore.BLUE}o [{Style.RESET_ALL}{Fore.MAGENTA}E{Style.RESET_ALL}{Fore.BLUE}]:{Style.RESET_ALL}  """)
        guardar = guardar.lower()
        if guardar == 's' or guardar == 'n' or guardar == 'e':
            break
        else:
            print(f"\n\t{Fore.RED}Error:{Style.RESET_ALL} Opción inválida. Por favor, ingresa 's' o 'n'. Inténtalo nuevamente.")            
    if(guardar=='s'):
        try:
            #Mensague de accion
            
            # Insertar los valores en la tabla
            cursor.execute(insertQuery)
            conn.commit()
        except pyodbc.IntegrityError as e:
            #Mensague de accion
            error_message = str(e)
            funciono=0
            print(f"\n{Fore.RED}Error al insertar los valores en la tabla:{Style.RESET_ALL}")
            print(f"{error_message}")
            print(f"\n{Fore.LIGHTMAGENTA_EX}El {Fore.RED}Error:{Style.RESET_ALL} {Fore.LIGHTMAGENTA_EX} se causa por que se REPITIO una llave PRIMRAIR {Style.RESET_ALL}\n\n")
        else:
            funciono=1
            print(f"\n{Fore.GREEN}Insercion de los valores CORRECTOS en la tabla:{Style.RESET_ALL}")
    if(guardar=='n'):
        ingresoDatosaTabla()
    if(guardar=='e'):
       pausar()


    while True:
        repetir = input(f"""\n\n\t\t\t\t ⁉ 😳 Ingresamos un valor mas en la misma columna uwu? [{Fore.GREEN}s{Style.RESET_ALL}{Fore.BLUE}/{Style.RESET_ALL}{Fore.RED}n{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL}  {Fore.BLUE}o [{Style.RESET_ALL}{Fore.MAGENTA}E{Style.RESET_ALL}{Fore.BLUE}]:  {Style.RESET_ALL}""")
        repetir = repetir.lower()
        if repetir == 's':
            ingresoDatosaTabla()
        elif repetir == 'n':        
            break
        else:
            print(f"\n\t\t\t\t{Fore.RED}Error:{Style.RESET_ALL} Opción inválida. Por favor, ingresa 's' o 'n'. Inténtalo nuevamente.")



    #
    #
    #
    return funciono
def generarDiseno():                                #Genera Estrellas
    ancho = 200  # Ancho del diseño
    alto = 20  # Alto del diseño
    diseño = ""
    


    #
    # Generar el cielo estrellado
    #
    for _ in range(alto):
        for _ in range(ancho):
            # Probabilidad de generar una estrella en cada posición
            probabilidadEstrella = 0.1
            if random.random() < probabilidadEstrella:
                # Generar diferentes caracteres para las estrellas
                probabilidadEstrella = ["*", " ", ".", "+"," ","⭐","☀","🌟","☄","✨"]
                diseño += random.choice(probabilidadEstrella)
            else:
                diseño += " "
        diseño += "\n"



    #
    # Ubicación aleatoria del corazón
    #
    xCorazon = random.randint(0, ancho - 5)
    yCorazon = random.randint(0, alto - 2)



    #
    # Insertar el corazón en el diseño
    #
    diseño = diseño[:yCorazon * (ancho + 1) + xCorazon] + "  **  \n" + \
            diseño[yCorazon * (ancho + 1) + xCorazon + ancho + 1:]
    return diseño
    #-----------
#Funciones Madres
def imprimirMenu(titulo, opciones):                 #Imprime Menu de Opciones
    global opcionEscojida   # Variable Opcion
    
    #
    # Encabezado
    #
    imprimirEncabezado()
    
    #
    # Imprecion de Titulo y Opciones
    #
    print(f"""          
            \t{Fore.LIGHTWHITE_EX}============================================================={Style.RESET_ALL}
                                {Fore.RED}{titulo}{Style.RESET_ALL}
            \t{Fore.LIGHTWHITE_EX}============================================================={Style.RESET_ALL}""")
    for i, opcion in enumerate(opciones, start=1):      # Texto de opciones
        print(f"\t\t\t{Fore.GREEN}[{i}.]{Style.RESET_ALL} {opcion}")
    print(f"""\t\t{Fore.LIGHTWHITE_EX}============================================================={Style.RESET_ALL}\n""")

    #
    # Ingresa opcion
    #
    while True:         # Validacion
        try:
            opcionEscojida = int(input(f"\t\t ⭐ {Fore.GREEN}Ingresa un número entre 1 y {len(opciones)}: {Style.RESET_ALL}"))
            if opcionEscojida < 1 or opcionEscojida > len(opciones):
                raise ValueError(f"\n\t\t\t\t  {Fore.RED}❗❗Error:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}El valor ingresado está fuera del rango válido. !{Style.RESET_ALL} \n")
            break
        except ValueError as error:
            print(f"\n\t\t\t\t  {Fore.RED}❗❗Error:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}El valor ingresado está fuera del rango válido. !{Style.RESET_ALL} \n")
    
    return opcionEscojida
def imprimirTablasSQL(opcionEscojida):              #Sube Menu [1]
    if(opcionEscojida==1):      #Imprime los nombres de las tabla [1.1]
        imprimirTablasNombres()
    elif(opcionEscojida==2):    #Imprime los nombres y los nombres de columnas de las tabla [1.2]                  
        #
        # Imprecion de Tabla
        #
        imprimirTablasNombreColumna()     
    elif(opcionEscojida==3):    #Imprime la tabla escojida con sus valores [1.3]
        imprimirEncabezado()
        
        opcionEscojidaNombreTabla = imprimirMenu(tituloMenuDeTablas, opcionesMenuDeTablas)
        
        imprimirTablaEscojida(opcionEscojidaNombreTabla)
def ingresarValores(opcionEscojidaValores):         #Proceso de Insercion    
    #
    # Consulta para imprimir la tabla ANTES de la inserción
    #
    imprimirTablaEscojida(opcionEscojidaValores) 



    #
    # Consulta de inserción
    #
    ingresoDatosaTabla()


    #
    # Consulta para imprimir la tabla después de la inserción
    #
    if(funciono==1):
        imprimirTablaEscojida(opcionEscojidaValores) 




#
#   Tablas de Menu
#
tituloMenuPrincipal = "Que quieres hacer mi rey 👑"
opcionesMenuPrincipal = [
    "Imprimir Tablas",
    "Ingresar valores",
    "Créditos",
    "Salir"
]

tituloMenuTablas = "Menu de acciones en las Tablas 🛠"
opcionesMenuTablas = [
    "Imprimir Los Nombres de las tabla",
    "Imprimir Todas las Tablas con sus columnas",
    "Imprimir Una Tabla En Especifico ⭐",
    "Regresar al Inicio"
]

tituloMenuInsercion = "Menu de Insercion "
opcionesMenuInsercion = [
    "Escojer Tabla",
    "Regresar al Inicio"
]

tituloMenuDeTablas = "Menu de las tablas 📓" 
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
opcionesMenuDeTablas = [row[0].replace("'", "") for row in cursor.fetchall() if row[0] != "sysdiagrams"]


tituloIngresoValores = "A que tabla Ingresamos 📓"
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
opcionesIngresoValores = [row[0].replace("'", "") for row in cursor.fetchall() if row[0] != "sysdiagrams"]



#
#   Mensague de Bienbenida
#
imprimirEncabezado()

vienvenida (nombreServer,nombreDatabase)
pausar()



#
#   Proceso
#
while True: 
    #
    #   Imprimir Menu - INPUT
    #
    imprimirMenu(tituloMenuPrincipal,opcionesMenuPrincipal)
    opcionEscojidaProceso = opcionEscojida

    
    #
    #   Ejecucion de opcion - Proceso
    #
    if opcionEscojidaProceso == 4:     #  Salir
        imprimirEncabezado()  
        print("Y el juego se terminó, y el jugador despertó del sueño. Y el jugador empezó un nuevo sueño. Y el jugador soñó otra vez, soñó mejor. Y el jugador fue el universo. Y el jugador fue el amor.")  
        pausar()
        subprocess.call("taskkill /F /IM cmd.exe")
        break        
    elif opcionEscojidaProceso == 1:   #  Imprimier Tablas
        while True:
            imprimirMenu(tituloMenuTablas,opcionesMenuTablas)
            opcionEscojidaTabla = opcionEscojida
                                      
            if(opcionEscojidaTabla==1):     #Imprimir nombres de las tablas                
                imprimirTablasSQL(opcionEscojidaTabla)
                pausar()
            elif(opcionEscojidaTabla==2):   #Imprimir tablas con sus columnas
                imprimirTablasSQL(opcionEscojidaTabla)
                pausar()
            elif(opcionEscojidaTabla==3):   #Escojer e Imprimir tablas
                print(opcionEscojidaTabla)
                imprimirTablasSQL(opcionEscojidaTabla)
                pausar()
            elif(opcionEscojidaTabla==4):   #Salir              
                break
    elif opcionEscojidaProceso == 2:   #  Ingresar Valores 
        while True:
            imprimirMenu(tituloMenuInsercion,opcionesMenuInsercion)
            opcionEscojidaTabla = opcionEscojida
                                      
            if(opcionEscojidaTabla==1):     #Imprimir nombres de las tablas                
                imprimirMenu(tituloIngresoValores,opcionesIngresoValores)
                opcionEscojidaValores = opcionEscojida
                ingresarValores(opcionEscojidaValores)
                pausar()
            elif(opcionEscojidaTabla==2):   #Salir
                break  
    elif opcionEscojidaProceso == 3:   #  Creditos
        # Generar el diseño ASCII
        disenoCielo = generarDiseno()

        # Imprimir el diseño ASCII
        print(disenoCielo)
        pausar()
           



#
#   Cerrar la conexión a la base de datos
#

conn.close()
