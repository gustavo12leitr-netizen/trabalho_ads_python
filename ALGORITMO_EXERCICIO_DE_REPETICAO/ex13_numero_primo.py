# Exercício 13: Verificador de Número Primo
numero = int(input("Digite um número inteiro: "))

divisores = 0

# O loop vai testar a divisão do número por todos os valores de 1 até ele mesmo
if numero > 1:
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    
    if divisores == 2:
        print(f"O número {numero} é PRIMO.")
    else:
        print(f"O número {numero} não é primo (ele possui {divisores} divisores).")
else:
    print(f"O número {numero} não é primo.")
