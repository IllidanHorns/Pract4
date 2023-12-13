import sqlite3
from Class_Visitor import Visitor
from CRUD import CRUD

class Client_Active:
    client = Visitor

    def start_client(self):
        print("1. Изменить параметры брони")
        print("2. Создать бронь")
        print("3. Отменить заказ")
        try:
            client_choice = int(input())
        except:
            print("Вы ввели данные неправильно. Попробуйте ещё раз.")
            Client_Active.start_client(None)
            return None
        if client_choice == 1:
            Client_Active.__client_enter(1)
        elif client_choice == 2:
            Client_Active.__client_create_booking(None)
        elif client_choice == 3:
            Client_Active.__client_enter(2)
        else:
            print("Похоже вы ввели данные неправильно. Повторите пожалуйста.")
            Client_Active.start_client(None)
        return None


    def __client_create_booking(self):
        conn = sqlite3.connect("Booking.db")
        cursor = conn.cursor()
        client_name = input("Ваше имя - ")
        try:
            client_phone_number = int(input("Ваш номер телевона - "))
        except:
            print("Вы указали номер телефона неправильно!")
            Client_Active.__client_create_booking(None)
            return None
        if len(client_name) > 30:
            print("Похоже вы неправильно записали имя")
            Client_Active.__client_create_booking(None)
            return None
        elif (client_phone_number // 10 ** 10) not in range(1, 10) or client_phone_number // 10 ** 10 != 8:
            print("Простите, но ввели номер телефона неправильно. Введите 11 значный номер, начинающийся с 8")
            Client_Active.__client_create_booking(None)
            return None
        else:
            Client_Active.client.name = client_name
            Client_Active.client.phone_number = client_phone_number
            Client_Active.__choice_halls(None)

    def __choice_halls(self):
        rows = CRUD.get_information("Halls", "*", True)
        try:
            client_hall = int(input("Ваш зал - "))
        except:
            print("Вы неправильно ввели данные о зале!")
            Client_Active.__choice_halls(None)
            return None
        if CRUD.chek_for_id(rows, client_hall) == False:
            print("Вы неправильно ввели данные о зале!!")
            Client_Active.__choice_halls(None)
            return None
        else:
            Client_Active.client.hall_type_id = client_hall
            Client_Active.__choice_smoking_type(None)

    def __choice_smoking_type(self):
        rows = CRUD.get_information("Smoking", "*", True)
        try:
            client_smoking = int(input())
        except:
            print("Вы неправильно ввели данные о типе курения!")
            Client_Active.__choice_smoking_type(None)
            return None
        if CRUD.chek_for_id(rows, client_smoking) == False:
            print("Вы неправильно ввели данные о типе курения!")
            Client_Active.__choice_smoking_type(None)
            return None
        else:
            Client_Active.client.smoking_type_id = client_smoking
            Client_Active.__choice_table_location(None)

    def __choice_table_location(Self):
        rows = CRUD.get_information("Tables", "*", True)
        try:
            client_table_location = int(input())
        except:
            print("Вы неправильно ввели данные о расположении столика!")
            Client_Active.__choice_table_location(None)
            return None
        if CRUD.chek_for_id(rows, client_table_location) == False:
            print("Вы неправильно ввели данные о расположении столика!")
            Client_Active.__choice_table_location(None)
            return None
        else:
            Client_Active.client.table_Location_id = client_table_location
            Client_Active.__save_client_booking(None)

    def __save_client_booking(Self):
        data = Client_Active.client.return_data(None)
        try:
            CRUD.insertData("Visitors", data)
            print("Бронь заказана.")
        except:
            print("Похоже произошла ошибка. Возможно данные, которые вы ввели совпадают с существующими. Повторите повторно.")
            Client_Active.start_client(None)
        return None

    def __client_enter(Change: int):
        conn = sqlite3.connect("Booking.db")
        cursor = conn.cursor()
        client_name = input("Ваше имя - ")
        try:
            client_phone_number = int(input("Ваш номер телевона - "))
        except:
            print("Вы указали номер телефона неправильно!")
            Client_Active.__client_enter(1)
            return None
        cursor.execute(f"SELECT Status_Of_Booking from Visitors Where Name = '{client_name}' and Phone_Number = {client_phone_number}")
        a = cursor.fetchall()
        if a:
            if a[0] == ('Canceled',):
                print("Ваша бронь отменена!")
                return None
            else:
                names = CRUD.get_information("Visitors", "Name", False)
                phone_numbers = CRUD.get_information("Visitors", "Phone_Number", False)
                a = (client_name,)
                b = (client_phone_number,)
                if a in names and b in phone_numbers:
                    print("Вход выполнен!")
                    if Change == 1:
                        Client_Active.__client_change_data(client_name, client_phone_number)
                    elif Change == 2:
                        CRUD.update_data_client("Status_Of_Booking", "Canceled", client_name, client_phone_number)
                        print("Бронь отменена")
                else:
                    print("Ой! Войти не получилось")
                    Client_Active.__client_enter(None)
                return None
        else:
            print("Вход не выполнен. Вероятно такой записи нет.")

    def __client_change_data(old_name: str, old_phone_number: int):
        print("Какие данные хотите изменить?\n"
              "1. Имя \n"
              "2. Номер телефона \n"
              "3. Столик \n"
              "4. Зал \n"
              "5. Тип курения \n")
        try:
            client_choice = int(input())
        except:
            print("Похоже вы ввели данные неправильно!")
        try:
            match client_choice:
                case 1:
                    new_name = input("Введите новое имя - ")
                    CRUD.update_data_client("Name", new_name, old_name, old_phone_number)
                    print("Данные успешно изменены!")
                    return None
                case 2:
                    new_phone_number = int(input("Введите новый номер телефона - "))
                    CRUD.update_data_client("Phone_Number", new_phone_number, old_name, old_phone_number)
                    print("Данные успешно изменены!")
                    return None
                case 3:
                    rows = CRUD.get_information("Tables", "*", True)
                    new_table_location = int(input("Введите новый столик - "))
                    if CRUD.chek_for_id(rows, new_table_location) == True:
                        CRUD.update_data_client("Table_Location_ID", new_table_location, old_name, old_phone_number)
                        print("Данные успешно изменены!")
                    else:
                        print("Ошибка!")
                        Client_Active.__client_enter(1)
                        return None
                case 4:
                    rows = CRUD.get_information("Halls", "*", True)
                    new_hall_type = int(input("Введите новый зал - "))
                    if CRUD.chek_for_id(rows, new_hall_type) == True:
                        CRUD.update_data_client("Hall_Type_ID", new_hall_type, old_name, old_phone_number)
                        print("Данные успешно изменены!")
                    else:
                        print("Ошибка!")
                        Client_Active.__client_enter(1)
                        return None
                case 5:
                    rows = CRUD.get_information("Smoking", "*", True)
                    new_smoking_type = int(input("Введите новый тип курения - "))
                    if CRUD.chek_for_id(rows, new_smoking_type) == True:
                        CRUD.update_data_client("Smoking_Type_ID", new_smoking_type, old_name, old_phone_number)
                        print("Данные успешно изменены!")
                    else:
                        print("Ошибка!")
                        Client_Active.__client_enter(1)
                        return None
                case _:
                    print("Ошибка!")
                    Client_Active.__client_enter(1)
                    return None
        except:
            print("Похоже, что вы введи данные неправльно.")
            Client_Active.__client_enter(1)
            return None
        return None
