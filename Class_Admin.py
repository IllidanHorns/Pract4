from Class_Human import Human

class Admin(Human):
    password = ""

    def return_data(self):
        data = {
            "Name": Admin.name,
            "Phone_Number": Admin.phone_number,
            "Password": Admin.password
        }
        return data

