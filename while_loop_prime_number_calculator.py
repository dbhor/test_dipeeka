#prime number calculator

choice ='y'
while (choice =='y'):
    num=int(input("enter a number:"))
    i = 2
    while (i <num):
        j=2
        while (j <= (i/j)):
            if not(i%j): break
            j= j+1
        if (j> (i/j)):
            print("{} is a prime number".format(i))
        i= i+1
    choice = str(input("Do you want to continue Y/N?")).lower()
print("thank you for using prime calculator")














