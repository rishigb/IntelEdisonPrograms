import time
import requests
import json

link ="https://lit-caverns-9397.herokuapp.com/"

#Response Code checking Step #2
def checkResponse():
        r = requests.get(link)
        curValue = r.status_code
        #print curValue
        if (curValue==200):
                print "Value Posted"
        else:
                print "Error Response Code",curValue

#Write A function to post requests Step#1
def postRequest(inp):
        headers = {'content-type': 'application/json'} #All provided in the docu
        r = requests.post(link,data=json.dumps(inp),headers = headers) #All this
        print (r.text)
        checkResponse()

#The code below is to post to a link, it has to be in the way written below. For
def cloudPost(cmd):
        if "s" in cmd:
                #postvalue This has to be in a particular format as shown below.
                postRequest({"value":"0"})
        if "o" in cmd:
                #postvalue This has to be in a particular format as shown below.
                postRequest({"value":"1"})
#CALL ALL THE FUNCTIONS
while True:
        #Read the serial monitor
        val = raw_input("Enter some value here s or o : ")
        #print val
        cloudPost(val)
