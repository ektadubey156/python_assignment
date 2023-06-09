# Python program to display the Fibonacci sequence
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
p=int(input("Enter till you want to run:"))
if p<= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(p):
       print(fibo(i))