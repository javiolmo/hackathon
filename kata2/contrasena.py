
# definimos la contraseña
password = "contraseña"

# pedimos al usuario que inserte una contraseña
password_del_usuario = input ("introduzca la contraseña: ")

# la pasamos a minusculas para hacer la comparación
password_del_usuario = password_del_usuario.lower()

# logica que comprueba si
if password == password_del_usuario:
    print("El password es correcto")
else:
    print("El password no coincide")
