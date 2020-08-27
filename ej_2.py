# -*- coding: utf-8 -*-
import mysql.connector

username = 'root'
password = ''
servername = 'localhost'
dbname = 'aumentos'

def run_query (query=''):
	datos = [servername, username, password, dbname]
	print (query)
	conn =  mysql.connector.connect(host=servername,database=dbname,user=username,password=password)
	cursor = conn.cursor()
	cursor.execute(query)
	
	data = cursor.fetchall()
	
	cursor.close()
	conn.close()
	
	return data
	
query = "SELECT * FROM aumentos_cartera"
result = run_query(query)
print (result)
