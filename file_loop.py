from pathlib import Path


## this script is an examply of how to create a file, and iterate through it to find the matching card

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



with open("cards.txt", "r") as a_file:
  for line in a_file:
    card = line.strip()
    if card == "3": # insert variable for card instead of "3"
        # IF card matches what is read then do this
        print(card)
        print(" - the card was matched")
    else:
        # if not erm...
        print(card)

    