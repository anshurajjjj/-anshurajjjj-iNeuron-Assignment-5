#Write a python script to accept one complex number from the user and display the
#greater number between real part and imaginary part
x=int(input("Enter any number"))
y=int(input("Enter any number"))
z=complex(x,y)
print(z)
print(z.real)
print(z.imag)
if x>y:
    print("Real part is greater than imaginary part.")
if y>x:
    print("Imaginary part is greater than real part.")
