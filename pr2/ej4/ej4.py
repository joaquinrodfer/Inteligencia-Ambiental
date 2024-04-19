import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe

broker_address = "192.168.48.245"
port = 1883
topic = "A3-467/puesto6/potenciometro"
client_id = "puesto6"
user = "TP-LINK_7794"
password = "00280549"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, "puesto6")
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


def enviar_mensaje(led, estado):
    topic = f"A3-467/puesto6/led{led}"
    client.publish(topic, estado)


def modificar_led1():
    enviar_mensaje("1", "1")


def modificar_led2():
    enviar_mensaje("2", "2")


def suscribir():
    msg = subscribe.simple("A3-467/puesto6/potenciometro", hostname=broker_address, port=port)
    print("%s %s" % (msg.topic, msg.payload))


LARGEFONT = ("Verdana", 20)

client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, "puesto6")


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Modo 1", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Modificar led 1", command=modificar_led1)
        button1.grid(row=1, column=0, padx=10, pady=10)
        button1 = ttk.Button(self, text="Modo 2", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Modificar led 2", command=modificar_led2)
        button2.grid(row=1, column=2, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Modo 2", font=LARGEFONT)
        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Modificar led 1", command=modificar_led1)
        button1.grid(row=1, column=0, padx=10, pady=10)
        button1 = ttk.Button(self, text="Modo 1", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="Modificar led 2", command=modificar_led2)
        button2.grid(row=1, column=2, padx=10, pady=10)
        run


# Driver Code
app = tkinterApp()
app.mainloop()
