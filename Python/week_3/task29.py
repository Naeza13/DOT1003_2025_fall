hak=3
password=314159
while hak:
    password2=int(input("password:"))
    if password==password2:
        print("Welcome")
        hak=0
    elif hak==1:
        print ("Incorrect Password. Exterminate...")
        hak=0
    else:
        hak=hak-1

