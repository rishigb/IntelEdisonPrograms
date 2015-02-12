from mosquitto import Mosquitto
publish_key = "pub-c-7f5b7bb7-2111-43d0-8442-ade8ca712f07" 
subscribe_key = "sub-c-c673b326-d4a0-11e3-b488-02ee2ddab7fe" 
channel_name = "hello_world" 
client_uuid = "1ddb86ef5" 
mqtt_hostname = "mqtt.pubnub.com" 
mqtt_connect = publish_key + "/" + subscribe_key + "/" + client_uuid 
mqtt_topic = publish_key + "/" + subscribe_key + "/" + channel_name 
mosq_object = Mosquitto(mqtt_connect) 
mosq_object.connect(mqtt_hostname) 
mosq_object.publish( mqtt_topic, "But why won't this work man?" )
