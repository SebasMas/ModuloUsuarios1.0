Datos_personas = [
    {
        "name": "Alejandro Villegas",
        "age": 17,
        "address": "Dosquebradas",
        "phone_number": "3104991221"
    },
    {
        "name": "Hayder Andrés",
        "age": 19,
        "address": "Sabrá Dios",
        "phone_number": "3205991223"
    },
    {
        "name": "Andrés Lopez",
        "age": 15,
        "address": "Parque Industrial",
        "phone_number": "3305951723"
    },
    {
        "name": "Sebastián Figueroa",
        "age": 20,
        "address": "Circunvalar",
        "phone_number": "3940600222"
    },
    {
        "name": "Carlos David",
        "age": 25,
        "address": "El Tigre Ave",
        "phone_number": "3102245675"
    }
]

password = input("Ingrese su contraseña: ")

while len(password)>4:
    if password == "3101721" :
        print(Datos_personas[0])
        break
    elif password == "3201923":
        print(Datos_personas[1])
        break
    elif password == "3301523":
        print(Datos_personas[2])
        break
    elif password == "3942022":
        print(Datos_personas[3])
        break
    elif password == "3102575":
        print(Datos_personas[4])
        break


