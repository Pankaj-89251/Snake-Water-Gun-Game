#Snake, Water, Gun Game.!!!!!!



import random

def gameWin(comp, player):
    if comp == player:
        return None
    if comp == 's':
        if player == 'w':
            return  False
        elif player== 'g':
             return True

    if comp == 'w':
        if player == 'g':
            return  False
        elif player== 's':
             return True   

    
    if comp == 'g':
        if player == 's':
            return  False
        elif player== 'w':
             return True                 
       



comp = print('Computer : Snake(s), Water(w) or Gun(g) ???')
randomNo= random.randint(1,3)
if randomNo == 1:
    comp = "s"
elif randomNo == 2:
    comp = "w"
elif randomNo == 3:
    comp = "g"
player = input('Player : Snake(s), Water(w) or Gun(g) ???')
a = gameWin(comp, player)

print(f"Computer choice : {comp}")
print(f"Your choice : {player}")

if a==None:
    print("Game Tie!")
elif a:
    print("You Win!") 
else:
    print("You Lose!")


