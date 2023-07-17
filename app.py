evenorOdd=float(input("enter the number : "))
if evenorOdd%2==0:
   print("even")
else:
    print("odd")
#----------------------------------------------
primeorNot=int(input("enter the number : "))
for i in range(2,primeorNot):
    if primeorNot%i==0:
        print("not prime")
        break
else :
     print("prime") 