import RPi.GPIO as GPIO

DO = 4

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def callback(ev=None):
    print("TOUCH")

def loop():
    GPIO.add_event_detect(DO, GPIO.FALLING, callback=callback, bouncetime=200)
    while True:
        pass

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt: 
        pass