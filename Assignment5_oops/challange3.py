class Student:
    
    def setName(self,new_name):
        self._name=new_name
        return new_name
    def getName(self,_name):
        return self._name
    def setRollNumber(self,new_rollno):
        self._rollno=new_rollno
        return new_rollno
    def getRollNumber(self,_rollno):
        return rollno
    
student=Student()
name=str(input("Enter the name of Student:"))
student.setName(name)
rollno=int(input("Enter the rolLno:"))
student.setRollNumber(rollno)
name_of_student=student.getName(name)
rollno_of_Student=student.getRollNumber(rollno)
print("Name and Rollno of student is:",name_of_student,rollno_of_Student)