import RPi.GPIO as GPIO
import time


LED_PIN = 18  
BUTTON_PIN = 17  


GPIO.setmode(GPIO.BCM)  
GPIO.setup(LED_PIN, GPIO.OUT)  
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)  
        if button_state == GPIO.LOW:  
            GPIO.output(LED_PIN, GPIO.LOW)  
            print("LED is OFF")
        else:
            GPIO.output(LED_PIN, GPIO.HIGH)  
            print("LED is ON")
        time.sleep(0.1)  

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    GPIO.cleanup()  
    print("GPIO cleaned up.")
