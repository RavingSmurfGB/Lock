from pathlib import Path
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


## this script is an example of how to create a file, and iterate through it to find the matching card

reader = SimpleMFRC522()

##Check if file exsists
try:
    my_file = Path("cards.txt")
    if my_file.is_file():
        print("file exists")
    else:
        print("file does not exists and will be created")
        f = open("cards.txt", "x")
        f.close()
except:
    print("Unable to find or create file cards.txt ")




try:
    with open("cards.txt", "r") as a_file:
        id, text = reader.read()
        for line in a_file:
            card = line.strip()
            if card == id: # insert variable for card instead of "3"
                # IF card matches what is read then do this
                print(id)
                print(" - the card was matched")
            else:
                # if not erm...
                print("card was not matched")
finally:
        GPIO.cleanup()