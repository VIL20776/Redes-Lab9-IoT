import numpy as np
import random

def generate_gaussian_value(media, desviacion, a, b):
    while True:
        x = np.random.normal(media, desviacion)
        if a <= x <= b:
            return x

def generate_data() -> tuple:
    temp = float(generate_gaussian_value(20, 5, 0, 110))
    hum = int(generate_gaussian_value(50, 10, 0, 100))
    dir = random.choice(['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE'])
    
    return (temp, hum, dir)

if __name__ == "__main__":
    for _ in range(10):
        temp, hum, dir = generate_data()
        print(f"Temperature: {temp}°C, Humidity: {hum}%, Direction: {dir}")