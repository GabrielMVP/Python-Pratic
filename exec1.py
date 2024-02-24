
numA = int(input("Escreva o valor da A: "))

numB = int(input("Escreva o valor da B: "))

numC = int(input("Escreva o valor da C: "))

soma = numA + numB

if  numA + numB < numC:
    print("A soma de A + B é menor que C:", soma, "<", numC)
else:
    print("A soma de A + B é maior ou igual a C:", soma, ">=", numC)

