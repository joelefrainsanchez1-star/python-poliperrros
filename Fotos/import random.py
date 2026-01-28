import random
import os
from PIL import Image
import time

datosPoliperros = {
    "Nombre": [],
    "huellaDactilar": [],
    "foto": [],
}

def menu():
    print(
        "======== POLIPERROS EPN ========\n"
        "Bienvenido!\n"
        "1.- Registrar Poliperro\n"
        "2.- Mostrar Poliperros\n"
        "3.- Buscar Poliperro\n"
        "4.- Salir\n"
    )
    return int(input("Ingresar una opcion: "))

# ---------------- REGISTRO ----------------
def registro():
    os.makedirs("Fotos", exist_ok=True)
    os.makedirs("BDDPERROS", exist_ok=True)

    archivo = open("poliperros.txt", "a")

    print("Ingrese los datos del poliperro:")
    nombre = input("Nombre: ")
    huellaDactilar = input("Huella dactilar: ")

    tieneFoto = input("¿Tiene foto? (S/N): ").upper()

    if tieneFoto == "S":
        rutaOriginal = input("Ingrese la ruta de la foto: ")
        imagen = Image.open(rutaOriginal)
    else:
        imagen = Image.open("dog.png")

    rutaGuardada = f"BDDPERROS/poliperro_{random.randint(1,1000)}.png"
    imagen.save(rutaGuardada)

    datosPoliperros["Nombre"].append(nombre)
    datosPoliperros["huellaDactilar"].append(huellaDactilar)
    datosPoliperros["foto"].append(rutaGuardada)

    archivo.write(f"{nombre} -- {huellaDactilar} -- {rutaGuardada}\n")
    archivo.close()

    print("Poliperro registrado correctamente")

# ---------------- MOSTRAR TODOS ----------------
def mostrar():
    if not datosPoliperros["Nombre"]:
        print("No hay poliperros registrados")
        return

    for i in range(len(datosPoliperros["Nombre"])):
        print("-------------------------")
        print("Nombre:", datosPoliperros["Nombre"][i])
        print("Huella Dactilar:", datosPoliperros["huellaDactilar"][i])
        imagen = Image.open(datosPoliperros["foto"][i])
        imagen.show()

# ---------------- BUSCAR UNO ----------------
def buscar():
    nombreBuscado = input("Ingrese el nombre del poliperro: ")

    if nombreBuscado in datosPoliperros["Nombre"]:
        i = datosPoliperros["Nombre"].index(nombreBuscado)
        print("Poliperro encontrado")
        print("Nombre:", datosPoliperros["Nombre"][i])
        print("Huella:", datosPoliperros["huellaDactilar"][i])
        Image.open(datosPoliperros["foto"][i]).show()
    else:
        print("Poliperro no encontrado")

# ---------------- MAIN ----------------
def main():
    opcion = 0
    while opcion != 4:
        opcion = menu()

        match opcion:
            case 1:
                registro()
            case 2:
                mostrar()
            case 3:
                buscar()
            case 4:
                print("Saliendo del sistema...")
                time.sleep(2)
            case _:
                print("Opción inválida")
                time.sleep(1)

main()
