import tkinter as tk
import paho.mqtt.client as mqtt
import threading

led1 = "OFF"
led2 = "OFF"

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
    global led1
    enviar_mensaje("1", led1 if led1 == "ON" else "OFF")
    led1 = "ON" if led1 == "OFF" else "OFF"

def modificar_led2():
    global led2
    enviar_mensaje("2", led2 if led2 == "ON" else "OFF")
    led2 = "ON" if led2 == "OFF" else "OFF"

def subscribe(client: mqtt):
	def on_message(client, userdata, msg):
		global led1
		global led2
		print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
		payload = int(msg.payload.decode())*2
		if payload > 500:
			enviar_mensaje("1", "ON")
			led1 = "ON"
			enviar_mensaje("2", "OFF")
			led2 = "OFF"
                  
		if payload < 500:
			enviar_mensaje("2", "ON")
			led2 = "ON"
			enviar_mensaje("1", "OFF")
			led1 = "OFF"

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

btn_detener = tk.Button(root, text="Modo 1", command=stop_thread)
btn_detener.pack()

btn_cambiar = tk.Button(root, text="Modo 2", command=start_thread)
btn_cambiar.pack()


# Configurar cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "puesto6")

client.connect(broker_address, port)

root.mainloop()
