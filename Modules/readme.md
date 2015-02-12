 Including all the modules I will be using the programs here and how to download them too.


1. Requests: 
 curl -OL https://github.com/kennethreitz/requests/tarball/master
 
to unpack it tar -xf nameOfFile


2. Paho mqtt client 

curl -OL https://pypi.python.org/packages/source/p/paho-mqtt/paho-mqtt-1.1.tar.gz

same as above to unpack


3. Mraa/Upma 

echo "src mraa-upm http://iotdk.intel.com/repos/1.1/intelgalactic" > /etc/opkg/mraa-upm.conf
opkg update
opkg install libmraa0

4. Mosquitto -- mqtt broker , for some reason I had more success with this than paho

curl -OL https://pypi.python.org/packages/source/m/mosquitto/mosquitto-1.2.3.tar.gz#md5=e25d3fb8eb258f7376c59f81870c78ca



To install cd nameOfFile

python setup.py install 




Thats all you need to do.
 
