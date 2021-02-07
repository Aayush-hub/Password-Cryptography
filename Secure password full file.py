import string                                                     #built in module
import random                                                     #built in module
if __name__ == "__main__":
    print("----------What you Want to do?------------")
    print("Press 0 to generate and encrpt password")
    print("Press 1 to decrpt password")
    e = int(input())                                              #taking input what to-do
    a1 = string.printable                                         #taking all characters,digits and punctuations as string
    if e == 0:

        while True:
	            i = input("Enter length of password: \n")     #checking whether input is integer.
	            if i.isdigit():
		            break
	            else:
		            print("Please enter a number")
		            continue
        a = []                                                   #taking empty list
        a.extend(list(a1))                                       #appending all elements in empty list.
        random.shuffle(a)                                        #shuffling all elements and choosing random elements
        print("Your Password is: " ,end="")
        c = "".join(a[0:int(i)])
        print(c)                                                 #printing password generated.
        while True:
	        j = input("Set your Access Key: \n")             #setting access key
	        if j.isdigit():                                  #checking whether input is integer.
		        break
	        else:
		        print("Please enter a number")
		        continue
			
	#SECURE can be changed according to need.
	
        SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('a','@'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
        def securepassword(password):
            for a,b in SECURE:
                password = password.replace(a, b)                #replacing original elements to encrypted ones.
            return password
        password = c
        password = securepassword(password)
        print(f"Your Encrpted Password is: {password}")          #printing encrypted password
    elif e==1:
        f = input("Enter password to be decrpted: \n")           #enter password to be decrypted
        while True:
	        j = input("Enter your Access Key: \n")           #entering access key
	        if j.isdigit():                                  #checking whether input is integer.
		        break
	        else:
		        print("Please enter a number")
		        continue
        SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('a','@'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
        def securepassword(password):
            for a,b in SECURE:
                password = password.replace(b, a)
            return password
        password = f
        password = securepassword(password)
        print(f"Your Password is: {password}")                  #printing original password 
    else:                                                       #checking condition if user input is other than 0 or 1.
        print("Enter 0 or 1")                                   
