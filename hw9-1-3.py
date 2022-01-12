# Ryan Lugo: RJL 1/12/22

def find_thing(item,element):

    if type(item) == list:
        for i,v in enumerate(item):
            for p,letter in enumerate(v):
                if letter == element:
                    return p
            else:
                if i == len(item)-1:
                    return -1
                else:
                    continue
    elif type(item) == str:
        for i,v in enumerate(item):
            if v == element:
                return i
            else:
                if i == len(item)-1:
                    return -1
                else:
                    continue
    else:
        print("The current first argument passed, is not a string or a list.")

print(find_thing(["hello"],"o"))