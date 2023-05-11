lst = []
while True:
    tuple_str = input("Enter a tuple (in the format 'a,b'), or press enter to stop: ")
    if tuple_str == "":
        break
    else:
        tuple_vals = tuple(map(int, tuple_str.split(",")))
        lst.append(tuple_vals)
print(lst)
sorted_list = sorted(lst, key=lambda x: x[-1])
print(sorted_list)



