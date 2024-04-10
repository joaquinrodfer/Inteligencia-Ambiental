import tkinter as tk
import paho.mqtt.client as mqtt

# Configuración MQTT
broker_address = "192.168.0.100"
port = 1883
user = "TP-LINK_7794"
password = "00280549"

def enviar_mensaje(led, estado):
    topic = f"A3-467/puesto6/led{led}"
    print(topic)
    client.publish(topic, estado)

def encender_led1():
    enviar_mensaje("1", "ON")

def encender_led2():
    enviar_mensaje("2", "OFF")

def apagar_led1():
    enviar_mensaje("1", "ON")

def apagar_led2():
    enviar_mensaje("2", "OFF")

# Creamos una ventana
root = tk.Tk()
root.title("Control de LEDs")
root.geometry("200x100")

# Botones para LED 1
btn_led1_on = tk.Button(root, text="ENCENDER LED 1", command=encender_led1)
btn_led1_on.pack()
btn_led1_on = tk.Button(root, text="APAGAR LED 1", command=apagar_led1)
btn_led1_on.pack()

# Botones para LED 2
btn_led2_on = tk.Button(root, text="ENCENDER LED 2", command=encender_led2)
btn_led2_on.pack()
btn_led2_on = tk.Button(root, text="APAGAR LED 2", command=apagar_led2)
btn_led2_on.pack()


# Configurar cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "puesto6")

client.connect(broker_address, port)
client.loop_start()

root.mainloop()
