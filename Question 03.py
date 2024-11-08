amount=int(input("Enter Amount (less than Rs.1000) Rs."))
note500=0
note100=0
note50=0
note20=0
note10=0
note5=0
note2=0
note1=0

if(amount<1000):
  
 note500=amount//500
 amount=amount-note500*500
   
 note100=amount//100
 amount=amount-note100*100
  
 note50=amount//50
 amount=amount-note50*50
  
 note20=amount//20
 amount=amount-note20*20
    
 note10=amount//10
 amount=amount-note10*10
   
 note5=amount//5
 amount=amount-note5*5
    
 note2=amount//2
 amount=amount-note2*2
 
 note1=amount//1
 amount=amount-note1*1


 print(note500,"Note(s)of 500.00")
 print(note100,"Note(S)of 100.00")
 print(note50,"Note(S)of 50.00")
 print(note20,"Note(S)of 20.00")
 print(note10,"Note(S)of 10.00")
 print(note5,"Note(S)of 5.00")
 print(note2,"Note(S)of 2.00")
 print(note1,"Note(S)of 1.00")
else:print('Invalid input,(Enter amount less than Rs.1000)')

      
