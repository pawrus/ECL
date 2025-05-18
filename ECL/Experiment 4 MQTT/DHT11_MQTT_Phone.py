import paho.mqtt.client as mqtt
import Adafruit_DHT
import time
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  

MQTT_BROKER = "" 
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        message = f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%"
        print("Sending:", message)
        client.publish(MQTT_TOPIC, message)  
    else:
        print("Failed to retrieve data from DHT11 sensor")

    time.sleep(5)
