print("Crea tu cuenta")
print("Pon aqui tu nombre de usuario")
user = input()
print("Pon aqui tu contraseña")
passw = input()

input()

print("Inicia sesion a tu cuenta")
print("Pon aqui tu nombre de usuario")
userInicio = input()
print("Pon aqui tu contraseña")
passwInicio = input()
while userInicio != user or passwInicio != passw:
    print("Vuelve a introducir usuario y contraseña")
    print("Inicia sesion a tu cuenta")
    print("Pon aqui tu nombre de usuario")
    userInicio = input()
    print("Pon aqui tu contraseña")
    passwInicio = input()
if userInicio == user and passwInicio == passw:
    print("Has iniciado sesion")