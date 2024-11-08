# initializing the variable output,used to gather everything which are printed to display in text file
output=''

#this function to get user name and to display a intro
def intro():
    prompt=('''\t\t\t"Welcome to DON game"\n\n\\\\\\\tYou should choose a lower value than your life score to fight\t\\\\\\
    \t\t\t\tGood Luck:)\n--------------------------------------------------------------------------------''')
    print(prompt)
    output=prompt
    name = input('Enter a user name for DON [should start with an alphabet]:-- ')#getting user name

    while name == '' or not name[0].isalpha():#check whther the user name starts with alphabet 
        print("Start the name with an alphabet, try again\n")
        name = input('Enter a user name [should start with an alphabet]:- ')
    
    name = name.capitalize()
    return name,output #return values to mainx file







