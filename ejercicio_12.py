num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el sugundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
if num1>num2:
    if num1>num3:
        print ("El mayor número es ",num1)
    else:
          print("El mayor número es ",num3)
else:
    if num2>num3:
            print("El mayor número es ",num2)
    else:
         print ("El mayor número es ",num3)