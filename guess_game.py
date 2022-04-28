'''if the player's guess is higher then the actual number , the program will display "try lower number"
similary if the user's guess is too low th eprogram will diaplay "try larger number" and when th euser guesses the correct number ,
 the program will display the number of gusses taken by the player till gusing it correct so who ever take the least guesses will win the game'''



import random
randomNumber = random.randint(1,100)
# print(randomNumber)
userguess= None
guesses = 0 
while(randomNumber!= userguess):
    userguess=int(input("enter your guess:"))
    if(userguess == randomNumber):
        print("you guessed it right")
    else:
        if(userguess>randomNumber):
            print("you guessed it wrong,try smaller number")
        else:
            print("you guessed it wrong,try larger number")
    guesses +=1
print(f"you have guesed in {guesses} guesses")            

        
