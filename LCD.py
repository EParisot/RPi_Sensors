from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2,
              pin_rs=LCD_RS, pin_e=LCD_E,
              pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7])

lcd.write_string(u"  Raspberry Pi\r\n")
lcd.write_string(u"     Model 4")

time.sleep(2)
lcd.clear()

lcd.write_string(u"    Welcome\r\n")

time.sleep(3)

lcd.close(clear=True)
#GPIO.cleanup() 