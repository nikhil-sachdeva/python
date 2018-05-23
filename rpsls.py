
import random



def name_to_number(name):

 if(name=="rock"):
    return 0
 elif(name=="Spock"):
    return 1
 elif(name=="paper"):
    return 2
 elif(name=="lizard"):
    return 3
 elif(name=="scissors"):
    return 4
 else:
    return -1

def number_to_name(number):

     if(number==0):
        return("rock")
     if(number==1):
        return("Spock")
     if(number==2):
        return("paper")
     if(number==3):
        return("lizard")
     if(number==4):
        return("scissors")



def rpsls(player_choice):

    print("---------------------------------")
    print("Player choses:"+player_choice)
    num1=name_to_number(player_choice)
    num2=random.randrange(0,5)
    comp_choice=number_to_name(num2)
    print("Computer chooses:"+comp_choice)
    win=(num1-num2)%5
    if(win==1 or win==2):
        print("Player wins")
    if(win==3 or win==4):
        print("Computer wins")
    if(win==0):
        print("Tie")


print("The rules are very simple")
print("Scissors cuts paper, paper covers rock. Rock crushes lizard, lizard poisons Spock. ")
print("Spock smashes scissors, scissors decapitates lizard. Lizard eats paper, paper disproves Spock.")
print("Spock vaporizes rock, and as always has been, rock crushes scissors.")



rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
