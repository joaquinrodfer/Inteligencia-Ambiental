from city_map import cityMap
import paho.mqtt.client as mqtt

broker_address = "192.168.48.245"
port = 1883
user = "TP-LINK_7794"
password = "00280549"
topic = "map"

def run(client: mqtt):
    while True:
        subscribe(client)
        client.loop()

def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
    

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "puesto6")
    client.connect(broker_address, port)

    run(client)

if __name__ == "__main__":
    main()