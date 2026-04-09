# Exercício 4: Verificador de Par ou Ímpar
numero = int(input("Digite um número inteiro: "))

# O operador % pega o resto da divisão por 2. Se for 0, o número é par.
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
