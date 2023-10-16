import pickle
import json
def serialize(obj, file, type):
    if type == 'pickle':
        with open(file, 'wb')as f:
            pickle.dump(obj,f)
    elif type =='json':
        import json
        with open(file, 'w')as f:
            json.dump(obj, f)
    else:
        print("invalid serialization")

def deserialization(file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'rb')as f:
            obj = pickle.load(f)
        return obj
    elif type == 'json':
        import json
        with open(file, 'r') as f:
            obj =json.load(f)
        return obj
    else:
        print("invalid deserialization")

if __name__ == "__main__":
    d1 = {'a':'x', 'b':'y','c':'z', 30:(2 ,3, 'a')}
    serialize (d1, '../../../Library/Application Support/JetBrains/PyCharmCE2021.2/scratches/show_sys_o/a.dat', 'pickle')

    mydict = deserialization(
        '../../../Library/Application Support/JetBrains/PyCharmCE2021.2/scratches/show_sys_o/a.dat', 'pickle')
    print(f'pickle:{mydict}')


    serialize(d1, '../../../Library/Application Support/JetBrains/PyCharmCE2021.2/scratches/show_sys_o/a.json', 'json')
    x= deserialization('../../../Library/Application Support/JetBrains/PyCharmCE2021.2/scratches/show_sys_o/a.json', 'json')
    print(f'json:{x}')





