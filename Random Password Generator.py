import random

print("Welcome to Random Password Generator!..")

Hpwd=int(input("Enter How many password can generated : "))
lpwd=int(input("Enter How many Digits you need? : "))
pwdchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910!@#*"

for i in range(Hpwd):
    pwd=""
    for char in range(lpwd):               
        pwd= pwd + random.choice(pwdchar) #pwd=pwd +random.choice(pwdchar)
    print("new passwords : ", pwd)        #pwd=0 + liberay.method(variable passing)
    
