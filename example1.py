#str ="Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

#task2. Write a Python program to get the Python version you are using
#ans:
#import sys  >>> import system specific module to use its functions.
#print(sys.version)

"""
import datetime
NOW= datetime.datetime.now()
print(NOW)
print(NOW.strftime("%Y/%m/%d time is %H:%M:%S"))

"""

#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#solution =
"""
name =input("enter your first and last name")
print(name)
Name= name.split(" ")
print(Name)
print(''.join(Name[::-1]))"""

#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#solution=
"""
seq= input("enter a series of numbers:")
a_list = seq.split(",")
print(a_list)
print(tuple(a_list)) """

#Write a Python program to accept a filename from the user and print the extension of that.
#solution =
file= input("enter a file name:")
print(file)













