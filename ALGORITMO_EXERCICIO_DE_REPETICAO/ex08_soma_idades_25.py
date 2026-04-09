# Exercício 8: Soma das idades dos alunos com mais de 25 anos
soma_idades = 0

total = int(input("Digite a quantidade de alunos na turma: "))

for i in range(total):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    
    # Condição: apenas alunos com MAIS de 25 anos (idade > 25)
    if idade > 25:
        soma_idades += idade

print(f"\nA soma das idades dos alunos com mais de 25 anos é: {soma_idades}")
