The detailed tutorial is here https://software.intel.com/en-us/articles/connecting-the-intel-edison-board-to-your-android-phone-with-serial-port-profile-spp
but the good news is, I have tested it and it works like a charm!

Few commands to follow:
1. ```python SPP-loopback.py &
 ``` 
2. ``` rfkill unblock bluetooth

bluetoothctl
```
3.``` scan on
 ```
4. ```pair MACIDHERE ```
5.```discoverable on ```
6. ``` trust MACIDHERE ```

