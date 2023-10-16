list= ['3','4','5']
for i in list:
    if i == '5':
        print(i[0])
    else:
        print("out of if")
print("out of for loop")

def isprime(n):
     if n <=1:
        return False;
     for i in range(2, n):
        print(i, "in for loop")
        if n % i ==0:
            print(i, "in if loop")
            return False;
            print(i,"after return false")
     return True
     print(i, "after return true")