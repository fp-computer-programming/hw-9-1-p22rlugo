# Ryan Lugo: RJL 1/12/22

def even_index(table):

    even = []

    if type(table) == list:
        for i,v in enumerate(table):
            
            if i % 2 == 0:
                even.append(v)
        return even
    else:
        print("This is not a table.")

print(even_index([1,2,3,4,5,6,7]))