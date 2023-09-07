# Calcular la suma de 10 números, utilizando la misma variable para leer los números
# desde la terminal.

vueltas=1 # variable que controla el bucle.
suma=0
print("Se van a sumar los 10 números ")
while vueltas <=10 :
      num=int(input("Ingrese un número "))
      suma=suma+num
      vueltas=vueltas+1  # actualiza
print(f"la suma de los 10 números es: {suma}")
