#import packages and modules created
import random
import functionx.lostx
import functionx.winx
import functionx.power


#variable output is used to gather everything which are printed to display in text file
output=''
def game(user):
    global output
    name=''
    power=0
    attempt=0
    score=0
    num=0
    score = random.randrange(1, 50)#getting a random number between 1 to 49 as life score
    for i in range(1, 21):#this loop is to get the randomly generated 5 numbers to fight with user
        elements = []
        attempt = i
        
        if 1 <= attempt <= 5:
            for i in range(0, 5):
                choice = random.randrange(15, 101)
                elements.append(choice)
        elif 6 <= attempt <= 10:
            for i in range(0, 5):
                choice = random.randrange(250, 2001)
                elements.append(choice)
        elif 11 <= attempt <= 15:
            for i in range(0, 5):
                choice = random.randrange(3000, 10001)
                elements.append(choice)
        else:
            for i in range(0, 5):
                choice = random.randrange(20000, 100001)
                elements.append(choice)
        print("Player's name-",user)
        output+="\nPlayer'sname-"+str(user)+'\n'
        print("Attempt:", attempt)
        output+="Attempt:"+ str(attempt)+'\n'
        print(user + "'s", "life score is:", score)
        output+=str(user) + "'s  life score is:"+str(score)+'\n'
       
        for val in elements:   #this loop is to print the randomly generated numbers without the brackets and commas
            val = str(val) + "  "
            print(val, end="")
            output+=val+" "

        try:  #error handling to make sure user inputs a integer to fight
            num = int(input("\nSelect a number to fight:"))
            power=random.randrange(1,32)
            score=functionx.power.boost(power,score)
            output+="\nSelect a number to fight:"+str(num)
           
        except ValueError:
            print("""\nYou didn't choose the numbers to fight\nfollow the instructions properly\n      You are defeated""")
            output+="""\nYou didn't choose the numbers to fight\nfollow the instructions properly\n      You are defeated"""
            
            result_timestamp = functionx.lostx.lost(user, attempt, score,output)
            return result_timestamp# Exit the function on invalid input and calls function lost in module lostx

        if num not in elements:# to check if the entered number is in the generated numbers
            print("No such enemy")
            output+="\nNo such enemy"
            
            result=functionx.lostx.lost(user, attempt, score,output)
            return result # Exit the function on invalid input and calls function lost in module lostx
        else:
            if num <= score:#check if the entered number to fight is lower than the lifescore
                print(user, "killed", num)
                output+='\n'+str(user)+"  killed "+str(num)
                score += int(num)
                if attempt == 20:#this is to check the attempt and make sure it stops in 20th attempt and print the win statement
                    result_timestamp = functionx.winx.win(user, attempt, score,output)
                    return result_timestamp
                print()
                output+='\n'
            else:
                print(num, "killed", user)#check if the entered number to fight is higher than the lifescore
                output+='\n'+str(num)+" killed "+str(user)
                
                result_timestamp = functionx.lostx.lost(user, attempt, score,output)
                return result_timestamp  # Exit the function if defeated and calls function lost in module lostx




    



