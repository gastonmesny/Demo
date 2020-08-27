# -*- coding: utf-8 -*-

def valid_usrname (usrname)
	if len(usrname) < 6:
		return "El nombre de usuario debe contenter al menos 6 caracteres"
	elif len(usrname) > 12:
		return "El nombre de usuario de no puede contener mas de 12 caracteres"
	elif !usrname.isalnum():
		return "El nombre de usuario puede contener solo letras y numeros"
	else
		return True
		
def valid_password (password):
	if len(password) < 8 or !password.isalpha() or !password.islower() or !password.isupper() or password.count(" ") > 0:
		return "La contraseña elegida no es segura"
	else
		return True

usrname = raw_input("Indique su nombre de usuario: ")
print valid_usrname(usrname)
password = raw_input("Ingrese su password: ")
print valid_password(password)