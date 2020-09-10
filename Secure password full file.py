import string
import random
if __name__ == "__main__":
    print("----------What you Want to do?------------")
    print("Press 0 to generate and encrpt password")
    print("Press 1 to decrpt password")
    e = int(input())
    a1 = string.printable
    if e == 0:

        while True:
	            i = input("Enter length of password: \n")
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
        while True:
	        j = input("Set your Access Key: \n")
	        if j.isdigit():
		        break
	        else:
		        print("Please enter a number")
		        continue
        SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('4','f'),('f','4'),('a','@'),('@','a'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
        def securepassword(password):
            for a,b in SECURE:
                password = password.replace(a, b)
            return password
        password = c
        password = securepassword(password)
        print(f"Your Encrpted Password is: {password}")
    elif e==1:
        f = input("Enter password to be decrpted: \n")
        while True:
	        j = input("Enter your Access Key: \n")
	        if j.isdigit():
		        break
	        else:
		        print("Please enter a number")
		        continue
        SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('4','f'),('f','4'),('a','@'),('@','a'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
        def securepassword(password):
            for a,b in SECURE:
                password = password.replace(b, a)
            return password
        password = f
        password = securepassword(password)
        print(f"Your Password is: {password}")
    else:
        print("Enter 0 or 1")
