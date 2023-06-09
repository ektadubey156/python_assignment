#Write a program to display the number of lines in the file and size of a file in bytes
import os

print("Enter the Name of File: ")
name = input()
size= os.path.getsize(name)
print("Size of given file is:")
print(size)