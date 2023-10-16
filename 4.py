temp= float(input("enter the Temerature:"))
unit = input("F or C:")
if unit =="F":
    print("Temparature in C is:", (temp-30)/2)
elif unit =="C":
    print("Temparature in F is:", (temp*1.8)+32)
