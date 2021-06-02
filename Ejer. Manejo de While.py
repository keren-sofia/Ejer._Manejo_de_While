'''
Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo. 
Sugerencia: La sintaxis valor in lista permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)
Instrucciones
Para la solución de este problema, se requiere que el usuario escriba un script y utilice la estructura While.
Se debe tener como prueba una lista llamada numero=[1,2,3] Con números enteros del 0 al 9. 
Se debe solicitar al usuario ingresar el número que quiera comprobar. 
Ejemplo, si la lista de números tiene la siguiente estructura: numero=[1,3,5,9] y se ingresa por consola el numero 8, 
debe salir un mensaje que diga que él numero 8 no se encuentra en la lista. Si el número que se coloca está en la lista, 
sale un mensaje que indique, el numero x esta en la lista
'''
num = int(input("Ingrese un número entero del 0 al 9: "))
numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while num not in list(numero):
    num = int(input("Ingrese un número entero del 0 al 9: "))
else:
    print("El numero", num, "está en la lista.")