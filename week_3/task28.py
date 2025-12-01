sec=int(input("enter a number"))
while sec:
    print(sec)
    if sec==1:
        print ("kaboom")
        sec=False
    else:
        sec=(sec-1)
        