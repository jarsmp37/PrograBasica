def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    return nombre, edad

def mostrar_datos(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años.")