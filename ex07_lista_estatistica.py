# Exercício 7: Estatísticas de uma Lista
n = int(input("Quantos números você deseja inserir na lista? "))

# Validação do Extra: N deve ser maior que 0
if n <= 0:
    print("Erro: A quantidade deve ser maior que zero.")
else:
    numeros = []
    
    for i in range(n):
        valor = float(input(f"Digite o {i+1}º número: "))
        numeros.append(valor) # Adiciona o número à lista

    print("\n--- Resultados ---")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
    print(f"Média dos valores: {sum(numeros) / len(numeros):.2f}")
