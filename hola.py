from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led1 = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(25, Pin.OUT)
led4 = Pin(26, Pin.OUT)
led5 = Pin(27, Pin.OUT)
led6 = Pin(14, Pin.OUT)
led7 = Pin(12, Pin.OUT)
led8 = Pin(13, Pin.OUT)

while True:
  led1.on()
  sleep(0.5)
  led1.off()
  sleep(0.5)

  led2.on()
  sleep(0.5)
  led2.off()
  sleep(0.5)

  led3.on()
  sleep(0.5)
  led3.off()
  sleep(0.5)
    
  led4.on()
  sleep(0.5)
  led4.off()
  sleep(0.5)

  led5.on()
  sleep(0.5)
  led5.off()
  sleep(0.5)

  led6.on()
  sleep(0.5)
  led6.off()
  sleep(0.5)

  led7.on()
  sleep(0.5)
  led7.off()
  sleep(0.5)

  led8.on()
  sleep(0.5)
  led8.off()
  sleep(0.5)

  led8.on()
  sleep(0.5)
  led8.off()
  sleep(0.5)

  led7.on()
  sleep(0.5)
  led7.off()
  sleep(0.5)

  led6.on()
  sleep(0.5)
  led6.off()
  sleep(0.5)

  led5.on()
  sleep(0.5)
  led5.off()
  sleep(0.5)

  led4.on()
  sleep(0.5)
  led4.off()
  sleep(0.5)

  led3.on()
  sleep(0.5)
  led3.off()
  sleep(0.5)

  led2.on()
  sleep(0.5)
  led2.off()
  sleep(0.5)

  led1.on()
  sleep(0.5)
  led1.off()
  sleep(0.5)
