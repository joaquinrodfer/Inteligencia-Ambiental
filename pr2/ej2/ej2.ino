#include <SPI.h>
#include <WiFi101.h>
#include <MQTT.h>

const char ssid[] = "TP-LINK_7794";
const char pass[] = "00280549";
bool led1 = false;
boolean led2 = false;
String numero;
WiFiClient net;
MQTTClient client;
unsigned long lastMillis = 0;

const char broker[] = "192.168.0.100";
int port = 1883;
const char topic1[] = "A3-467/puesto6/led1";
const char topic2[] = "A3-467/puesto6/led2";

void connect() {
    Serial.print("checking wifi...");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(1000);
    }
    Serial.println("\nConnected to WiFi!");

    Serial.print("\nConnecting to broker...\n");
   // while(!mqttClient.connect(broker, port)) {
     // Serial.print("MQTT failed\n");
     // delay(5000);
    //}

    while (!client.connect("mkr1000")){
        Serial.print(".");
        delay(1000);
    }


    Serial.println("\nConnected!");
    client.subscribe("A3-467/puesto6/led1");
    client.subscribe("A3-467/puesto6/led2");
}

void setup() {
  Serial.begin(9600);
    
    while (!Serial) {
        delay(10);
    }
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);
    Serial.println("Iniciando conexión wifi");
    WiFi.begin(ssid, pass);

    client.begin(broker,net);
    client.onMessage(messageReceived);
    
    connect();
}

void messageReceived(String &topic, String &payload) {
    if (topic = "A3-467/puesto6/led1") {
        if (payload = "ON") {
            digitalWrite(A0, HIGH);
            client.publish("A3-467/puesto6/led1", ";");
            Serial.println("Encendiendo Led1");
        } else if (payload = "OFF"){
            client.publish("A3-467/puesto6/led1", ";");
            Serial.println("Apagando Led1");
            digitalWrite(A0, LOW);
        }  
    } else if(topic = "A3-467/puesto6/led2") {
        if (payload = "ON") {
            digitalWrite(A0, HIGH);
            client.publish("A3-467/puesto6/led1", ";");
            Serial.println("Encendiendo Led1");
        } else if (payload = "OFF"){
            client.publish("A3-467/puesto6/led1", ";");
            Serial.println("Apagando Led1");
            digitalWrite(A0, LOW);
        }  
    }    
}



void loop() {
    client.loop();
    if (!client.connected()) {
        connect();
        delay(1000);
    }    
}
