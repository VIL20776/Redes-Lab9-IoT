import numpy as np
import random

def generate_gaussian_value(media, desviacion, a, b):
    while True:
        x = np.random.normal(media, desviacion)
        if a <= x <= b:
            return x

def generate_sensor_data(temp_media=20, temp_desviacion=5, hum_media=50, hum_desviacion=10):
    temp = float(generate_gaussian_value(temp_media, temp_desviacion, 0, 110))
    hum = int(generate_gaussian_value(hum_media, hum_desviacion, 0, 100))
    dir = random.choice(['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE'])
    
    return (temp, hum, dir)

# Este if permite que el código se ejecute solo si se ejecuta directamente
if __name__ == "__main__":
    for _ in range(10):
        temp, hum, dir = generate_sensor_data()
        print(f"Temperature: {temp}°C, Humidity: {hum}%, Direction: {dir}")
