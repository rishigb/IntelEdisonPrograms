# IntelEdisonPrograms

The above code has been written and tested on Intel Edison, the powerful product from Intel. 
I am using the grove sensor kit which is equipped with various sensors and the LCDs used above are RGB LCDs and have I2C connections.
You might need additional dependencies to make things work but most of them can be found in the resources provided by the 
intel edison website. Upmaa and Mraa have been written in C++, but since I love python, I have used the python wrapper to code the projects.
Use the following links to get started:
1. https://github.com/intel-iot-devkit/mraa 
2. https://github.com/intel-iot-devkit/upm
3. http://iotdk.intel.com/docs/master/mraa/python/

Install python modules using this curl -O (link address)

example curl - O https://pypi.python.org/packages/source/r/requests/requests-2.5.1.tar.gz#md5=c270eb5551a02e8ab7a4cbb83e22af2e for python requests

I am trying to keep the code clean, in case there are any doubts or any explanation is needed, feel free to get in touch.
A few things you should know before getting started. Edison gets clogged up rather easily, for example, if you have installed a lot of modules, there won't be any free space and you are going to suffer a lot trying to figure out what has gone wrong. Do see the other document to troubleshoot this.
