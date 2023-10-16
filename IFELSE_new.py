cfts = str(input("Are you part of CFTS(Y/N):"))
csat= int(input("What is your Csat score?"))
if (cfts=='y' and csat >= 100):
    print("your team is eligible for funds")
else:
    print("better luck next time")
print("goodbye!")

