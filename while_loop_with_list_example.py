lines = list()
user_input= input("do you want to enter more lines Y/N:")
while user_input=='Y':
    line= input("next line: ")
    lines.append(line)
    user_input=input("do you want to enter more lines Y/N:")
    print(lines)
print("you are now outside of while loop")
for line in lines:
    print(line)



