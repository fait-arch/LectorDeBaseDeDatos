'''
    Desarillador:
                    jub1101 - Juan Moromenacho                

    Orden:

    
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


Driver="ODBC Driver 17 for SQL Server"
nombreServe     = input("Ingrese el nombre del Server: ") 
nombreDatabase  = input("Ingrese el nombre de la DataBase: ")

"""
Serve="DESKTOP-MP8VTD9"
Database="ImstartDataBase"
"""

coneccion=(f""" Driver={Driver};
Server={nombreServe};
Database={nombreDatabase};
Trusted_Connection=yes;""") 

print(coneccion)
#
#   Establecer la conexión a la base de datos
#
conn = pyodbc.connect(coneccion)
cursor = conn.cursor()



#
#   Funciones
#
def imprimirTabla(opcion):
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
        terminal_width = shutil.get_terminal_size().columns
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
        text_width = len(message.split('\n')[2])
        padding = (terminal_width - text_width) // 2 - 35  # 4 espacios adicionales antes del centrado
        # Imprimir el mensaje con el espaciado adecuado
        for line in message.split('\n'):
            print(' ' * padding + ' ' * 4 + line)   
def pausar():                               #Pausar pantalla
    print("\n\nPresiona una tecla para continuar...")
    msvcrt.getch()
def imprimirEncabezado():                   #Imprimir Cabesilla
    os.system('cls' if os.name == 'nt' else 'clear')
    # Obtener el ancho de la terminal
    terminal_width = shutil.get_terminal_size().columns

    # Mensaje a imprimir
    message = f"""
    
    
    {Fore.GREEN}8888888                        888                     888{Style.RESET_ALL}    
      {Fore.GREEN}888                          888                     888{Style.RESET_ALL}    
      {Fore.GREEN}888                          888                     888{Style.RESET_ALL}    
      {Fore.GREEN}888   88888b.d88b.  .d8888b  888888  8888b.  888d888 888888{Style.RESET_ALL} 
      {Fore.GREEN}888   888 "888 "88b 88K      888        "88b 888P"   888{Style.RESET_ALL}    
      {Fore.GREEN}888   888  888  888 "Y8888b. 888    .d888888 888     888{Style.RESET_ALL}    
      {Fore.GREEN}888   888  888  888      X88 Y88b.  888  888 888     Y88b.{Style.RESET_ALL}  
    {Fore.GREEN}8888888 888  888  888  88888P'  "Y888 "Y888888 888      "Y888{Style.RESET_ALL} 
                                                              
-----------------------------------------------------------------------         
"""
    
    # Calcular el espaciado para centrar horizontalmente
    text_width = len(message.split('\n')[2])
    padding = (terminal_width - text_width) // 2 - 35  # 4 espacios adicionales antes del centrado
    # Imprimir el mensaje con el espaciado adecuado
    for line in message.split('\n'):
        print(' ' * padding + ' ' * 4 + line)
def imprimirTablasSQL(opcionEscojida):           #Imprime los nombres de todas las <Filas> de las <Tablas> 
    if(opcionEscojida==1):      #   Nombre de las Tablas
        # Obtener el nombre de todas las tablas
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tablas = [row[0] for row in cursor.fetchall()]

        # Dividir las tablas en dos columnas
        mitad = len(tablas) // 2
        columna1 = tablas[:mitad]
        columna2 = tablas[mitad:]
        # Calcular el ancho máximo para cada columna
        anchoMaximo = max(max(len(tabla) for tabla in columna1), max(len(tabla) for tabla in columna2))
        # Obtener el ancho de la terminal
        terminalAncho = shutil.get_terminal_size().columns
        # Calcular el margen izquierdo para centrar horizontalmente
        margenIzquierdo = (terminalAncho - (anchoMaximo + 2) * 2) // 2

        # Imprimir las tablas en dos columnas con cuadros ASCII centrados
        for tabla1, tabla2 in zip(columna1, columna2):
            print(f"{' ' * margenIzquierdo}╔{'═' * (anchoMaximo + 2)}╗  ╔{'═' * (anchoMaximo + 2)}╗")
            print(f"{' ' * margenIzquierdo}║ {tabla1:<{anchoMaximo}} ║  ║ {tabla2:<{anchoMaximo}} ║")
            print(f"{' ' * margenIzquierdo}╚{'═' * (anchoMaximo + 2)}╝  ╚{'═' * (anchoMaximo + 2)}╝")
        # Si hay un número impar de tablas, imprimir la última tabla en una columna
        if len(tablas) % 2 != 0:                    
            ultima_tabla = tablas[-1]
            print(f"{' ' * margenIzquierdo}╔{'═' * (anchoMaximo + 2)}╗\t")
            print(f"{' ' * margenIzquierdo}║ {ultima_tabla:<{anchoMaximo}} ║")
            print(f"{' ' * margenIzquierdo}╚{'═' * (anchoMaximo + 2)}╝  ")
    elif(opcionEscojida==2):    #   Nombre de las Tablas con nombres de sus columnas                  

    
        # Obtener el nombre de todas las tablas
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tablas = [row[0] for row in cursor.fetchall()]

        # Dividir las tablas en dos columnas
        n = 14      #Espacio dentro de las tablas 
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
    elif(opcionEscojida==3):    #   Escoje la Tabla
        imprimirEncabezado()
        
        opcionEscojidaNombreTabla = imprimirMenu(tituloMenuDeTablas, opcionesMenuDeTablas)
        
        imprimirTabla(opcionEscojidaNombreTabla)
def imprimirFilasSQL():            #Imprimir <Nombre> de las <Tablas>
    #Igualaciones
    n=0
    imprimirEncabezado()

    print("\n\n*-- Imprimier todas las filas --* \n")
    #Modifique el script para que seleccione todas las filas de todas las tablas e imprima los resultados en la consola IDLE.
    # Obtener el nombre de todas las tablas en la base de datos
    tables = [table.table_name for table in cursor.tables(tableType='TABLE')]
    # Iterar sobre cada tabla y seleccionar solo las que están dentro de la carpeta "Tables"
    for table in tables:
        n+=1
        print(f"Tabla {n}: {table}") 
def ingresarValores(opcionEscojidaValores):             #Ingresar datos a una Tabla 
    #
    # Consulta para imprimir la tabla ANTES de la inserción
    #
    imprimirTabla(opcionEscojidaValores) 



    #
    # Consulta de inserción
    #
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
        if(columnaTipo=='int'):
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
        valores.append(valor)
    
    #
    valoresNormalizados = ""        
    for i, elemento in enumerate(valores):
        if isinstance(elemento, str):
            valoresNormalizados += f"'{elemento}'"
        else:
            valoresNormalizados += str(elemento)        
        if i < len(valores) - 1:
            valoresNormalizados += ","

    # Generar la consulta de inserción
    #insertQuery = f"INSERT INTO {NombredetablaElegida} ({', '.join(column[0] for column in columns)}) VALUES ({', '.join( str(valor) for valor in valores)})"
    insertQuery = f"insert into {NombredetablaElegida}({', '.join(column[0] for column in columns)}) values ({valoresNormalizados});"
    print(insertQuery)

    # Insertar los valores en la tabla
    cursor.execute(insertQuery)
    conn.commit()
    


    #
    # Consulta para imprimir la tabla después de la inserción
    #
    imprimirTabla(opcionEscojidaValores) 
def creditos():                    #Creditos del desarollador
    print("Opcion 5")
def imprimirMenu(titulo, opciones):
    imprimirEncabezado()
    global opcionEscojida   # Variable Opcion
    print(f"""          
            \t{Fore.LIGHTWHITE_EX}============================================================={Style.RESET_ALL}
                                {Fore.RED}{titulo}{Style.RESET_ALL}
            \t{Fore.LIGHTWHITE_EX}============================================================={Style.RESET_ALL}""")
    for i, opcion in enumerate(opciones, start=1):      # Texto de opciones
        print(f"\t\t\t{Fore.GREEN}[{i}.]{Style.RESET_ALL} {opcion}")
    print(f"""\t\t{Fore.LIGHTWHITE_EX}============================================================={Style.RESET_ALL}\n""")

    while True:         # Ingresa opcion
        try:
            opcionEscojida = int(input(f"\t\t ⭐ {Fore.GREEN}Ingresa un número entre 1 y {len(opciones)}: {Style.RESET_ALL}"))
            if opcionEscojida < 1 or opcionEscojida > len(opciones):
                raise ValueError(f"\n\t\t\t\t  {Fore.RED}❗❗Error:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}El valor ingresado está fuera del rango válido. !{Style.RESET_ALL} \n")
            break
        except ValueError as error:
            print(f"\n\t\t\t\t  {Fore.RED}❗❗Error:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}El valor ingresado está fuera del rango válido. !{Style.RESET_ALL} \n")
    
    return opcionEscojida



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

tituloMenuDeTablas = "Menu de las tablas 📓" 
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
opcionesMenuDeTablas = [row[0].replace("'", "") for row in cursor.fetchall()]

tituloMenuFilas = "Menu de acciones sobre las Filas "
opcionesMenuFilas = [
    "-",
    "-",
    "Regresar al Inicio"
]

tituloIngresoValores = "A que tabla Ingresamos 📓"
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
opcionesIngresoValores = [row[0].replace("'", "") for row in cursor.fetchall()]

#
#   Mensague de Bienbenida
#
imprimirEncabezado()

print(f"""
               < Vienvenido a la vercion 1.0 >
            ..--''
      (☞ﾟヮﾟ)☞                  ⭐♥⭐
    ------------            ------------                 
""")
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
    if opcionEscojidaProceso == 5:     #  Salir
        imprimirEncabezado()  
        print("holas")  
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
                imprimirTablasSQL(opcionEscojidaTabla)
                pausar()
            elif(opcionEscojidaTabla==4):                    
                break
    elif opcionEscojidaProceso == 2:   #  Ingresar Valores 
        imprimirMenu(tituloIngresoValores,opcionesIngresoValores)
        opcionEscojidaValores = opcionEscojida
        
        ingresarValores(opcionEscojidaValores)
        

        pausar()     
    elif opcionEscojidaProceso == 3:   #  Creditos
     
        pausar()
        break   



#
#   Cerrar la conexión a la base de datos
#

conn.close()