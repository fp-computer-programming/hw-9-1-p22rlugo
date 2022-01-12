# Ryan Lugo: RJL 1/12/22

def odd_element(table):

    odd = []

    if type(table) == list:
        for i,v in enumerate(table):
            
            if not i % 2 == 0:
                odd.append(v)
        return odd
    else:
        print("This is not a table.")

print(odd_element([1,2,3,4,5,6,7]))