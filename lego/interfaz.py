import tkinter as tk
import threading
import city_map as cm
import main as main
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe
from tkinter import PhotoImage
from PIL import Image,ImageTk

# Configuración MQTT
#broker_address = "192.168.48.245"
broker_address = "localhost"
port = 1883
user = "TP-LINK_7794"
password = "00280549"
topic="GRUPOJ/#"
map_received = False
mapCode = ""
mapNotMQTT = "0202000105030705000200041109060110031000000200080101100110000106010701"
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, "GRUPOJ")

puntosEntrega= []
lista_imagenes=[]

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, "GRUPOJ")
    client.on_connect = on_connect
    client.connect(broker_address, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def on_message(client,userdata,msg):
    if(msg.topic == "GRUPOJ/posicion"):
        
        tableroLEGO.dibujarTablero()
        #tableroLEGO.localizarLEGO(x,y)

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

# función para mandar mensajes
def enviar_mensaje(topic):
    coord=puntosEntrega.pop()
    coord_str = [str(x) for x in coord]
    cadena=', '.join(coord_str)
    
    try:
        client.publish(topic, cadena)
    except Exception as e:
        print("Error al publicar el mensaje:", e)

def start_mqtt_thread():
    mqtt_thread = threading.Thread(target=run, daemon=True)
    mqtt_thread.start()

def recoge_mensaje():
    msg = subscribe.simple("GRUPOJ/posicion", hostname=broker_address, port=port)
    return msg

# función para mostrar los puntos de entrega seleccionados
def muestraPtosEntrega():
    # Limpiar widgets de Label existentes
    cityMap = cm.CityMap(mapNotMQTT)
    for widget in frame_puntos_entrega.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for fila in range(len(puntosEntrega)):
        #if(cityMap.get_codes(puntosEntrega[fila])):
        enunciado=tk.Label(frame_puntos_entrega, text=f"Punto de entrega seleccionado: {puntosEntrega[fila]}")
        enunciado.pack()

# función para recoger las coordenadas del boton pulsadas
def anadePtos(coordenada):
    
    puntosEntrega.append(coordenada)
    muestraPtosEntrega()
    enviar_mensaje("GRUPOJ")

# función para pintar el mapa
# TODO: poner para que no se puedan seleccioanr los ptos en los que no se pueda entregar
def paintMap():
    cityMap = cm.CityMap(mapNotMQTT)

    # Crear una matriz de botones
    matriz_botones = []
    for fila in range(len(cityMap.cityMap)):
        fila_botones = []
        for columna in range(len(cityMap.cityMap[fila])):
            #coordenadas = cityMap.get_codes(fila,columna)
            
            codigo=cityMap.get_c(fila,columna)
            
            img = Image.open(f'imagenes/{codigo}.png')
            img = img.resize((50, 50), Image.LANCZOS) # Redimension (Alto, Ancho)
            photo = ImageTk.PhotoImage(img)

            boton = tk.Button(frame,image=photo, command=lambda coord=[fila,columna]: anadePtos(coord))
            boton.grid(row=fila, column=columna)

            fila_botones.append(boton)
            lista_imagenes.append(photo)
        matriz_botones.append(fila_botones)

class Tablero(tk.Canvas):
    def __init__(self, master, filas, columnas, size, **kwargs):
        self.filas = filas
        self.columnas = columnas
        self.size = size
        self.piezas = {}  # Diccionario para mantener referencia de las piezas

        width = columnas * size
        height = filas * size
        super().__init__(master, width=width, height=height, **kwargs)
        self.dibujarTablero()
        self.pack()

    def dibujarTablero(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                color = "white"
                x1 = columna * self.size
                y1 = fila * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.create_rectangle(x1, y1, x2, y2, fill=color)
    
    def localizarLEGO(self, fila, columna):
        x = columna * self.size + self.size / 2
        y = fila * self.size + self.size / 2
        pieza_id = self.create_oval(x - self.size / 4, y - self.size / 4, x + self.size / 4, y + self.size / 4)
        self.piezas[(fila, columna)] = pieza_id
    

start_mqtt_thread()

ventana = tk.Tk()
ventana.title("LesGooo")
ventana.geometry("700x900")

LARGEFONT = ("Verdana", 20)

enunciado = tk.Label(ventana, text="Seleccione el punto de entrega")
enunciado.pack()

#frame para contener los botones
frame = tk.Frame(ventana)
frame.pack()

# frame para los ptos de entrega
frame_puntos_entrega = tk.Frame(ventana)
frame_puntos_entrega.pack()

tableroLEGO= Tablero(ventana, filas=7,columnas=5,size=40)
tableroLEGO.pack()

paintMap()

ventana.mainloop()
