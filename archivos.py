def leer_archivo(file_name):
    print(f'Intentas abrir este archivo {file_name}')
    #Abrir open()
    #Procesar read/write
    #Cerrar close()
    #Wth nso permite agrupar el trabajo con archivos
    with open (file_name, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            print(linea, end=' ')
        #while(linea):
        #    print(linea)
        #    linea = file.readLine()
    #print('Archivo leido y cerrado')

def agregar_equipo(file_name, equipo):
    with open(file_name, 'a') as file:
        file.write(f"\n{equipo}")

    print("Equipo guardado :3")

def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        lista_equipos.remove(equipo)
        print("Equipo eliminado :( ")
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo que deseas eliminar no existe')

def actualizar_equipo(file_name, equipo, new_equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        index_equipo = lista_equipos.index(f'{equipo}\n')
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo no se encontro :(')