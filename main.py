from producer_module import start_producer
from consumer_module import start_consumer

def main():
    print("Seleccione la opción a ejecutar:")
    print("1. Iniciar Productor (Envío de Datos)")
    print("2. Iniciar Consumidor (Consumo y Despliegue de Datos)")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        start_producer()
    elif opcion == '2':
        start_consumer()
    else:
        print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
