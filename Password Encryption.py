inp = input("Enter password to be encrypted: \n")     #taking password to be encrypted
d = int(input("Set Access Key: \n"))                  #setting access key
SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('a','@'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
def securepassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)             #replacing orginal elements to encrypted ones.
    return password
password = inp
password = securepassword(password)
print(f"Your Encrpted Password is: {password}")       #printing encryted password
