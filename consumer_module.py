from kafka import KafkaConsumer
import matplotlib.pyplot as plt
from encoding24 import decode_24

def start_consumer():
    consumer = KafkaConsumer(
        '21471',
        group_id='grupo_consumer',
        bootstrap_servers='164.92.76.15:9092'
    )

    # Listas para almacenar las mediciones
    all_temp = []
    all_hume = []
    all_wind = []

    plt.ion()  # Modo interactivo
    fig, (ax1, ax2) = plt.subplots(2, 1)

    try:
        for mensaje in consumer:
            # Se decodifica el mensaje recibido usando la funcion decode_24
            temp, hum, dir = decode_24(mensaje.value)
            all_temp.append(temp)
            all_hume.append(hum)
            all_wind.append(dir)

            # Se grafican los datos en tiempo real
            ax1.clear()
            ax2.clear()

            ax1.plot(all_temp, label='Temperatura (°C)')
            ax2.plot(all_hume, label='Humedad (%)')

            ax1.legend()
            ax2.legend()

            # Forzar la actualización de la gráfica
            plt.draw()
            plt.gcf().canvas.flush_events()
            plt.pause(0.5)  # Aumentar el tiempo de pausa para asegurar la actualización
    except KeyboardInterrupt:
        print("Interrumpido. Cerrando consumidor.")
    finally:
        plt.ioff()
        plt.show()

