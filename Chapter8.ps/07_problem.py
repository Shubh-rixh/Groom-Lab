import random 
computer = random.choice([1, 0, -1])
youStr = input("Enter your Choice: ")
youDict = {"d": 1, "p": -1, "s": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissor"}

you = youDict[youStr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw")

else:
    if(computer == 1 and you == -1):
        print("You Win!")

    elif(computer == 1 and you == 0):
        print("You Lose!")

    elif(computer == -1 and you == 1):
        print("You Lose!")
    
    elif(computer == -1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Lose!")

    else:
        print("Something Went Wrong")