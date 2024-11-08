import random

number=[100,120,40,80]
random.shuffle(number)
integer=number[2]

def boost(power,score):
    if power%2==0:
        ally=score+integer
        print("\nYou got an Option to Boost your power!!!!")
        ask=input("Do you want to use that power(y/n)")
        if ask=="y":
            print("Your Life score is added with"+str(integer))
            return ally
        else:
            return score
    else:
        return score


