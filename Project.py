import random
'''
 1 for snake
 -1 for water
 0 for gun
'''
computer=random.choice([-1,0,1])
youstr=(input("Enter your choice : "))
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]
# by now have 2 number (variables),you and computer 
print(f"You chose {[reversedict]}\ncomputer choose {reversedict[computer]}")
if(computer==you):
    print("its game draw")
else:
    if(computer==-1 and you==1):
        print("You Win !!")
    elif(computer==-1 and you==0):
        print("You Lose !!")
    elif(computer==1 and you==-1):
        print("You Lose !!")
    elif(computer==0 and you==-1):
        print("You win !!")
    elif(computer==0 and you==1):
        print("You Lose !!")
    else:
       print("went wrong")