num = int(input("Enter the num: "))
if num==1 and num==2:
    print(f"{num} is Prime")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")


