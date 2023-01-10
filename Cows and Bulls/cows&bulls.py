from random import choice
word = ['APPLE', 'BANANA', 'KIWI', "TOMATO", 'CRUEL', 'TEACHER', 'TOMB', 'TOWER']

correctWord = choice(word).upper()
correctWordList = list(correctWord)

length = len(correctWord)

print("The word of {length} characters".format(length=length))

lives = 10

while(lives>=0):
    cows=bulls=0
    userWord = input("Enter your word: ")
    userWord=userWord.upper()

    userWordList = list(userWord)
    lives-=1
    
    if len(userWord)!= length:
        print("Wrong length of words")
        print('Remaining lives', lives)
        continue
    
    if userWord==correctWord:
        print("Correct Guess")
        break
    
    for i in range(length):
        if correctWordList[i]==userWordList[i]:
            bulls+=1
        
    for i in range(length):
        if correctWordList[i] in userWordList:
            cows+=1
            userWordList.remove(correctWordList[i])

    cows=cows-bulls
    print("cows = {}, bulls = {}".format(cows, bulls))
    print('Remaining lives', lives)

else:
    print("You loose")