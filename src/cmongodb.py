# -*- coding: utf-8 -*-

from pymongo import MongoClient

# Establecer conexion a MongoDB
cliente = MongoClient('mongodb://localhost:27017/vuelos')
db = cliente.vuelos
coleccion = db.reservas

# Funcion para crear una reserva de vuelo
def crear_reserva():
    nombre_pasajero = raw_input("Ingrese el nombre del pasajero: ")  # Cambio de input a raw_input
    numero_vuelo = raw_input("Ingrese el numero de vuelo: ")  # Cambio de input a raw_input
    origen = raw_input("Ingrese el origen del vuelo: ")  # Cambio de input a raw_input
    destino = raw_input("Ingrese el destino del vuelo: ")  # Cambio de input a raw_input
    fecha = raw_input("Ingrese la fecha del vuelo (YYYY-MM-DD): ")  # Cambio de input a raw_input
    asiento = raw_input("Ingrese el asiento reservado: ")  # Cambio de input a raw_input

    reserva = {
        "nombre_pasajero": nombre_pasajero,
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "fecha": fecha,
        "asiento": asiento
    }

    return coleccion.insert_one(reserva)

# Funcion para leer todas las reservas de vuelo
def obtener_todas_reservas():
    reservas = coleccion.find().sort("orden", 1)  # Orden ascendente por el campo "orden"
    for reserva in reservas:
        print("ID:", str(reserva["_id"]))
        print("Nombre pasajero:", str(reserva["nombre_pasajero"]))
        print("Numero de vuelo:", str(reserva["numero_vuelo"]))
        print("Origen:", str(reserva["origen"]))
        print("Destino:", str(reserva["destino"]))
        print("Fecha:", str(reserva["fecha"]))
        print("Asiento:", str(reserva["asiento"]))
        print()

# Funcion para leer una reserva de vuelo por nombre de pasajero
def obtener_reserva_por_pasajero():
    nombre_pasajero = raw_input("Ingrese el nombre del pasajero: ")  # Cambio de input a raw_input
    reserva = coleccion.find_one({"nombre_pasajero": nombre_pasajero})
    if reserva:
        return reserva
    else:
        return None

# Funcion para actualizar una reserva de vuelo por nombre de pasajero
def actualizar_reserva():
    nombre_pasajero = raw_input("Ingrese el nombre del pasajero: ")  # Cambio de input a raw_input
    nuevos_datos = {
        "numero_vuelo": raw_input("Ingrese el nuevo numero de vuelo: "),  # Cambio de input a raw_input
        "origen": raw_input("Ingrese el nuevo origen del vuelo: "),  # Cambio de input a raw_input
        "destino": raw_input("Ingrese el nuevo destino del vuelo: "),  # Cambio de input a raw_input
        "fecha": raw_input("Ingrese la nueva fecha del vuelo (YYYY-MM-DD): "),  # Cambio de input a raw_input
        "asiento": raw_input("Ingrese el nuevo asiento reservado: ")  # Cambio de input a raw_input
    }
    resultado = coleccion.update_one({"nombre_pasajero": nombre_pasajero}, {'$set': nuevos_datos})
    if resultado.modified_count > 0:
        print("Reserva actualizada correctamente.")
    else:
        print("No se encontro ninguna reserva con ese nombre de pasajero.")

# Funcion para eliminar una reserva de vuelo por nombre de pasajero
def eliminar_reserva():
    nombre_pasajero = raw_input("Ingrese el nombre del pasajero: ")  # Cambio de input a raw_input
    resultado = coleccion.delete_one({"nombre_pasajero": nombre_pasajero})
    if resultado.deleted_count > 0:
        print("Reserva eliminada correctamente.")
    else:
        print("No se encontro ninguna reserva con ese nombre de pasajero.")

# Funcion para mostrar los pasajeros que reservaron en un mes y ano especifico
def mostrar_pasajeros_por_mes_y_anio():
    mes = raw_input("Ingrese el mes (MM): ")
    anio = raw_input("Ingrese el anio (YYYY): ")
    reservas = coleccion.find({"fecha": {"$regex": "^{}-{}-".format(anio, mes)}})
    if reservas.count() > 0:
        print("Pasajeros que reservaron en {}-{}:".format(anio, mes))
        for reserva in reservas:
            print("Nombre pasajero:", str(reserva["nombre_pasajero"]))
    else:
        print("No hay reservas para el mes y anio especificados.")

# Ejemplos de uso
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Crear reserva de vuelo")
        print("2. Obtener todas las reservas de vuelo")
        print("3. Obtener reserva de vuelo por nombre de pasajero")
        print("4. Actualizar reserva de vuelo por nombre de pasajero")
        print("5. Eliminar reserva de vuelo por nombre de pasajero")
        print("6. (Consulta) Mostrar nombre pasajeros que reservaron en un mes y anio especifico")
        print("0. Salir")

        opcion = raw_input("\nIngrese el numero de la opcion que desea ejecutar: ")  # Cambio de input a raw_input
        opcion = int(opcion)

        if opcion == 1:
            crear_reserva()
            print("Reserva creada correctamente.")
        elif opcion == 2:
            print("Todas las reservas:")
            obtener_todas_reservas()
        elif opcion == 3:
            reserva = obtener_reserva_por_pasajero()
            if reserva:
                print("Reserva encontrada:")
                for key, value in reserva.items():
                    print('{}: {}'.format(key, value))
            else:
                print("No se encontro ninguna reserva con ese nombre de pasajero.")
        elif opcion == 4:
            actualizar_reserva()
        elif opcion == 5:
            eliminar_reserva()
        elif opcion == 6:
            mostrar_pasajeros_por_mes_y_anio()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor, ingrese un numero del menu.")

    # Cerrar la conexion
    cliente.close()
