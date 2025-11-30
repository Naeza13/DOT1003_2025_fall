print("Dumb calculator v0.1 If you want to exit, enter 0")
plus=0
total=0
odd=0
even=0
mean=0

flag=1
while flag:
    num=int(input("Please enter a number"))
    if num!=0:
        mean=mean+num
        plus=plus+num
        total=total+1
        if num%2==0:
            even=even+1
        else:
            odd=odd+1
    elif num==0:
        mean=mean/total
        print(f"Total number:{total}")
        print(f"Sum:{plus}")
        print(f"Mean:{mean}")
        print(f"Odd:{odd} even:{even}")
        
        flag=0