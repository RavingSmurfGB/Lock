from pirc522 import RFID
from pathlib import Path
import time, logging
import datetime
import subprocess

rdr = RFID()

##////////////////logging Setup/////////////////
# create logger with the name 'SleepyServer'
logger = logging.getLogger('DoorLock')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('DoorLock.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

##this part is to easily seperate lines before the new logs are created - not really needed
startingstring = " \n" + " \n" 
logger.addHandler(fh)
logger.addHandler(ch)
logger.info(startingstring + startingstring + startingstring )

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

#print("NFC Loading...")
logger.info("Adding Cards Loading...")
##////////////////

##////////////////Check if file exists/////////////////
try:
    my_file = Path("cards.txt")
    if my_file.is_file():
        #print("file exists")
        logger.info("cards file does not exists and will be created")
    else:
        #print("cards file does not exists and will be created")
        logger.info("cards file does not exists and will be created")
        f = open("cards.txt", "x")
        f.close()
except:
    #print("cards file does not exists and will be created")
    logger.info("cards file does not exists and will be created")


try:
    print("hi")
    subprocess.run(["sudo", "systemctl", "stop", "lock"])
except:
    GPIO.cleanup()

try:
    while True:
        logger.info("waiting for card")
        rdr.wait_for_tag()
        logger.info("I read a card")
        (error, tag_type) = rdr.request()
        if not error:
            print("Tag detected")
            (error, uid) = rdr.anticoll()
            if not error:
                nfcid = ':'.join(str(x) for x in uid)
                print(f"{datetime.datetime.now()} - UID: " + nfcid)
                logger.info(f"{datetime.datetime.now()} - UID: " + nfcid)
                f = open("cards.txt", "a")
                print(nfcid)
                f.write(nfcid)
                f.close()
            
        else:
            print(f"I have errored: {error}")
            logger.error(f"I have errored: {error}")
        time.sleep(2)
except:
    GPIO.cleanup()

##////////////////


