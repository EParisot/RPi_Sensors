from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from datetime import datetime
import time

import Adafruit_DHT

LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2,
              pin_rs=LCD_RS, pin_e=LCD_E,
              pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7])

lcd.cursor_pos = (0, 0)
lcd.write_string(u"  Raspberry Pi")
lcd.cursor_pos = (1, 0)
lcd.write_string(u"     Model 4")
time.sleep(1)
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string(u"    Welcome\r\n")
time.sleep(1)
lcd.clear()

try:
    while True:
        lcd.cursor_pos = (0, 0)
        lcd.write_string(datetime.now().strftime("%d/%m/%Y %H:%M"))
        humidity, temperature = Adafruit_DHT.read_retry(11, 17)
        lcd.cursor_pos = (1, 0)
        lcd.write_string("T:%sC H:%s%%" % (temperature, humidity))
except:
    lcd.close(clear=True)
    GPIO.cleanup()