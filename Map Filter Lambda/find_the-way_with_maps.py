
numbers = input("Enter a list of integers (space-separated): ").split()

result = list(map(lambda x: int(x) * 3,numbers ))

print("Triple of list numbers:",result)
