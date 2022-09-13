import os

# Projeto de Calculadora

print("===================")
print("Calculadora.py")
print("===================")
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = int(input("Informe a operação que deseja realizar:"))
print("\n==================================================")
if op == 1:
    print("Operação escolhida: SOMA")
elif op == 2:
    print("Operação escolhida: SUBTRAÇÃO")
elif op == 3:
    print("Operação escolhida: MULTIPLICAÇÃO")
else:
    print("Operação escolhida: DIVISÃO")
print("==================================================")
print("\nInforme o 1º número:")
valor1 = int(input())
print("Informe o 2º número:")
valor2 = int(input())
if op == 1:
    print("Resultado:",valor1+valor2)
elif op == 2:
    print("Resultado:",valor1-valor2)
elif op == 3:
    print("Resultado:",valor1*valor2)
else:
    print("Resultado:",valor1/valor2)



