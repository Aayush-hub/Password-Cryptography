import random
if __name__ == "__main__":
    inp = input("Enter password to be encrypted: \n")
    d = int(input("Set Access Key: \n"))
    SECURE = (('s', '$'),('i', '|'), ('x', '*'), ('k','+'), ('g','4'),('4','f'),('f','4'),('a','@'),('@','a'),('o','0'),('X','x'),('%','#'),('w','^'),('h','='),('H','~'),('r',','),('e','/'),('t','<'),('q','>'),('l','?'),('c','1'))
    def securepassword(password):
        for a,b in SECURE:
            password = password.replace(a, b)
        return password
    password = inp
    password = securepassword(password)
    print(f"Your Encrpted Password is: {password}")
