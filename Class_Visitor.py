from Class_Human import Human
class Visitor(Human):
        table_Location_id = 0
        hall_type_id = 0
        smoking_type_id = 0

        def return_data(self):
                data = {"Name": Visitor.name,
                        "Phone_number": Visitor.phone_number,
                        "Status_Of_Booking": "Actual",
                        "Table_Location_ID": Visitor.table_Location_id,
                        "Hall_Type_ID": Visitor.hall_type_id,
                        "Smoking_Type_ID": Visitor.smoking_type_id}
                return data