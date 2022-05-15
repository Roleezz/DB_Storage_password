import sqlite3
import bin.Password_Generation
import traceback
import sys


def create_base():

    try:
        connection = sqlite3.connect('BASE_PASSWORD.db')
        cursor = connection.cursor()

        Site = input("Name of the site: ")
        login = input("Enter your login: ")
        print('\nUse your password - 1\nUse password generation - 2')
        user_answer = input('Do you want to create your own password or use password generation?: ')

        if user_answer == '1':
            Passw = input('Enter your password: ')
        else:
            Passw = bin.Password_Generation.generate()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Password(
                        Site VARCHAR(100) NOT NULL UNIQUE,
                        login VARCHAR(100),
                        Passw VARCHAR(150))
        ''')
        cursor.execute('''INSERT INTO Password (Site, login, Passw)
                        VALUES(?, ?, ?)''', (Site, login, Passw))

        connection.commit()
        connection.close()

    except:
        print('Invalid data entry / Or you are trying to enter data that is available')
        sys.exit()
