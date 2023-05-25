#Write a program in python to check a number whether it is prime or not
n=int(input("Enter a number:"))
if n==1:
    print("Entered element is not prime")
elif n>1:
    for i in range(2,n):
        if(n%i)==0:
            print("Entered number is not prime")
            break
        else:
            print("Entered element is prime")
            break