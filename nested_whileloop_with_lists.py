a = ["mx", "ptx", "qfx"]
while a:
    print(a.pop(0))
    b= ["Junos", "EVO"]
    while not len(b) == 1:
        print("\t{}".format(b.pop(-1)))

