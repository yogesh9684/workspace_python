# def test(num):
#     if num>10:
#         print("number is big")
#     else:
#         print("number is small")
# print(test(6))

# def fact(num):
#     if(num > 1):
#         num=num*fact(num-1)
#     return num
# num = int(input("Enter the Number="))
# print(fact(num))

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

