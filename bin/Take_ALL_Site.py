import sqlite3
import traceback


def take_all_name_site():

    try:
        connection = sqlite3.connect('BASE_PASSWORD.db')
        cursor = connection.cursor()

        for i in cursor.execute('SELECT Site FROM Password'):
            print('\nSite = {0}'.format(i[0]))
        OUT = input('\nPress ENTER to exit.')

    except:
        print('No data to show')
