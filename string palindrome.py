#Python program to check if a string is palindrome or not.
def check(str):
  if str==str[::-1]:
    return "The string is a palindrome"
  else:
    return "The string is not a palindrome"
str=input("Enter string:")
print(check(str))