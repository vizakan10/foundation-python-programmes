number= int(input("Enter an integer number between 1 and 100: "))
sum_n=0
addition = ""
print("Input number =",number)
if (1 <= number <= 100):
    n = 1
    while n <= number*2:
        if (n % 2 != 0):
            sum_n += n
            if(addition):
                addition += "+"+str(n)
            else:
                addition += str(n)
        n+= 1
    print("Square number",number,"=",addition, "=", sum_n) 
else:
    print("Invalid input. Please enter an integer number between 1 and 100.")
  
