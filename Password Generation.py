import string
import random
if __name__ == "__main__":
    a1 = string.printable
    i = input("Enter length of password: \n")
    while True:
	        
	        if i.isdigit():
		        break
	        else:
		        print("Please enter a number")
		        continue
    a = []
    a.extend(list(a1))    
    random.shuffle(a)
    print("Your Password is: " ,end="")
    c = "".join(a[0:int(i)])
    print(c)
       
