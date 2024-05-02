from city_map import CityMap
import paho.mqtt.client as mqtt

broker_address = "192.168.48.245"
port = 1883
user = "TP-LINK_7794"
password = "00280549"
topic = "map"
map_received = False
mapCode = ""
mapNotMQTT = "0202000105030705000200041109060110031000000200080101100110000106010701"

def run(client: mqtt):
    while not map_received:
        subscribe(client)
        client.loop()

def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        global map_received
        map_received = True
        global mapCode
        mapCode = msg.payload.decode()

    client.subscribe(topic)
    client.on_message = on_message

def main():
    #En caso de no estar conectado a MQTT
    city = CityMap(mapNotMQTT)


    # client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "puesto6")
    # client.connect(broker_address, port)
    # run(client)
    # city = cityMap(mapCode)

    print(city.find_quickest_path((6, 0), (3, 0)))

if __name__ == "__main__":
    main()