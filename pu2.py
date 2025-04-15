import paho.mqtt.client as mqtt
import time
import random
import json

BROKER_URL = "crossover.proxy.rlwy.net"
BROKER_PORT = 57689
TOPIC = "sensor/datos"

# Callback de conexión
def on_connect(client, userdata, flags, rc):
    print(f"Conexión establecida con código: {rc}")

# Crear el cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Conectar al broker
client.connect(BROKER_URL, BROKER_PORT, 60)

# Función principal para enviar datos
def main():
    while True:
        # Crear el mensaje con el formato solicitado
        datos = {
            "a11": random.randint(0, 1),
            "a12": random.randint(0, 1), 
            "s09": random.randint(0, 1),
            "s10": random.randint(0, 1),
            "s11": random.randint(0, 1),
            "s12": random.randint(0, 1024),
            "s13": random.randint(0, 1024),
            "s14": random.randint(0, 1024),
        }

        mensaje = json.dumps(datos)
        client.publish(TOPIC, mensaje)
        print(f"Mensaje enviado: {mensaje}")

        time.sleep(3)

# Ejecutar si es el archivo principal
if __name__ == "__main__":
    main()