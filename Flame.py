import RPi.GPIO as GPIO

DO = 4
state = 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def callback(ev=None):
    global state
    if state == 1:
        state = 0
        print("FIRE")
    else:
        state = 1
        print("SAFE")

def loop():
    GPIO.add_event_detect(DO, GPIO.FALLING, callback=callback)
    while True:
        pass

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt: 
        pass    