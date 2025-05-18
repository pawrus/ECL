import BlynkLib
import RPi.GPIO as GPIO

BLYNK_AUTH = ''

blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud")

LED_PIN = 4 

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW) 

@blynk.on("V2")
def control_led(value):
    if int(value[0]) == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
    else:
        GPIO.output(LED_PIN, GPIO.LOW) F
        print("LED OFF")


while True:
    blynk.run()

