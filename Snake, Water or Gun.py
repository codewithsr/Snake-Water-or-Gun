import random



def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        
        else: 
            return True


    elif comp == 'w':
        if you == 'g':
            return False
        
        else: 
            return True


    else:
        if you == 's':
            return False
        
        else: 
            return True

print("Computer's turn: Snake(s) Water(w) or Gun(g) \n\n")
randomNumber = random.randint(1,3) #--> (1,3) is a range meaning 1,2,3. It is not like range func. jisme last vala number include nhi hota. 
if randomNumber == 1:
    comp = 's'

elif randomNumber == 2:
    comp = 'w'

else:
    comp = 'g'



you = input("Your turn: Snake(s) Water(w) or Gun(g) \n")   #(s), (g), (w) signifies keys to press for snake, water or gun


a = gameWin(comp, you)
print(f"Computer chose {comp}")
if a == None:
    print("It's a draw!")

elif a == False:
    print("You lose!")

else:
    print("***********You Won!****************")