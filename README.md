# PiLock

This project is designed to be a smart lock that can be opened via NFC.
- The status of this project is unknown and unfinished

**Installation:**

1. Ensure to enable SPI interface via
   1. Entering `sudo raspi-config`
   1. Select option 5 Interfacing Options
   1. Then enable P4 SPI
1.	Install any requirements via `pip3 install -r requirements.txt`

**Wiring Diagram:**
![]( https://i.imgur.com/529UkLd.png)

**Raspberry Pi Pinout:**
![](https://i.imgur.com/CmKckYw.png)

**Installing a Service:**

Create the dervice file by typing `sudo nano /etc/systemd/system/lock.service`
Enter the following: (be sure to change the directories if needed)
```sh
[Unit]
Description=Lock Service
After=multi-user.target

[Service]
User=pi
Group=pi
Type=simple
WorkingDirectory=/home/pi/Lock/
ExecStart=/usr/bin/python3 /home/pi/Lock/nfc.py

[Install]
WantedBy=multi-user.target
```
**Other Info:**

nfc.py is the main program while importing motor controls from lock.py

Logs will enter in to the same directory as the repro as DoorLock.log

For redundancy reasons once the device has lost power and is in a locked state, on next run it will unlock.

If you would like a simple command to alternate the lock, then simply type this in to a terminal and when "lock" is written it will alternate the lock
echo "alias lock='cd /home/pi/Lock && python3 /home/pi/Lock/alternate_lock.py && cd -' " >> ~/.bashrc
