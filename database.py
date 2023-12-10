import sqlite3
def db():
    conn = sqlite3.connect("Booking.db")
    cursor = conn.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Smoking (
                    ID_Smoking_Type INTEGER PRIMARY KEY, 
                    Smoking_Type VARCHAR(40) UNIQUE NOT NULL
                )
            ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Tables (
                    ID_Table_Location INTEGER PRIMARY KEY,
                    Table_Location VARCHAR(40) UNIQUE NOT NULL
                )
            ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Halls (
                    ID_Hall_Type INTEGER PRIMARY KEY, 
                    Hall_Type VARCHAR(40) UNIQUE NOT NULL
                )
            ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Admins (
                    ID_Admin INTEGER PRIMARY KEY, 
                    Name VARCHAR(30) NOT NULL,
                    Phone_Number INTEGER(11) UNIQUE NOT NULL,
                    Password VARCHAR(20) UNIQUE NOT NULL
                )
            ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Visitors (
                        ID_Visitors INTEGER PRIMARY KEY,
                        Name VARCHAR(30) NOT NULL,
                        Phone_Number INT(11) UNIQUE NOT NULL,
                        Status_Of_Booking VARCHAR(15) NOT NULL,
                        Table_Location_ID INT(1) NOT NULL, 
                        Hall_Type_ID INT NOT NULL,
                        Smoking_Type_ID INT NOT NULL,
                        FOREIGN KEY (Table_Location_ID) REFERENCES Tables(ID_Table_Location),
                        FOREIGN KEY (Hall_Type_ID) REFERENCES Halls(ID_Hall_Type),
                        FOREIGN KEY (Smoking_Type_ID) REFERENCES Smoking(ID_Smoking_Type)
                )
            ''')

    # cursor.execute('''
    #     INSERT INTO Smoking (Smoking_Type)
    #         VALUES
    #         ('Любой'),
    #         ('Только сигареты'),
    #         ('Только электронные сигареты'),
    #         ('Только кальян'),
    #         ('Нет')
    #             ''')
    #
    # cursor.execute('''
    #     INSERT INTO Tables (Table_Location)
    #         VALUES
    #         ('У окна'),
    #         ('У кухни'),
    #         ('У входа'),
    #         ('У картин')
    # ''')
    #
    # cursor.execute('''
    #     INSERT INTO Halls (Hall_Type)
    #         VALUES
    #         ('Большой'),
    #         ('Средний'),
    #         ('Малый'),
    #         ('На одну компанию')
    # ''')
    conn.commit()
    conn.close()
