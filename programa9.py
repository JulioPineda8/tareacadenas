fechaDeNacimiento = input("ingrese su fecha de nacimiento, tiene que escribirla en el siguiente formato 06/10/23: ")
dia = fechaDeNacimiento[:fechaDeNacimiento.find("/")]
mesAnio= fechaDeNacimiento[fechaDeNacimiento.find("/")+1:]

mes= mesAnio[:mesAnio.find("/")]
anio = mesAnio[mesAnio.find("/")+1:]
print("el dia de su nacimiento es: ", dia)
print("el mes de su nacimiento es: ", mes) 
print("el año de su nacimiento es: ", anio)