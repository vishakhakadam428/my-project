num = int(input("Enter the num: "))
sum_of_num = 0
temp = num
while temp<0:
    digit=temp%10
    sum_of_digit+=digit**3
    temp//=10
if sum_of_num==num:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")
    