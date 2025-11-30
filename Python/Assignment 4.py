
game_list=[]
newlist=[]

def anarya():
    for i in range(len(game_list),0,-1):
        newlist.append(game_list[i-1])


flag=1
while flag==1:
    word=input("Please Enter a game:")
    if word=="exit":
        anarya()
        print(newlist)
        flag=0
    else :
        game_list.append(word)
        