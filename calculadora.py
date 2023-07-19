num1 = float(input("informe o primeiro numero:\n"))
operador = input("informe o operador:\n")
num2 = float(input("informe o segundo numero:\n")) 
if(operador == "+"):
    calculadora = num1 + num2
    print("o resultado é da soma do número", num1, "e do número", num2 , calculadora) 
else:
    if(operador == "-"):
        calculadora = num1 - num2
        print("o resultado é da subtração do número", num1, "e do número", num2 , calculadora)     
    if(operador == "*"):
            calculadora = num1 * num2
            print("o resultado é da multiplicação do número", num1, "e do número", num2 , calculadora)
    if(operador == "/"):
                calculadora = num1 / num2
                print("o resultado é da divisão do número", num1, "e do número", num2 , calculadora)
