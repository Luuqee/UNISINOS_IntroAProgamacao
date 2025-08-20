numero = int (input("Digite um número inteiro: "))
if numero < 0:
    print("ERRO: O número é deve ser positivo.")
elif numero == 0:
    print("ERRO: O número digitado é zero.")
elif numero % 2 == 0:
    print("O número" ,numero,"é par.")
else:
    print("O número", numero, "é ímpar.")