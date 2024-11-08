#import packages and modules created
import functionx.namex


#this function takes the arguments from mainx file and open text file in write mode, in the name of the value given to result argument
def file(result,output1,output2):
    with open(result, "w") as fo:
        fo.write(output1+output2)#write the things in output1 and output2 in the text file
