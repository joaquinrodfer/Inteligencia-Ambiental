import tkinter as tk
import threading
import city_map as cm
import main as main
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe

# Configuración MQTT
broker_address = "192.168.48.245"
port = 1883
user = "TP-LINK_7794"
password = "00280549"
topic = "map"
map_received = False
mapCode = ""
mapNotMQTT = "0202000105030705000200041109060110031000000200080101100110000106010701"
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, "GRUPOJ")

puntosEntrega= []

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker_address, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

# función para mandar mensajes
def enviar_mensaje():
    coord=puntosEntrega.pop()
    coord_str = [str(x) for x in coord]
    cadena=', '.join(coord_str)
    print(cadena)
    topic = f"GRUPOJ"
    client.publish(topic, cadena)

# función para mostrar los puntos de entrega seleccionados
def muestraPtosEntrega():
    # Limpiar widgets de Label existentes
    for widget in frame_puntos_entrega.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for fila in range(len(puntosEntrega)):
        enunciado=tk.Label(frame_puntos_entrega, text=f"Punto de entrega seleccionado: {puntosEntrega[fila]}")
        enunciado.pack()

# función para recoger las coordenadas del boton pulsadas
def anadePtos(coordenada):
    cityMap = cm.CityMap(mapNotMQTT)
    x=coordenada[0]
    y=coordenada[1]
    #print(x,y)
    puntosEntrega.append(coordenada)
    muestraPtosEntrega()
    enviar_mensaje()

# función para pintar el mapa
# TODO: poner para que no se puedan seleccioanr los ptos en los que no se pueda entregar
def paintMap():
    cityMap = cm.CityMap(mapNotMQTT)
    # Crear una matriz de botones
    matriz_botones = []
    for fila in range(len(cityMap.cityMap)):
        fila_botones = []
        for columna in range(len(cityMap.cityMap[fila])):
            coordenadas = (fila,columna)
            boton = tk.Button(frame, text=f"{coordenadas}", command=lambda coord=[fila,columna]: anadePtos(coord))
            boton.grid(row=fila, column=columna)
            fila_botones.append(boton)
        matriz_botones.append(fila_botones)

ventana = tk.Tk()
ventana.title("LesGooo")
ventana.geometry("500x300")


LARGEFONT = ("Verdana", 20)

connect_mqtt()

enunciado = tk.Label(ventana, text="Seleccione el punto de entrega")
enunciado.pack()

#frame para contener los botones
frame = tk.Frame(ventana)
frame.pack()

# frame para los ptos de entrega
frame_puntos_entrega = tk.Frame(ventana)
frame_puntos_entrega.pack()

paintMap()

ventana.mainloop()