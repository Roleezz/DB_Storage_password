import pyperclip
import sqlite3
import traceback
import sys


def take_password():

    try:
        connection = sqlite3.connect('BASE_PASSWORD.db')
        cursor = connection.cursor()

        name = input('\nEnter site name to get password: ')
        for i in cursor.execute('SELECT Passw FROM Password WHERE Site != ?', (name,)):
            sys.exit()
        for i in cursor.execute('SELECT Passw FROM Password WHERE Site = ?', (name,)):
            print('Your password has been received.')
            OUT = input('\nPress ENTER to exit.')
            return pyperclip.copy(''.join(i))

    except:
        print('Apparently there is no data in the table\nOr they were entered incorrectly')
