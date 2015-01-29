#hcsr04.py
 
import pyupm_i2clcd as lcd
import mraa
import time
import sys
 
# display - lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
 
# digital output - trig
trigPin = mraa.Gpio(5)
trigPin.dir(mraa.DIR_OUT)
trigPin.write(0)
 
# digital input - echo
echoPin = mraa.Gpio(6)
echoPin.dir(mraa.DIR_IN)
 
time.sleep(0.3)
 
trigPin.write(1)
time.sleep(0.00001)
trigPin.write(0)
 
while echoPin.read() == 0:   
 
    pulseOff = time.time()
   
while echoPin.read() == 1:
 
    pulseOn = time.time()
   
timeDifference = pulseOn - pulseOff
centimeters = timeDifference * 17000
print centimeters
centimetersStr = str(centimeters)
lcdDisplay.setCursor(0, 0)
lcdDisplay.write(centimetersStr)