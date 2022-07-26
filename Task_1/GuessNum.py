import random
from warnings import catch_warnings
print("----select range you want to play in----\n")
print("A> 1 - 10\n")
print("B> 1 to 100\n")
print("-->")
correctInput = True
while(correctInput):
    
    print("A> 1 - 10\n")
    print("B> 1 to 100\n")
    print("----select range you want to play in----\n")
    print("\n-->\n")

    n = input()
    if(n == "A" or n=="a" or n=="B" or n =="b"):
        correctInput = False
        if(n == "A" or "a"):
            secNum = random.randint(1, 10)
        elif(n == "B" or "b"):
            secNum = random.randint(1, 100)
            chances = True
        guessed = False
        if(n == "A" or "a"):
            print("\nGREAT!! SNOW GUESS A NUMBER BETWEEN 1️⃣-------🔟")
            i = 5
            score = 5
            while(score != 0):
                if(score >= 0):
                    print(" chances left ⌚" + str(score) + " \n")
                    print(" GUESS THE NUMBER 🤔🤔\n")
                    print("--------------------------------------------------------\n")
                    print("-->")
                    n = int(input())

                    if(n > secNum):
                        range1 = secNum - i
                        if(range1 < 0):
                            range1 = 0
                        range2 = secNum+i
                        if(range2>10):
                            range2 = 10
                        print("\nNumber greater than Secret number 📈📈📈")
                        print("number is  between " + str(range1) +
                            " and " + str(range2) + "\n")
                        print("--------------------------------------------------------\n")
                        score -= 1
                    elif(n < secNum):
                        range1 = secNum - i
                        range2 = secNum+i
                        if(range2 > 10):
                            range2 = 10
                        if(range1 < 0):
                            range1 = 0

                        print("\nNumber smaller than Secret number 📉📉📉")
                        print("number is  between " + str(range1) +
                            " and " + str(range2)+"\n")
                        print("--------------------------------------------------------\n")
                        score -= 1
                    if(n == secNum):
                        print("🎉🎉🎉🎉secret number " + str(secNum) +
                            " guessed successfully🎉🎉🎉🎉")
                        chances = False
                        print("score :" + str(score))
                        guessed = True
                        print("--------------------------------------------------------\n")
                        break
                    i -= 1

            print("\n\n❌❌❌❌❌❌GAME OVER❌❌❌❌❌❌\n\n")
            if(guessed == False):
                print("SORRY YOU COULDN'T GUESS THE NUMBER : " + str(secNum))
        elif(n == "B" or "b"):
            print("\nGREAT!! SNOW GUESS A NUMBER BETWEEN 1------100")
            i = 50
            score = 20
            while(score != 0):
                if(score >= 0):
                    print(" chances left ⌚" + str(score) + " \n")
                    print(" GUESS THE NUMBER 🤔🤔\n")
                    print("--------------------------------------------------------\n")
                    print("-->")
                    n = int(input())

                    if(n > secNum):
                        range1 = secNum - i
                        if(range1 < 0):
                            range1 = 0
                        range2 = secNum+i
                        print("\nNumber greater than Secret number 📈📈📈")
                        print("number is  between " + str(range1) +
                            " and " + str(range2) + "\n")
                        print("--------------------------------------------------------\n")
                        score -= 1
                    elif(n < secNum):
                        range1 = secNum - i
                        range2 = secNum+i
                        if(range2 > 100):
                            range2 = 100
                        if(range1 < 0):
                            range1 = 0

                        print("\nNumber smaller than Secret number 📉📉📉")
                        print("number is  between " + str(range1) +
                            " and " + str(range2)+"\n")
                        print("--------------------------------------------------------\n")
                        score -= 1
                    if(n == secNum):
                        print("🎉🎉🎉🎉secret number " + str(secNum) +
                            " guessed successfully🎉🎉🎉🎉")
                        chances = False
                        print("score :" + str(score))
                        guessed = True
                        print("--------------------------------------------------------\n")
                        break
                    i -= 1

            print("\n\n❌❌❌❌❌❌GAME OVER❌❌❌❌❌❌\n\n")
            if(guessed == False):
                print("SORRY YOU COULDN'T GUESS THE NUMBER : " + str(secNum))

    else:
        print("PLEASE ENTER EITHER A OR B")
        correctInput = True

