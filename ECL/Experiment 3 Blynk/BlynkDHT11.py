import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import Adafruit_DHT
import time
import socket  


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
BLYNK_AUTH_TOKEN = ''


blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN, server="blynk.cloud")


timer = BlynkTimer()

@blynk.on("connected")
def blynk_connected():
    print("You have connected to Blynk")

def myData():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        blynk.virtual_write(0, temperature)
        blynk.virtual_write(1, humidity)
        print("Values sent to Blynk Server!")
    else:
        print("Sensor failure")

timer.set_interval(2, myData)


while True:
    blynk.run()
    timer.run()
    time.sleep(0.1)  
