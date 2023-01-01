#Write a python script to check whether a given number is a three digit number or not.
n=int(input("Enter any number: "))
if n>=100 and n<=999:
    print("n is a 3 digit number")
if n<100 and n>999:
    print("n is not a 3 digit number")
