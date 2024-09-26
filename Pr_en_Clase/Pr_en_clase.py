print("")
print("Alfaro Ibarra Sheccid 3w, calcular el combustible que gasta un automovil por kilometro")
#se define variable gasolina y se le pregunta al usuario
gasolina=float(input("Insertar los litros de gasolina:"))
#Se define viariable kilometro y se le pregunta al usuario
kilometro=float(input("insertar kilometros recorridos:"))
#se define una variable para tener la operacion de las dos anteriores
coste= gasolina/kilometro*100
#Se muestra el resultado en pantalla
print("el combustible consumido es:")
print(coste)
print("")