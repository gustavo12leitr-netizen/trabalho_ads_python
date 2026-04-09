# Exercício 12: Cálculo de Fatorial
numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

# Se o número for 0 ou 1, o fatorial é 1 por definição
if numero < 0:
    print("Não existe fatorial de número negativo.")
elif numero == 0 or numero == 1:
    print(f"O fatorial de {numero} é 1.")
else:
    # O loop começa no número e vai multiplicando até o 1
    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é {fatorial}")
