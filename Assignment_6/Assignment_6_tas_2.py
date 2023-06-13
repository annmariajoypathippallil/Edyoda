class Dog:
    def __init__(self,name,age,coat_color):
         self.name=name
         self.age=age
         self.coat_color=coat_color
    def description(self):
         print("Name:",self.name,"\n Age :",self.age)
    def get_info(self):
         print("Coat Color:",self.coat_color)


class JackRussellTerrier(Dog):
     def __init__(self,name,age,coat_color):
          super().__init__(name,age,coat_color)
     def jack(self):
          print("JackRussellTerrier is Running!")

class Bulldog(Dog):
     def __init__(self,name,age,coat_color):
          super().__init__(name,age,coat_color)
     def bull(self):
          print("Bulldog is Barking!")



dog1=Dog("Jimmy",11,"Blue")
dog1.description()
dog1.get_info()
     
dog2=JackRussellTerrier("Scooby",5,"green")
dog2.description()
dog2.get_info()
dog2.jack()

dog3=Bulldog("Tiger",7,"White")
dog3.description()
dog3.get_info()
dog3.bull()
     


     
        