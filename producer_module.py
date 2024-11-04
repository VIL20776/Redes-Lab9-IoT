from kafka import KafkaProducer
import time
from generator import generate_sensor_data
from encoding24 import encode_24

def start_producer():
    producer = KafkaProducer(
        bootstrap_servers='164.92.76.15:9092'
    )

    topic = '21471'

    try:
        while True:
            # Se generan los datos usando la funcion generate_data
            temp, hum, dir = generate_sensor_data()

            # Se codifican los datos a 3 bytes
            encoded_data = encode_24(temp, hum, dir)

            # Se envian los datos al broker Kafka
            producer.send(topic, value=encoded_data)
            print(f"Datos enviados (codificados): {encoded_data}")

            # Esperamos entre 15 y 30 segundos (puede variar para que se reciba mejor) para el siguiente envío
            time.sleep(15)
    except KeyboardInterrupt:
        print("Interrumpido. Cerrando productor.")
    finally:
        producer.close()
