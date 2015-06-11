# IntelEdisonPrograms using Python

The above code has been written and tested on Intel Edison, the powerful product from Intel. 
I am using the grove sensor kit which is equipped with various sensors and the LCDs used above are RGB LCDs and have I2C connections.
You might need additional dependencies to make things work but most of them can be found in the resources provided by the 
intel edison website. Upmaa and Mraa have been written in C++, but since I love python, I have used the python wrapper to code the projects.

Use the following links to get started:
1.Mraa from Intel Devkit [link]( https://github.com/intel-iot-devkit/mraa) .

2. UPM [link](https://github.com/intel-iot-devkit/upm) .

3. Source for python files [here](http://iotdk.intel.com/docs/master/mraa/python/) .

4. Find wiki [here](https://github.com/intel-iot-devkit/edison-guides/wiki) . 

5. Install pip using this: ```curl -OL https://bootstrap.pypa.io/get-pip.py``` .

5. Install git : ```opkg install git ```.
or follow [this] (https://github.com/intel-iot-devkit/edison-guides/wiki/Installing-Git-on-Intel-Edison) or just check the getting started document, there I have written the step by step process on how to get started.

For installing the various modules that you will need please look into the modules folder, all the modules being used and how to install them on edison is being documented there.

I am trying to keep the code clean, in case there are any doubts or any explanation is needed, feel free to get in touch.
A few things you should know before getting started. Edison gets clogged up rather easily, for example, if you have installed a lot of modules, there won't be any free space and you are going to suffer a lot trying to figure out what has gone wrong. Do see the other document to troubleshoot this.
#Socket IO intergration coming soon
#To Do
>1.Clean the documents
>2.Test cases
>3.Modules for python and Node
