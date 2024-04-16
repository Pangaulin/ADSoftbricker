# ADSoftbricker

This software is for educational purposes only, I am not responsible of any damage made on your phone. This software was tested on Windows 10 and Windows 11 with Python 3.12, on a Samsung A03

## How to start the program

In a command line, type :

```bash
  git clone https://github.com/Pangaulin/ADSoftbricker
  cd ADSoftbricker
  python main.py
```
Or : 
- Download source code
- Extract it with WinRAR, 7-Zip, on an other data compression and archiving software
- Launch the **start.bat** file

Then, enjoy !
## How to use USB Debug
After starting the software, you have two choices
```bash
USB Debug (1)
Wireless Debug (2)
```
If you choose USB debug, check if it's activated on your phone, here is a [tutorial](https://developer.android.com/studio/debug/dev-options?hl=en#enable). 

After this, plug the device to you computer, select 1, and enjoy !
## How to use Wireless Debug

After starting the software, you have two choices
```bash
USB Debug (1)
Wireless Debug (2)
```

If you choose Wireless debug select 2, follow the same tutorial, but enable the "Use wireless debugging" option. If you have already paired your device, press "y", and write the IP adress, in this case "192.168.1.242", then the port, in this case "38157", and enjoy !

![alt text](https://developer.android.com/static/studio/images/run/adb_wifi-wireless_debugging.png)

If you have not paired your device before, press "n", select "Pair device with pairing code" on your phone. Then write the new IP adress on the software, the new port, then the six digit code. After it's successfully paired, leave the "Pair device" menu on your phone, write the new IP adress, in this case "192.168.1.242", then the port, in this case "38157", then enjoy ! 

## License

See the license [here](https://github.com/Pangaulin/ADSoftbricker/blob/main/LICENSE.txt)