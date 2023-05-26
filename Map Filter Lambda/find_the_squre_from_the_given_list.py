numbers = input("Enter a list of integers (space-separated): ").split()

result = list(map(lambda x: int(x) ** 2,numbers ))

print("Square the elements of the list:",result)
