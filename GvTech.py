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

def checkCommandExists():
    r = requests.get("https://morning-brushlands-7219.herokuapp.com/")
    curValue = r.text
    if curValue == "none":
        return None
    else:
        return curValue
#Declaring Pins for Intel Edison
x = mraa.Gpio(3) #pin 3
x.dir(mraa.DIR_OUT)


def getSerialCommand(cmd):
    if "coffee" in cmd and "on" in cmd:
        lcdValprint("Coffee Machine Switched on")
        return "a"
    elif "coffee" in cmd and "off" in cmd:
        lcdValprint("Coffee Machine Switched off")
        return "b"
    elif "light" in cmd and "on" in cmd:
        x.write(1)
        lcdValprint("Lights Switched on")
        return "c"
    elif "light" in cmd and "off" in cmd:
        x.write(0)
        lcdValprint("Lights Switched off")
        return "d"

while True:
    val = checkCommandExists()
    if val != None:
        s = getSerialCommand(val)

lcdValprint("Controlling Lights")


