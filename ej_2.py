# -*- coding: utf-8 -*-
import MySQLdb

username = 'root'
password = ''
servername = 'localhost'
dbname = 'aumentos'

def run_query (query=''):
	datos = [servername, username, password, dbname]
	
	conn = MySQLdb.connect(*datos)
	cursor = conn.cursor()
	cursor.execute(query)
	
	if query.upper().startwith('SELECT'):
		data = cursor.fetchall()
	else:
		conn.commit()
		data = None
	
	cursor.close()
	conn.close
	
	return data
	
query = "SELECT * FROM aumentos_cartera"
result = run_query(query)
print (result)
