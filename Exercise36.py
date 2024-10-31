#wap to program check prime number or not
num = int(input("enter the number :"))
if num <= 1:
    print("not prime")
elif num == 2:
    print("prime")
else:
    prime = True
    for i in range(2,num):
      if num % i == 0:    
        prime = False
        break
    if prime:  
      print("prime")
    else:
      print("not prime")