#Write a function to swap the values of two variables through a function

x = input("Enter value of x:  ")
y = input("Enter value of y:  ")
temp = x
x = y
y = temp
print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))