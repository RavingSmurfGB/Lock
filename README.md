# PiLock

This project is designed to be a smart lock that can be opened via NFC.

**Installation:**
1.	Ensure to enable SPI interface via:
a.	Entering `sudo raspi-config`
b.	Select option 5 Interfacing Options
c.	Then enable P4 SPI
2.	Install any requirements via `pip3 install requirements.txt`

**Wiring Diagram:**
![]( https://i.imgur.com/529UkLd.png)

**Raspberry Pi Pinout:**
![](https://i.imgur.com/CmKckYw.png)

**Installing a Service:**

Create the dervice file by typing `sudo nano /etc/systemd/system/lock.service`
Enter the following: (be sure to change the directories if needed)
```
[Unit]
Description=Lock Service
After=multi-user.target

[Service]
Type=simple
WorkingDirectory=/home/pi/Lock/
ExecStart=/usr/bin/python3 /home/pi/Lock/nfc.py

[Install]
WantedBy=multi-user.target
```
**Other Info:**

nfy.py is the main program while importing motor controls from lock.py
