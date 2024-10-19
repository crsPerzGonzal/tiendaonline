import mysql.connector

mysql_confi = {
    'host': '127.0.0.1',
    'user':'root',
    'database':'tiendaonline',
    'auth_plugin':'mysql_native'
}
connetion = mysql.connector.connect(**mysql_confi, autocommit=True)
def get_connetion():
    return connetion