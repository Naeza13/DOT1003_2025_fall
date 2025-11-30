def left():
    print("There is a wild cat licking his paws. Better to be avoid.")

def right():
    print("You find a treasure chest!")
    print("Open it and find some gold coins!")

def idle():
    print("You can't start an adventure by waiting.")
    print("You're boring...")

def start_adventure():
    cevap = input("make a choice")

    if cevap == "left":
        left()
    elif cevap == "right":
        right()
    elif cevap == "idle":
        idle()
    else:
        print("invalid input")
        start_adventure()

start_adventure()