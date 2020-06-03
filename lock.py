import RPi.GPIO as GPIO
from pathlib import Path
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

print("Program Loading...")
logger.info("Program Loading...")
##////////////////


##////////////////Declaring pins & motor control stuff/////////////////
GPIO.setmode(GPIO.BOARD)

pins = [13,11,15,12]
for pin in pins: 
    GPIO.setup(pin,GPIO.OUT)

### Motor Variables
rotations = 50
max_rotations = 90 # this is the max it should ever rotate 
timings = 0.001

#Setting the sequence for rotation
halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

##///////////////


##////////////////Check if file exists/////////////////
try:
    my_file = Path("status.txt")
    if my_file.is_file():
        print("file exists")
    else:
        print("file does not exists")
        f = open("status.txt", "x")
        f.close()
        f = open("status.txt", "w")
        f.write("unlocked")
        f.close()
except:
    print("Unable to find or create file status.txt ")
    logger.info("Unable to find or create file status.txt ")
##////////////////






##////////////////Lock code/////////////////

def Lock():
    logger.info("I locked the door")
    print("I locked the door")
    f = open("status.txt", "w")
    f.write("locked")
    f.close()
    #How many times to do a rotation
    if rotations > 0 and rotations <= max_rotations:
        for i in range(rotations):
            #start from the start of the sequence and move up 
            for step in range(0,8,+1):
                #loops through the pins
                for pin in range(4):
                    #Sets the pins as per the sequence 
                    GPIO.output(pins[pin], halfstep_seq[step][pin])
                time.sleep(timings)

def Unlock():
    logger.info("I un-locked the door")
    print("I un-locked the door")
    f = open("status.txt", "w")
    f.write("unlocked")
    f.close()
    #How many times to do a rotation
    if rotations > 0 and rotations <= max_rotations:
        for i in range(rotations):
            #start from the end of the sequence and move down 
            for step in range(8,0,-1):
                step = step-1
                #loops through the pins
                for pin in range(4):
                    #Sets the pins as per the sequence 
                    GPIO.output(pins[pin], halfstep_seq[step][pin])
                time.sleep(timings) 


##////////////////If file status was locked on last startup/////////////////
try:
    f = open("status.txt", "rt")
    contents = f.read()
    f.close()
    if contents == "locked":
        print("Locked on last shutdown, unlocking door")
        logger.info("Locked on last shutdown, unlocking door")
        Unlock()
        f = open("status.txt", "w")
        f.write("unlocked")
        f.close()
    else:
        print("lock was already unlocked...")

except:
    print("Unable to detect status.txt on boot")
    logger.info("Unable to detect status.txt on boot")
##////////////////

##////////////////Alternate lock/////////////////
def alternate_lock():
    f = open("status.txt", "rt")
    contents = f.read()
    f.close()
    try:
        if contents == "locked":
            Unlock()
        elif contents == "unlocked":
            Lock()
    except:
        print("Was not able to read file status.txt")
        logger.info("Was not able to read file status.txt")



##////////////////Main/////////////////
try:
    while True:
        alternate_lock()
        time.sleep(1)
        alternate_lock()
        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()