import sqlite3
import traceback
import sys

def delete_data():

    try:
        connection = sqlite3.connect('BASE_PASSWORD.db')
        cursor = connection.cursor()

        print('Do not forget that all data associated with this site will be deleted.')
        Delete = input('Enter the name of the site to delete: ')
        for i in cursor.execute('SELECT Site FROM Password Where Site != ?', (Delete,)):
            sys.exit('This site name is already in the database')
        for i in cursor.execute('DELETE FROM Password WHERE Site = ?', (Delete,)):
            print('Data deleted.')
            OUT = input('Press ENTER to exit')
            connection.commit()
            connection.close()

    except:
        
        print('No data to delete')
