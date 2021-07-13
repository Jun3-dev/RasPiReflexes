import RPi.GPIO as GPIO
import random
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT)


waitTime = random.randint(1,10)

#time.sleep()

for i in range(0,10):
    GPIO.output(25,GPIO.HIGH)
    print("LED On")
    time.sleep(1/(1+i))
    GPIO.output(25,GPIO.LOW)
    time.sleep(waitTime)

while True:
    if GPIO.input(4)==GPIO.HIGH:
        print("Button Pressed!")
