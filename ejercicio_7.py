cantidad=float(input("Ingerese la cantidad a invertir: $"))
interes=float(input("Ingrese el interes anual: "))
años=int(input("Ingrese la cantidad de años: "))
ganancia=(cantidad/100)*interes
gananciatotal=ganancia*años

print("El capital obtenido es de: $",gananciatotal)