W = float(input("Weight:"))
unit = input("(K)g or (L)bs (Case Sensitive):")
if unit == "K":
   print("your weight in Lbs is:", W*2.205)
elif unit == "k":
   print("your weight in LBS is:", W * 2.205)
elif unit == "L":
   print("Your weight in Kgs is:", W/ 2.205)
elif unit == "l":
   print("Your weight in KGS is:", W / 2.205)










