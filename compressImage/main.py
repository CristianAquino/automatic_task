import fileScript
import folderScript

if __name__ == '__main__':
    print('Bienvenido elija una opcion a realizar')
    print('1. Comprimir imagenes dentro de una carpeta')
    print('2. Comprimir imagenes desde de un conjunto de folders')
    option = input('Elija una opcion: ')

    if option == '1':
        fileScript.run()
    else:
        folderScript.run()
