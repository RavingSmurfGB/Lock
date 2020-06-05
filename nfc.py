from pathlib import Path
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from lock import alternate_lock
import time, logging


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

print("NFC Loading...")
logger.info("NFC Loading...")
##////////////////

## this script is an example of how to create a file, and iterate through it to find the matching card

reader = SimpleMFRC522()

##Check if file exsists
try:
    my_file = Path("cards.txt")
    if my_file.is_file():
        print("file exists")
    else:
        print("cards file does not exists and will be created")
        logger.info("cards file does not exists and will be created")
        f = open("cards.txt", "x")
        f.close()
except:
    print("cards file does not exists and will be created")
    logger.info("cards file does not exists and will be created")

while True:
    logger.info("waiting for card read")
    nfcid, text = reader.read()
    if nfcid is None:
        continue
    with open("cards.txt", "r") as a_file:
        for line in a_file.readlines():
            card = line.strip()
            if card == str(nfcid): # insert variable for card instead of "3"
                # IF card matches what is read then do this
                print(str(nfcid) + " - the card was matched")
                logger.info(str(nfcid) + " - the card was matched")
                alternate_lock()
                
            else:
                # if not erm...
                print(str(nfcid) + " card does not match")
                logger.info(str(nfcid) + " card does not match")
    time.sleep(2)
                

