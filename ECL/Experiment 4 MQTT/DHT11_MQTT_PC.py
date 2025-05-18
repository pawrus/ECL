import Adafruit_DHT
import paho.mqtt.client as mqtt
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 

MQTT_BROKER = "" 
MQTT_PORT = 1883
MQTT_TOPIC = "home/temperature_humidity"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        print(f"Temperature={temperature}C  Humidity={humidity}%")
        message = f"Temperature={temperature}C, Humidity={humidity}%"
        client.publish(MQTT_TOPIC, message)
    else:
        print("Failed to retrieve data from sensor.")
    
    time.sleep(2)
