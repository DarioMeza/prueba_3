import os
import globales
import random
import json
os.system("cls")
def asignar_montos():
    productos = [
    "Café Americano",
    "Té Chai",
    "Croissant",
    "Jugo Naranja",
    "Panini de Pavo y Queso",
    "Pastel de Zanahoria",
    "Espresso Doble",
    "Ba;do de Frutas",
    "Muffin",
    "Ensalada",
    "Chocolate Caliente",
    "Tarta de Frambuesa",
    "Sándwich de Huevo",
    "Galletas de Avena",
    "Frappé de Caramelo"
    ]
    productos_precio = []
    for producto in productos:
        valor = random.randint(2000, 10000)
        valor_producto = {
            "nombre": producto,
            "valor": valor,
            "iva": (valor / 100) * 0.19
            }
        productos_precio.append(valor_producto)
    globales.guardar_archivo_json("valores.json", productos_precio)

def ver_estadisticas():
    productos_precio = globales.leer_archivo_json("valores.json")
    valores = [producto["valor"] for producto in productos_precio]
    iva = [producto["iva"] for producto in productos_precio]
    valor_max = max(valores)
    iva_min = max(iva)
    valor_promedio = sum(valores) / len(valores)

    print(valor_max)
    print(iva_min)
    print(valor_promedio)


def iniciar_menu():
    while True:
        print("1. Asignar Montos Aleatorias")
        print("2. Ver Estadisticas")
        print("3. Salir")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            asignar_montos()
        elif opcion == 2:
            ver_estadisticas()
        elif opcion == 3:
            False


__name__ == "__main__"
iniciar_menu()