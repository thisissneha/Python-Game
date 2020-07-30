import random
print("WELCOME TO THE SNAKE WATER GUN GAME...!!!")
name=input("Enter your Name : ")
a=['Snake','Water','Gun']
n=0
comp_won=0
user_won=0
game_tie=0
while(n!=5):
    comp = random.choice(a)
    user = input("What you want to Choose from Snake, Water, Gun : ")
    if(user.lower()=='snake'):
        if(comp=='Snake'):
            print("Game tie...Try again")
            game_tie=game_tie+1
        elif(comp=='Water'):
            print(name,"you won this game")
            user_won=user_won+1
        else:
            print(name,"you lose this game..Try again")
            comp_won=comp_won+1
    elif(user.lower()=='water'):
        if(comp=='Water'):
            print("Game tie...Try again")
            game_tie = game_tie + 1
        elif(comp=='Gun'):
            print(name,"you won this game")
            user_won=user_won+1
        else:
            print(name,"you lose this game..Try again")
            comp_won=comp_won+1
    elif(user.lower()=='gun'):
        if(comp=='Gun'):
            print("Game tie...Try again")
            game_tie = game_tie + 1
        elif(comp=='Snake'):
            print(name,"you won this game")
            user_won=user_won+1
        else:
            print(name,"you lose this game..Try again")
            comp_won=comp_won+1
    else:
        print("Invalid Input..Please Try Again")
    n=n+1
print("User won this games ",user_won," times")
print("Computer won this game ",comp_won," times")
print("Game tie ",game_tie," times")
if(user_won>comp_won):
    print("Final Winner : ",name)
elif(user_won<comp_won):
    print("Final Winner : computer")
else:
    print("Game Tie")