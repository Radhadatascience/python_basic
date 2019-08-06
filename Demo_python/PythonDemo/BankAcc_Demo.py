'''
Created on Jun 24, 2019

@author: Lenovo
'''
from _ast import Num
print('Helloworld')


    
i = input("Enter your Account num: ")
print("Account num is "+i)
if (i == i): 
    print ("Valid pls proceed") 

     

#elif (i != 15): 
    #print ("Inv") 
#elif (i <=0): 
    #print ("N") 
#else: 
    #print ("i is not present") 

phnum = input("Enter Phone num : ") 
print(phnum) 

Amt_despoite = input("Enter Ammt desp: ") 
print(Amt_despoite) 
print("Account desp is "+Amt_despoite)

Amt_WD = input("Enter Ammt WD: ") 
if(Amt_despoite<=Amt_WD):
    print("Withdraw amt"+Amt_WD)
elif(Amt_despoite>=Amt_WD):
 print("You have  withdraw"+Amt_WD)
 bal=int(Amt_despoite)- int(Amt_WD)
 print ("bal is",bal)


 
 
 
 
 
 
 
 
 
 
 
 

#bal=Amt_WD-Amt_despoite
#print("The balance anount is"+bal)


# Printing type of input value 
#print ("type of number", type(num)) 
#print ("type of name", type(name1)) 


