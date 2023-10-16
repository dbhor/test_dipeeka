list=[3,2]
for i in list:
    list.insert(0,7)     #insert() method inserts an element at given index position. (index, element)
    list.append("hello")  #"append() method adds element in the end of the list.
    print(list)
    print(list.index("hello"))   # this index() method, will provide the element's exact index. example, hello is at index 3 in list.
    break

