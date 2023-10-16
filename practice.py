import time
import datetime
import json
def read_input(file='file.json'):
    with open(file) as inputfile:
        #print(inputfile)
        inputjson = json.load(inputfile)
        return(inputjson)


if __name__ == '__main__':
    start = time.time()
    print("start time is: {}".format(start))
    input = read_input()
    print("Received input : {}".format(input))

    #for x in input['food']['item']['cost']:
        #print("cost of the food is: {}".format(x))
    for x in input['food']:
        print(x)
        f=input['food'][x]
        print(f)
        fruit_name=f['name']
        print(fruit_name)
        fruit_cost= f['cost']
        print(fruit_cost)