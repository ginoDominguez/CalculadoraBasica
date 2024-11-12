###Creacion de entorno virtual:
# en terminal: python -m venv venv
# luego activar entorno:
# venv\Scripts\activate

### Definir calculadora:
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        return "No se puede dividir para cero"
    else:
        return a/b

if __name__ == "__main__":
    print("Seleccione la operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    seleccion = input("Elegir la opción deseada: ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if seleccion == '1':
        print(f"El resultado de la suma es: {suma(num1, num2)}")
    elif seleccion == '2':
        print(f"El resultado de la resta es: {resta(num1, num2)}")
    elif seleccion == '3':
        print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
    elif seleccion == '4':
        print(f"El resultado de la división es: {dividir(num1, num2)}")
    else:
        print("Invalid input")

