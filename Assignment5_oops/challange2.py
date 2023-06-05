class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return self.num1+self.num2
    
    def substract(self):
        return self.num1-self.num2
    
    def multiply(self):
        return self.num1*self.num2
    
    def divide(self):
        return self.num1/self.num2
    
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
calculator=Calculator(num1,num2)
add=calculator.add()
sub=calculator.substract()
mul=calculator.multiply()
div=calculator.divide()

option=int(input("Which operation do you want to perform \n1: Addition,\n2: Substraction,\n3: Multiplication,\n4: Division,\n5: All operation \n"))
if option==1:
    print("sum = ",add)
elif option==2:
    print("Difference = ",sub)
elif option ==3:
    print("Product = ",mul)
elif option==4:
    print("quoitent = ",div)
elif option==5:
    print("sum = ",add,"\nDifference = ",sub,"\nProduct = ",mul,"\nquoitent = ",div)
else:
    print("Invalid Option")



