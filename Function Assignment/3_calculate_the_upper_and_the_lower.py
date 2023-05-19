def calculating_count_of_upper_and_lower(string):
    upper_count=0
    lower_count=0
    for i in string:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    print("No. of uppercase Character: ",upper_count)
    print("No. of lowercase Character: ",lower_count)



string = input("Enter the string:")
calculating_count_of_upper_and_lower(string)
            
