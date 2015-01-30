import mraa
import requests
import json
import time

#Declare the flags
flag1 = 0 #Initializing the value globaly.
flag2 = 1 #This so that it enters the else statement in the while loop

#Link
link = "https://lit-caverns-9397.herokuapp.com/"

#Setting up the processor
# x = mraa.Gpio(pinNumber)
#x = dir(mraa.DIR_IN)
x = mraa.Gpio(2)
x.dir(mraa.DIR_IN)


#Setting up the cloud/server etc
def postRequest(inp):
        headers = {'content-type': 'application/json'} #All this mentioned in the documents
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
        if "s" in cmd:
                #postvalue This has to be in a particular format as shown below.
                postRequest({"value":"0"})
        if "o" in cmd:
                #postvalue This has to be in a particular format as shown below.
                postRequest({"value":"1"})


while True:
        #val =raw_input('Enter the value to be posted: ') #This is only for debu
        #cloudPost(val)
        val =  x.read()
        #print (val)
        if (val== 1 and flag1):
                #Use some flags here to make the code more efficient
                #post the value to cloud and trigger the change.
                cloudPost('o') #sends1
                flag1 = 0
                flag2 = 1
        elif(val == 0 and flag2):
                #Nothing in the cart yet
                cloudPost('s') #sends0
                flag2 = 0
                flag 1 = 1