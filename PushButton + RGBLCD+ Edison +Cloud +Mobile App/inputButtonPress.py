'''Use the following code to send values, updates, names, presence status and much more, to the cloud using intel edison '''

import pyupm_i2clcd as lcd
import mraa
import time

#Products
plist = ["sugar","flour","salt","toilet paper","tooth-paste","mouth-wash"]

#Buttons
x = mraa.Aio(0)

#display lcd code
lcdDisplay= lcd.Jhd1313m1(0,0X3E,0X62)

#Break the string to print in two lines
def lcdValprint(string):
    lcdDisplay.clear()
    time.sleep(1)
    # print "lenght of string is "
    # print (len(string))
    if (len(string)>16):
        lcdDisplay.setCursor(0,0)
        lcdDisplay.write(string[0:15])
        #print "String 1 is: "
        #print (string[0:15])
        # Display the next 16 character in the next line
        lcdDisplay.setCursor(1,0)
        lcdDisplay.setCursor(1,0)
        lcdDisplay.write(string[15:])
        #print "String 2 is"
        #print (string[16:])
    else:
        lcdDisplay.setCursor(0,0)
        lcdDisplay.write(string)
        print string
#Flags for the following function
flagH = 0
flagL = 0
#Function to read value and take an action
def checkButtonInp (buttonNumber, product):
    inpStatus = (mraa.Aio(buttonNumber)).read()
        if(inpStatus>50) and (flagL == 0):
                globals()['flagH'] = 0 #This is a beautiful
                globals()['flagL'] = 1 #Using a global variable locally and changin the values
                time.sleep(0.5)
                lcdValprint("Sending value")
                #send value to the cloud
                cloudPost(product)
                time.sleep(0.5)
                lcdValprint("List updated")
                lcdValprint(product)
                time.sleep(0.5)
        elif (inpStatus<10) and (flagH == 0):
                globals()['flagL'] = 0
                globals()['flagH'] = 1
                lcdDisplay.clear()
                print "Still waiting"

#Function to send some values to the cloud
link= "https://secure-anchorage-4352.herokuapp.com/number"
#link  = "http://localhost:3000/number"
def postRequest(inp):
    headers = {'content-type': 'application/json'} #All this mentioned in th
        r = requests.post(link,data=json.dumps(inp),headers = headers)
        print (r.text)
        checkResponse()
def checkResponse():
    r = requests.get(link)
        curValue = r.status_code
        #print curValue
        if (curValue==200):
            print "Value Posted"
        else:
            print "Error Response Code",curValue
def cloudPost(cmd):
    postRequest({"value":cmd})



while True:
    #lcdValprint(raw_input('Enter some text here ')) # Using this we can display
    checkButtonInp (0,pList[0])
    checkButtonInp (1,pList[1])

