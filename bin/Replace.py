import sqlite3
import bin.Password_Generation
import traceback
import sys


def replace_password():
    
    try:
        connection = sqlite3.connect('BASE_PASSWORD.db')
        cursor = connection.cursor()

        Site_new = input('Enter the name of the site you want to update: ')
        for i in cursor.execute('SELECT Site FROM Password Where Site != ?', (Site_new,)):
            sys.exit('The table has no data to change')
        print('\nUse your password - 1\nUse password generation - 2')
        Update_password = input('Do you want to use your password or generate a new one?: ')
        if Update_password == '1':
            Password_new = input('Enter a new password name : ')
            cursor.execute('UPDATE Password SET Passw=? WHERE Site =?', (Password_new, Site_new,))
            print("Password updated.")

        else:
            Password_new = bin.Password_Generation.generate()
            cursor.execute('UPDATE Password SET Passw=? WHERE Site =?', (Password_new, Site_new,))
            print("Password updated.")

        connection.commit()
        connection.close()
    except:
        print('There is no such site for changing password')
