def sum_of_numbers(lst):
    sum=0
    for i in lst:
        sum+=int(i)
    return sum



lst=input("Enter the numbers (Seperated by spaces):")
lst=lst.split(" ")
result=sum_of_numbers(lst)
print("Sum of numbers is :",result)







