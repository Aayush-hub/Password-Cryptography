f = input("Enter password to be decrpted: \n")    #enter password to be dcrypted
d = int(input("Enter Access Key: \n"))            #enter access key
        
SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('a','@'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
def securepassword(password):
    for a,b in SECURE:
        password = password.replace(b, a)    #replacing encrypted elements with original ones.
    return password
password = f
password = securepassword(password)
print(f"Your Encrpted Password is: {password}") #printing original password.
