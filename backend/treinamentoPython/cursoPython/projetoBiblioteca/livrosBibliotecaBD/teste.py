import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456789Teste*',
                              host='localhost',
                              database='BIBLIOTECA')

print(cnx)
cnx.close()