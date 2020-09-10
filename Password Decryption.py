f = input("Enter password to be decrpted: \n")
d = int(input("Enter Access Key: \n"))
        
SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('4','f'),('f','4'),('a','@'),('@','a'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
def securepassword(password):
    for a,b in SECURE:
        password = password.replace(b, a)
    return password
password = f
password = securepassword(password)
print(f"Your Encrpted Password is: {password}")
