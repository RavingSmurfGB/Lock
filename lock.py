import RPi.GPIO as GPIO
import pathlib as Path
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

logger.info('START')
print("Start")
##////////////////

### Declaring pins for the motor control 
out1 = 13
out2 = 11
out3 = 15
out4 = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

### Motor Variables
i=0
positive=0
negative=0
y=0
timings = 0.001



##////////////////Check if file exists/////////////////
try:
    my_file = Path("status.txt")
    if my_file.is_file():
        print("file exists")
    else:
        print("file does not exists")
        f = open("status.txt", "x")
        f.close()
except:
    print("File error :( ")
##////////////////



print("Program Loading...")
logger.info("Program Loading...")

def Lock():
    global positive
    global negative
    global i 
    global y
    logger.info("I locked the door")
    print("I locked the door")
    f = open("status.txt", "w")
    f.write("locked")
    f.close()
    x = 200
    for y in range(x,0,-1):
        if negative==1:
            if i==7:
                i=0
            else:
                i=i+1
            y=y+2
            negative=0
        positive=1
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==2:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==3:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==4:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timings)
        elif i==6:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timings)
        elif i==7:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timings)
        if i==7:
            i=0
            continue
        i=i+1

def Unlock():
    global positive
    global negative
    global i 
    global y
    logger.info("I un-locked the door")
    print("I un-locked the door")
    f = open("status.txt", "w")
    f.write("unlocked")
    f.close()
    x = -200
    x=x*-1
    for y in range(x,0,-1):
        if positive==1:
            if i==0:
                i=7
            else:
                i=i-1
            y=y+3
            positive=0
        negative=1
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==2:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==3:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==4:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timings)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timings)
        elif i==6:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timings)
        elif i==7:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timings)
        if i==0:
            i=7
            continue
        i=i-1
    return(x)


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
    print("something went wrong help me")
##////////////////

try:
    while True:
        Lock()
        time.sleep(1)
        Unlock()
        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()