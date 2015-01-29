import pyupm_i2clcd as lcd
import mraa
import time
import requests
#display lcd code
lcdDisplay= lcd.Jhd1313m1(0,0X3E,0X62)

#Break the string to print in two lines
def lcdValprint(string):
        lcdDisplay.clear()
        time.sleep(1)
        print "lenght of string is "
        print (len(string))
        if (len(string)>16):

                #display the first 16 characters in line 1

                lcdDisplay.setCursor(0,0)
                lcdDisplay.write(string[0:15])
                print "String 1 is: "
                print (string[0:15])
                # Display the next 16 character in the next line
                lcdDisplay.setCursor(1,0)
                lcdDisplay.write(string[15:])
                print "String 2 is"
                print (string[16:])


        else:

                lcdDisplay.setCursor(0,0)
                lcdDisplay.write(string)
                print string

#Declaring Pins for Intel Edison
x = mraa.Gpio(5) #pin 5 Trigger
x.dir(mraa.DIR_OUT) #Declared as output
y = mraa.Gpio(6) #pin 6 Echo Pin
y.dir(mraa.DIR_IN) #Declared as Input

lcdValprint("Checking if this works")
while True:
#establish the duration of the pings and distance

x.write(0)
time.sleep(0.0001)
x.write(1)
time.sleep(0.0005)

print(y.read())


