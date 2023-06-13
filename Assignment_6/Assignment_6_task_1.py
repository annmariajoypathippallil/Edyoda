import json

# ------ASSIGNMENT 1 -------
class Employee:
    employee_list = []
    header = []

    def read_file(self):
        with open("C:\\Users\\YOGA\\Desktop\\Edyoda\\Assignment_6\\employee.json","r") as file:
            data=json.load(file)
            # print(type(data))
            for i in data.keys():
                # print(data[i])
                self.save_to_list(data[i])
                
                # for j in data[i].keys():
                #     # print(j)
                #     print(j, '-->', data[i][j])
                # print("\n")

    def save_to_list(self, data):
        temp_list = []
        for j in data.values():
            temp_list.append(j)
        for i in data.keys():
            self.header.append(i)
        self.employee_list.append(temp_list)


    def display_employee(self):
        for i in self.employee_list:
            # print(i)
            for j,k in zip(i,self.header):
                print(k,'\t\t----->', j)
            print('---------------------------------------------')


# -----ASSIGNMENT2--------


    def write_to_json(self):
        data={
            "kerala":"Trivandram",
            "Tamil Nadhu":"Chennai",
            "Andhra pradesh":"Amaravathi",
            "Karnataka":"Bangaluru",
            "Rajasthan":"Jaipur",
            "Bhiar":"Patna",
            "Gujarat":"Gandhinagar"
            }
        with open("C:\\Users\\YOGA\\Desktop\\Edyoda\\Assignment_6\\state_capital.json",'w') as file:
            json.dump(data,file,indent=4)


    







obj = Employee()
obj.read_file()
obj.display_employee()
obj.write_to_json()

