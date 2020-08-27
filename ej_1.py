# -*- coding: utf-8 -*-

def valid_usrname (usrname):
	if len(usrname) < 6:
		return "El nombre de usuario debe contenter al menos 6 caracteres"
	elif len(usrname) > 12:
		return "El nombre de usuario de no puede contener mas de 12 caracteres"
	elif not(usrname.isalnum()):
		return "El nombre de usuario puede contener solo letras y numeros"
	else:
		return True
		
def valid_password (password):
	if len(password) < 8 or not(password.isalpha()) or not(password.islower()) or not(password.isupper()) or password.count(" ") > 0:
		return "La contraseña elegida no es segura"
	else:
		return True

usrname = input("Indique su nombre de usuario: ")
usrname_validation = valid_usrname(usrname)
print (usrname_validation)
password = input("Ingrese su password: ")
password_validation = valid_password(password)
print (password_validation)