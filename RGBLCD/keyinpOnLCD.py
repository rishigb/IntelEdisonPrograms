'''This code aims at displaying the user input on the LCD display by grove sensor kit (I2C).
The code will have two forms in the future, one to split the text and the next to make the text scroll on the LCD.
Code has been tested on Intel Edison with the Yocto Linux on 14th January 2015 by Rishi Gaurav Bhatnagar. 
Reach out : @rishigb or www.rishigauravbhatnagar.net '''

import pyupm_i2clcd as lcd
import mraa
import time

#display lcd code
lcdDisplay= lcd.Jhd1313m1(0,0X3E,0X62)

#Break the string to print in two lines
def lcdValprint(string):
    lcdDisplay.clear()
    time.sleep(1)
    print "lenght of string is "
    print (len(string))
    if (len(string)>16):
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

while True:
    lcdValprint(raw_input('Enter some text here ')) # Using this we can display the keyboard input on the LCD


