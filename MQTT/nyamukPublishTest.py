#
# Nyamuk Publish Test
#

import sys
from nyamuk import nyamuk
import nyamuk.nyamuk_const as NC
from nyamuk import event

# Assign Server/Client/Payload details
server_ip = "test.mosquitto.org"
client_id = "test_client"
topic = "/nyamuk/test"
payload = "Horay, it works!"

# Connect to the MQTT Server
ny = nyamuk.Nyamuk(client_id, server = server_ip)
print "Connecting..."
rc = ny.connect()

# Check for a successful connection
if rc != NC.ERR_SUCCESS:
    print "Can't connect"
    sys.exit(-1)
print "Connected!"

# Publish the Payload
pb = ny.publish(topic, payload)

# Check for a successful publish
if pb:
    print "Publish Failed"
else:
    print "Publish Success!"
rc = ny.loop()