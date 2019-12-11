import RPi.GPIO as GPIO
import time

IrPin  = 23

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IrPin, GPIO.OUT)

def loop():
    while True:
        GPIO.output(IrPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(IrPin, GPIO.LOW)
        time.sleep(1)

def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
