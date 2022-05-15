import bin.Create_Data_Base
import pyperclip
import sqlite3


def add_new_data():

    connection = sqlite3.connect('BASE_PASSWORD.db')
    cursor = connection.cursor()

    bin.Create_Data_Base.create_base()
    print('New data added')
    OUT = input('\nPress Enter to exit.')

    connection.commit()
    connection.close()
