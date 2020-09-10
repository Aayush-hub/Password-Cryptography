import string                                      #built-in module
import random                                      #built-in module
if __name__ == "__main__":
    a1 = string.printable                          #taking all characters,digits and punctuations as string
    i = input("Enter length of password: \n")      #taking length of password required as input
    while True:
	        
	        if i.isdigit():                    #checking whether input is interger.
		        break
	        else:
		        print("Please enter a number")
		        continue
    a = []                                         #taking empty list
    a.extend(list(a1))                             #appending all elements in empty list.
    random.shuffle(a)                              #shuffling all elements and choosing random elements
    print("Your Password is: " ,end="")
    c = "".join(a[0:int(i)])
    print(c)                                       #printing password generated.
       
