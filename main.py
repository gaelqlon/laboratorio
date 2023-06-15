from laboratorio import *
def main():
    print("De todo las eleciones elija 1 ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multipliacion")
    print("4. Division")
    print("5. Exponenciacion")
    print("6. Raices")
    print("7. Suma de 5 numeros")
    print("8. quetzal a dolar")
    print("9. dolar a quetzal")
    print("10.Dolar a Quetzal")
main()

opcion=int(input("Ingrese la opcion"))
if opcion==1:
    n1=float(input("ingrese el primer numero"))
    n2=float(input("ingrese el segundo numero"))
    print(suma(n1,n2))
if opcion==2:
    n1=float(input("ingrese el primer numero"))
    n2=float(input("ingrese el segundo numero"))
    print(resta(n1,n2))
if opcion==3:
    n1=float(input("ingrese el primer numero"))
    n2=float(input("ingrese el segundo numero"))
    print(multipliacion(n1,n2))
if opcion==4:
    n1=float(input("ingrese el primer numero"))
    n2=float(input("ingrese el segundo numero"))
    print(division(n1,n2))
if opcion==5:
    n1=float(input("ingrese el numero que desea sacar la exponenciacion"))
    n2=float(input("ingrese el numero por el que se va a exponenciar"))
    print(exponenciacion(n1,n2))
if opcion==6:
    n1=float(input("ingrese el numero que desea sacar la raiz"))
    n2=float(input("ingrese el numero por el que se va a dividir "))
    print(raiz(n1,n2))
if opcion==7:
    n1=float(input("ingrese el primer numero"))
    n2=float(input("ingrese el segundo numero"))
    n3=float(input("ingrese el tercer numero"))
    n4=float(input("ingrese el cuarto numero "))
    n5=float(input("ingrese el quinto numero "))
    print(suma_5numeros(n1,n2,n3,n4,n5))
if opcion==8:
    n1=float(input("ingrese el primer numero "))
    n2=float(input("ingrese el segundo numero "))
    print(residuo(n1,n2))
if opcion==9:
    n=float(input("ingrese el primer numero "))
    print(quetzal_a_dolar(n))
if opcion==10:
    n=float(input("ingrese el primer numero "))
    print(dolar_a_quetzal(n))
    

    
    
   
