class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2+self.y**2+self.z**2

# num1=int(input("Enter three numbers:\n"))
# num2=int(input())
# num3=int(input())
# point=Point(num1,num2,num3)

num = input('Enter three numbers : ').split()
point = Point(int(num[0]), int(num[1]), int(num[2]))

result=point.sqSum()
print("Sum of squre of Numbers:",result)
