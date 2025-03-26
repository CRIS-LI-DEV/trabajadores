import paho.mqtt.client as mqtt

BROKER_URL = "crossover.proxy.rlwy.net"
BROKER_PORT = 57689
TOPIC = "sensor/datos1"

def on_connect(client, userdata, flags, rc):
    print(f"Conectado con código de resultado {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_URL, BROKER_PORT, 60)
client.loop_forever()
