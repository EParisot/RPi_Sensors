import RPi.GPIO as GPIO

IrPin  = 14

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IrPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def callback(ev=None):
    print('Received infrared.')

def loop():
    GPIO.add_event_detect(IrPin, GPIO.FALLING, callback=callback) # wait for falling
    while True:
        pass   # Don't do anything

def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()