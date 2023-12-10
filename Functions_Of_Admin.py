import sqlite3
from Class_Admin import Admin
from CRUD import CRUD

class Admin_active():
    admin = Admin
    def start_of_admin(self):
        print("1. Зарегестрироваться как администратор")
        print("2. Войти в сиситему как администратор")
        try:
            user_choice = int(input())
        except:
            print("Вы ввели данные неправильно! Попробуйте ещё раз")
            Admin_active.start_of_admin(None)
            return None
        if user_choice == 1:
            Admin_active.__admin_reg(None)
        elif user_choice == 2:
            Admin_active.__admin_enter(None)
        else:
            print("Похоже вы ввели даные неправильно! Давайте попробуем заново")
            Admin_active.start_of_admin(None)
            return None

    def __admin_reg(self):
            try:
                Admin_active.admin.name = input("Введите своё имя - ")
                Admin_active.admin.phone_number = int(input("Введите свой номер телефона - "))
                Admin_active.admin.password = input("Введите пароль - ")
            except:
                print("Похоже вы ввели данные некоректно. Попробуйте ещё раз")
            if len(Admin_active.admin.name) > 30:
                print("Вы ввели слишком длинное имя. Попробуйте сократить и повторите попытку")
                Admin_active.start_of_admin()
            elif (Admin_active.admin.phone_number // 10 ** 10) not in range(1, 10) or Admin_active.admin.phone_number // 10 ** 10 != 8:
                print("Простите, но ввели номер телефона неправильно. Введите 11 значный номер, начинающийся с 8")
                Admin_active.__admin_reg(None)
                return None
            else:
                data = Admin_active.admin.return_data(None)
                try:
                    a = CRUD.insertData("Admins", data)
                    if a == True:
                        print("Вы успешно зарегестрированы!")
                except:
                    print("Произошла ошибка регистрации. Давайте повторим заново")
                    Admin_active.__admin_reg(None)
            return None

    def __admin_enter(self):
        try:
            conn = sqlite3.connect("Booking.db")
            cursor = conn.cursor()
            admin_name = input("Введите ваше имя - ")
            admin_password = input("Введите ваш пароль - ")
            cursor.execute(f"SELECT * from Admins Where Name = '{admin_name}' and Password = '{admin_password}'")
            a = cursor.fetchone()
            if a == None:
                print("Такой записи не существует!")
                Admin_active.__admin_enter(None)
            print("Выберите, что хотите сделать: \n"
                  "1. Добавить информацию в таблицу\n"
                  "2. Изменить свои данные \n"
                  "3. Получить информацию с таблицы \n"
                  "4. Удалить данные\n")
            try:
                admin_choice = int(input("Ваш выбор - "))
            except:
                print("Вы ввели данные неправильно!")
                Admin_active.__admin_enter(None)
            match admin_choice:
                case 1:
                    Admin_active.__admin_add_data(None)
                case 2:
                    Admin_active.__admin_change_himself_data(None, admin_name, admin_password)
                case 3:
                    Admin_active.__admin_print_data(None)
                case 4:
                    Admin_active.__admin_delete(None)
        except:
            print("Похоже вы ввели данные неправильно!")

    def __admin_add_data(self):
        print("В какую из таблиц вы хотите добавить значение? \n"
                  "1. Залы \n"
                  "2. Столики \n"
                  "3. Курение")
        try:
            admin_choice = int(input())
        except:
            print("Введите данные правильно")
            Admin_active.__admin_add_data()
        match admin_choice:
            case 1:
                new_hall = input("Новый зал - ")
                CRUD.insertData("Halls", {"Hall_Type" : new_hall})
            case 2:
                new_table = input("Новый столик - ")
                CRUD.insertData("Tables", {"Table_Location" : new_table})
            case 3:
                new_smoking = input("Новый тип курения - ")
                CRUD.insertData("Smoking", {"Smoking_Type": new_smoking})
            case _:
                print("Вы ввели данные неправильно!")
                Admin_active.__admin_add_data()

    def __admin_change_himself_data(self, name, password):
        print("Выберите, что хотите изменить - \n"
              "1. Имя \n"
              "2. Номер телефона \n"
              "3. Пароль")
        try:
            admin_choice = int(input("Изменить - "))
        except:
            print("Вы ввели данные неправильно! Давайте попробуем ввести заново")
        try:
            match admin_choice:
                case 1:
                    new_name = input("Новое имя - ")
                    CRUD.update_data_admin("Name", new_name, name, password)
                    print("Данные успешно изменены")
                case 2:
                    new_phone_number = int(input("Новый номер телефона - "))
                    CRUD.update_data_admin("Phone_Number", new_phone_number, name, password)
                    print("Данные успешно изменены")
                case 3:
                    new_password = input()
                    CRUD.update_data_admin("Password", new_password, name, password)
                    print("Данные успешно изменены")
        except:
            print("Похоже данные были введены неправильно! Давайте попробуем ввести их снова")
            Admin_active.__admin_enter(None)
            return None

    def __admin_print_data(self):
        try:
            print("Названия таблиц - ")
            CRUD.get_information(inf="Таблицы")
            table_name = input("Введите название таблицы - ")
            CRUD.get_information(table=table_name, inf="Колонки")
            column_name = input("Введите  название колонки - ")
            CRUD.get_information(table_name, column_name, True)
        except:
            print("Похоже, что вы допустили ошибки при вводе данных")

    def __admin_delete(self):
        try:
            print("Название таблиц - ")
            CRUD.get_information(inf="Таблицы")
            table_name = input("Введите название таблицы - ")
            print("Названия колонок - ")
            CRUD.get_information(table=table_name,inf="Колонки")
            column = input("Ваша колонка - ")
            conditional = input("Введите условие - ")
            CRUD.delete(table_name, column, conditional)
            return None
        except:
            print("Произошла ошибка при удалении.")
