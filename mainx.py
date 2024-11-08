#import packages
import functionx.namex
import functionx.textx
import functionx.optionx
import functionx.listry

#Declaring and intit. variables
user=output1=output2=result=''

# user and output1 will get the alues returned by the intro function in module callled namex in the package called functionx
user,output1=functionx.namex.intro()
functionx.listry.main(user)

#result and output2 will get the alues returned by the game function in module callled optionx in the package called functionx
result,output2=functionx.optionx.game(user)

#file function in module textx will get result,ouput1,output2 as parameters
functionx.textx.file(result,output1,output2)
