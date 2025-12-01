word1=input("first word")
word2=input("second word")
length1=len(word1)
length2=len(word2)
if length1<length2:
    print(word2)
elif length2<length1:
    print(word1)
else :
    print("Their length are same")

