intro=input("enter your introduction")
charactercount=0
wordcount=1
for i in intro:
    charactercount=charactercount+1
    print(charactercount)
    if(i==''):
        wordcount=wordcount+1
print("number of word in the string")
print(wordcount)
print("number of characterin the string")
print(charactercount)
