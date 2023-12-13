import sqlite3

class CRUD:
    @staticmethod
    def executeQuerry(query, value = None):
            with sqlite3.connect("booking.db") as conn:
                cursor = conn.cursor()
                if value:
                    cursor.execute(query, value)
                else:
                    cursor.execute(query)

    @staticmethod
    def insertData(table, data):
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join("?" for _ in data)
            querry = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            CRUD.executeQuerry(querry, list(data.values()))
            print("Данные успешно добавлены!")
            return True
        except:
            print("Произошла ошибка внесения данных!")
            return False

    @staticmethod
    def update_data_client(column, new_data, name, phone_number):
        if type(new_data) == str:
            querry = f"UPDATE Visitors SET '{column}' = '{new_data}' WHERE Name = '{name}' and Phone_Number = {phone_number}"
        else:
            querry = f"UPDATE Visitors SET {column} = {new_data} WHERE Name = '{name}' and Phone_Number = {phone_number}"
        CRUD.executeQuerry(querry)

    @staticmethod
    def update_data_admin(column, new_data, name, password):
        if type(new_data) == str:
            querry = f"UPDATE Admins SET '{column}' = '{new_data}' WHERE Name = '{name}' and Password = '{password}'"
        else:
            querry = f"UPDATE Admins SET {column} = {new_data} WHERE Name = '{name}' and Password = '{password}'"
        CRUD.executeQuerry(querry)

    @staticmethod
    def update_data(table, column, new_data):
        try:
            querry = f"UPDATE {table} SET {column} = {new_data}"
            CRUD.executeQuerry(querry)
        except:
            print("Произолка ошибка изменения данных!")
    @staticmethod
    def get_information(table = None, column=None, chek_to_print:bool=False, inf:str = ""):
        conn = sqlite3.connect("Booking.db")
        cursor = conn.cursor()
        def print_rows(rows):
            for row in rows:
                print(*row, sep=". ")
        if inf == "Таблицы":
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            rows = cursor.fetchall()
            print_rows(rows)
        elif inf == "Колонки":
            cursor.execute(f"pragma table_info({table});")
            rows = cursor.fetchall()
            for i in rows:
                print(i[1])
        else:
            cursor.execute(f"SELECT {column} from {table}")
            rows = cursor.fetchall()
            if chek_to_print == True:
                print_rows(rows)
        return rows

    @staticmethod
    def delete(table, column, conditional):
        try:
            conditional = int(conditional)
        except:
            pass
        if type(conditional) == int:
            querry = f"DELETE from {table} where {column} = {conditional}"
        else:
            querry = f"DELETE from {table} where {column} = '{conditional}'"
        CRUD.executeQuerry(querry)

    @staticmethod
    def chek_for_id(massive, chek):
        a = []
        for i in massive:
            a.append(i[0])
        if chek in a:
            return True
        else:
            return False


