# baza danych - system przetwarzania i przechowywania danych (silnik)
# sql, nosql
# mysql, oracle, postgres, mssql
# terradata

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_db.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych:", e)
finally:
    if sql_connection:
        sql_connection.close()
