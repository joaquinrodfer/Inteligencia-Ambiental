import tkinter as tk
import paho.mqtt.client as mqtt
import threading

# Configuración MQTT
broker_address = "192.168.48.245"
port = 1883
user = "TP-LINK_7794"
password = "00280549"
topic = "A3-467/puesto6/potenciometro"

def enviar_mensaje(led, estado):
    topic = f"A3-467/puesto6/led{led}"
    print(topic)
    client.publish(topic, estado)

def modificar_led1():
    enviar_mensaje("1", "1")

def modificar_led2():
    enviar_mensaje("2", "2")

def subscribe(client: mqtt):
	def on_message(client, userdata, msg):
		print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
		if int(msg.payload.decode()) > 500:
			enviar_mensaje("1", "ON")
			enviar_mensaje("2", "OFF")

	client.subscribe(topic)
	client.on_message = on_message

def run():
    global running
    running = True
    while running:
        subscribe(client)
        client.loop()

def start_thread():
    global thread
    thread = threading.Thread(target=run)
    thread.start()

def stop_thread():
    global running
    running = False

# Creamos una ventana
root = tk.Tk()
root.title("Control de LEDs")
root.geometry("200x150")

# Botones para LED 1
btn_led1_on = tk.Button(root, text="ENCENDER LED 1", command=modificar_led1)
btn_led1_on.pack()

# Botones para LED 2
btn_led2_on = tk.Button(root, text="ENCENDER LED 2", command=modificar_led2)
btn_led2_on.pack()

btn_cambiar = tk.Button(root, text="Cambiar modo", command=start_thread)
btn_cambiar.pack()

btn_detener = tk.Button(root, text="Detener modo", command=stop_thread)
btn_detener.pack()

# Configurar cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "puesto6")

client.connect(broker_address, port)

root.mainloop()
