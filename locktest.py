import RPi.GPIO as GPIO
import time

#Setting optional variables
rotations = 50
timings = 0.001

### Declaring pins for the motor control 
GPIO.setmode(GPIO.BOARD)

pins = [13,11,15,12]
for pin in pins: 
    GPIO.setup(pin,GPIO.OUT)

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

def Forward(rotations):
    #How many times to do a rotation
    for i in range(rotations):
        #start from the start of the sequence and move up 
        for step in range(0,8,+1):
            #loops through the pins
            for pin in range(4):
                #Sets the pins as per the sequence 
                GPIO.output(pins[pin], halfstep_seq[step][pin])
            time.sleep(timings) 

def Backward(rotations):
    #How many times to do a rotation
    for i in range(rotations):
        #start from the end of the sequence and move down 
        for step in range(8,0,-1):
            step = step-1
            #loops through the pins
            for pin in range(4):
                #Sets the pins as per the sequence 
                GPIO.output(pins[pin], halfstep_seq[step][pin])
            time.sleep(timings) 

print("Program Loading...")

try:
    while True:
        Forward(rotations)
        time.sleep(1)
        Backward(rotations)
        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()