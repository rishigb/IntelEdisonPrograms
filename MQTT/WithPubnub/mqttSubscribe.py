from mosquitto import Mosquitto 
publish_key = "pub-c-7f5b7bb7-2111-43d0-8442-ade8ca712f07" 
subscribe_key = "sub-c-c673b326-d4a0-11e3-b488-02ee2ddab7fe" 
channel_name = "hello_world" 
client_uuid = "2fb96def5"
mqtt_hostname = "mqtt.pubnub.com" 
mqtt_connect = publish_key + "/" + subscribe_key + "/" + client_uuid 
mqtt_topic = publish_key + "/" + subscribe_key + "/" + channel_name 
mosq_object = Mosquitto(mqtt_connect) 
def on_message( mosq, obj, msg ): 
	print( msg.payload, msg.topic ) 
mosq_object.on_message = on_message 
mosq_object.connect(mqtt_hostname) 	
mosq_object.subscribe(mqtt_topic)
mosq_object.loop_forever() 
