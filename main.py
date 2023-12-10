import sqlite3
import sys

import Functions_Of_Client
from Class_Visitor import Visitor
from Class_Admin import Admin
from CRUD import CRUD
from database import db
from Functions_Of_Client import *
from Functions_Of_Admin import *
def main():
    db()
    while True:
        print("Выберите вашу роль - ")
        print("1. Клиент \n"
              "2. Администратор \n"
              "3. Закончить сессию")
        user_role = input()
        if user_role:
            if user_role.isdigit():
                user_role = int(user_role)
            else:
                print("Введите данные правильно!!!!!")
        if user_role == 1:
            Client_Active.start_client(None)
        elif user_role == 2:
            Admin_active.start_of_admin(None)
        elif user_role == 3:
            sys.exit()
        else:
            print("Введите данные правильнооо!")

main()

