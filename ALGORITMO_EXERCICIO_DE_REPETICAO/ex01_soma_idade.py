# Exercício: Soma das idades de uma turma de 30 alunos
soma_idades = 0
total_alunos = 30

for i in range(total_alunos):
    # O loop vai rodar 30 vezes pedindo cada idade
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    soma_idades += idade

print(f"\nA soma total das idades da turma é: {soma_idades}")
