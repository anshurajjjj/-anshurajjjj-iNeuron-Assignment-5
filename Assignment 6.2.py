#Write a python script to check whether a given number is divisible by 5 or not
n=int(input("Please Enter any Positive Integer:"))
if((n%5==0)):
    print("Given Number {0} is Divisible by 5".format(n))
else:
    print("Given Number {0} is Not Divisible by 5".format(n))
