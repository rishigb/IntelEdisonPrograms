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





To install cd nameOfFile

python setup.py install 




Thats all you need to do.
 
