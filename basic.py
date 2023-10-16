list1 = [10,20,30]
list2 = [40,50,60]
list3=[]

for x,y in zip(list1, list2[::-1]):
    print(x,y)
