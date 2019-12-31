import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    print(humidity, temperature)