# IoT Estación Meteorológica
Este proyecto es una implementación de una estación meteorológica basada en Internet de las Cosas (IoT), utilizando Apache Kafka para la transmisión de datos de sensores. La estación meteorológica simula sensores que envían datos de temperatura, humedad y dirección del viento hacia un servidor Kafka. Estos datos se consumen y se despliegan de manera gráfica en tiempo real.
## Tabla de Contenidos

- [Requisitos](#Requisitos) 
- [Estructura del Proyecto](#EstructuradelProyecto)
- [Configuración y Uso](#ConfiguraciónyUso)
- [Iniciar el Productor](#IniciarelProductor)
- [Iniciar el Consumidor](#IniciarelConsumidor)
- [Detalles Técnicos](#DetallesTécnicos)

## Requisitos
Antes de empezar, asegúrate de tener los siguientes elementos:
- Python 3.9 o superior
- Apache Kafka (servidor activo)
- Librerías de Python:
  - kafka-python o confluent-kafka
  - matplotlib
  - numpy

Puedes instalar las dependencias necesarias ejecutando:
```bash
  pip install kafka-python confluent-kafka matplotlib numpy
```
## Estructura del Proyecto
- main.py: Archivo principal para ejecutar el productor o consumidor.
- producer_module.py: Contiene la lógica del productor Kafka.
- consumer_module.py: Contiene la lógica del consumidor Kafka y la visualización de datos.
- encoding24.py: Módulo que contiene funciones para codificar y decodificar los datos de sensores en mensajes de 3 bytes.
- generator.py: Módulo que genera los datos simulados de los sensores (temperatura, humedad y dirección del viento).

## Configuración y Uso

Este proyecto permite elegir entre iniciar un productor que genera y envía datos de sensores o un consumidor que recibe y despliega estos datos.

### Iniciar el Productor

Para iniciar el productor, ejecuta main.py y selecciona la opción correspondiente:
```bash
python main.py
```
Cuando se te pregunte, ingresa 1 para iniciar el productor:
```bash
Seleccione la opción a ejecutar:
1. Iniciar Productor (Envío de Datos)
2. Iniciar Consumidor (Consumo y Despliegue de Datos)
Ingrese el número de la opción deseada: 1
```

### Iniciar el Consumidor

Para iniciar el consumidor, ejecuta main.py y selecciona la opción correspondiente:
```bash
python main.py
```
Cuando se te pregunte, ingresa 2 para iniciar el consumidor:
```bash
Seleccione la opción a ejecutar:
1. Iniciar Productor (Envío de Datos)
2. Iniciar Consumidor (Consumo y Despliegue de Datos)
Ingrese el número de la opción deseada: 2
```

El consumidor mostrará en tiempo real los datos recibidos en un gráfico con la temperatura y la humedad.

La idea seria tener dos terminales abiertas para que funcionen al mismo tiempo. Para parar tanto el productor como el consumidor, precione CTRL + C en cada terminal.

## Detalles Técnicos

### Productor

El productor genera datos de temperatura, humedad y dirección del viento utilizando distribuciones aleatorias para simular valores realistas.

Estos datos son codificados a un formato compacto de 3 bytes utilizando encoding24.py antes de ser enviados al servidor Kafka.

El productor envía datos al servidor Kafka cada 15 segundos.

### Consumidor

El consumidor se suscribe al topic del productor y recibe los mensajes de sensores en tiempo real.

Los datos recibidos se decodifican usando encoding24.py y se grafican usando matplotlib.

Los gráficos se actualizan automáticamente cada vez que se recibe un nuevo mensaje.
