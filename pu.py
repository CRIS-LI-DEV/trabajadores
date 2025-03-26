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
        # Generar el arreglo de diccionarios para 8 sensores con números de 5 dígitos
        sensores = [
            {"id": i, "valor": random.randint(10000, 99999)} for i in range(1, 9)
        ]

        # Crear el mensaje en formato JSON
        mensaje = json.dumps({"sensores": sensores})

        # Publicar el mensaje en el topic
        client.publish(TOPIC, mensaje)
        print(f"Mensaje enviado: {mensaje}")

        time.sleep(1)  # Espera 1 segundo antes de enviar otro mensaje

# Ejecutar el script solo si es el archivo principal
if __name__ == "__main__":
    main()
