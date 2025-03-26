import paho.mqtt.client as mqtt
import tkinter as tk

# Configuración MQTT
BROKER_URL = "crossover.proxy.rlwy.net"
BROKER_PORT = 57689
TOPIC = "sensor/datos1"

# Función para cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        status_label.config(text="Conectado al Broker", fg="green")
        client.subscribe(TOPIC)  # Nos suscribimos al topic para ver los mensajes
    else:
        status_label.config(text="Error de conexión", fg="red")

# Función para manejar los mensajes recibidos
def on_message(client, userdata, msg):
    mensaje = msg.payload.decode()  # Decodificamos el mensaje recibido
    log_text.insert(tk.END, f" {msg.topic}: {mensaje}\n")  # Lo mostramos en la interfaz
    log_text.yview(tk.END)  # Desplazamos la vista para ver el último mensaje

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz MQTT - Mensajes Recibidos")

# Etiqueta de estado de conexión
status_label = tk.Label(ventana, text="Conectando al Broker...", font=("Arial", 14))
status_label.pack(pady=10)

# Área de texto para mostrar los mensajes recibidos
log_text = tk.Text(ventana, height=10, width=50, wrap=tk.WORD, font=("Arial", 12))
log_text.pack(pady=10)

# Configuración del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker
client.connect(BROKER_URL, BROKER_PORT, 60)

# Iniciar el cliente MQTT en un hilo separado
def iniciar_cliente_mqtt():
    client.loop_start()

# Iniciar la interfaz gráfica y la conexión MQTT
ventana.after(1000, iniciar_cliente_mqtt)
ventana.mainloop()
