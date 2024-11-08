#import packages and modules created
import functionx.timex
import functionx.namex

#varibale output is used to gather everything which are printed to display in text file

#entire function to print when player loose
def lost(user, attempt, score,output):
    print()
    print("***Game status***")
    output+="\n\n***Game status***"
    print('Player name:', user)
    output+='\nPlayer name:'+ user
    print("Total attempts:", attempt)
    output+="\nTotal attempts:"+str(attempt)
    print("Final score:", score)
    output+="\nFinal score:"+str(score)
    print(user, "was defeated!!!")
    output+= '\n'+user+ " was defeated!!!"
    return functionx.timex.time(output) # Exit the function and calls time function in timex module
