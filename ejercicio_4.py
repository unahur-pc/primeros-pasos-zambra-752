print("Ingrese los valores para hallar el perimetro y el area de un rectangulo")
perimetro=int(input("Ingrese el valor de la base: "))
area=int(input("Ingrese el valor de la altura: "))
peri=perimetro*2 + area*2
are=perimetro*area
print("el preimetro es: ",peri)
print("El area es: ",are)

print("Ingrese los valores para hallar el perimetro y el area de un circulo")
print("ingrese el valor de el radio del circulo: ")
radio= float(input("radio de el circulo: "))
pi=3.14
area=pi*(radio**2)
perime=2*radio*pi
print("El area de el circulo es: ", area)
print("El perimetro es: ", perime)