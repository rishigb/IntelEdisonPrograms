Project Voice :
It is an attempt at controlling device with voice controlled Mobile App (android app in this case). This project has been tested with Intel Edison (kickass as it is), with a few hurdles here and there. I am writing this document to make sure you can installed the required packages required here without a lot of pain. All this has been done on Yocto Linux , this was the default linux that was loaded on the edison.

Python 2.7 comes installed. You will need Requests and Mraa modules to be imported. The funny thing is pip doesn't work, nor does apt-get. So we will install things like a hacker does it.

We will use a command called curl.

To install Requests, do this 

curl -O https://pypi.python.org/packages/source/r/requests/requests-2.5.1.tar.gz#md5=c270eb5551a02e8ab7a4cbb83e22af2e 

The above is going to point to the download address in the requests page, to do the same with some other package you want to install, do this :
1. Go to the package page and hover on the download button, right click and copy the link address. All you have to do now is 
curl -O linkAddress



You can also use wget to do the same, but since it does not work on https that easy, I had to install another version of wget. I will share more details on that soon.