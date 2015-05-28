Ofcourse, by now you guys should know that version 2 of the firmware has been released. I am downloading it now.
By the release documents, it looks promising but then again, I am prepared for a crash again, you know because, well, Intel's first firmware did not turn out so well.

Here is a link to release notes: http://download.intel.com/support/edison/sb/edison_rn_332032009.pdf 

Quick update:
1. BT seems to have been fixed. Not sure if they have written python wrappers for it though.
2. There are still a lot of unresolved issues.
3. Intel has also come up with Flash tool Lite which will help a lot of flashing the Edison( it is a GUI). I will not be using it though. I will be using the good old commandline on the mac to achieve the same. This is not available for Mac OS X. They said it will be launched soon.

#Flashing the firmware

Please follow this link: https://software.intel.com/en-us/flashing-firmware-on-your-intel-edison-board-mac-os-x


1.Install Homebrew by entering the command:
```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" ```
2.Install dfu-util, coreutils, and gnu-getopt by entering the command:
```brew install dfu-util coreutils gnu-getopt```
Note: Steps 1 and 2 above need to be done only once on a system with Mac OS X.
Download the latest Yocto* complete image from the main Edison downloads page: https://software.intel.com/iot/hardware/edison/downloads.
Extract the contents of the image file.
In your terminal, navigate to the directory where you extracted the Linux image. For example:
```cd ~/Downloads/edison-image-ww36-14```
Flash your board by entering the command:
```./flashall.sh```
The script can take up to 5 minutes to complete the flashing process.
Plug the USB cable in to your board.



