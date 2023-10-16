dict= {}
dict["k"]="hey"
dict["b"]=2
print(dict)
for i in dict:
    print(dict.keys())   ##this keys() method, returns a list of keys.
    print(dict["b"])  ##this is printing a value of key "b".
    print(dict.items()) ####this items() method if dict, returns, a list of tuples of key,value pair.
    print(dict.values()) ##this keys() method, returns a list of values.
