import RPi.GPIO as GPIO

ObstaclePin = 17

def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def callback(ev=None):
    print("Detected")

def loop():
    GPIO.add_event_detect(ObstaclePin, GPIO.FALLING, callback=callback) # wait 
    while True:
        pass

def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()