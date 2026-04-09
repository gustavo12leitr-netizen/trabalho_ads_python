# Exercício: Média das idades de uma turma de 50 alunos
soma_idades = 0
total_alunos = 50

for i in range(total_alunos):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    soma_idades += idade

media = soma_idades / total_alunos

print(f"\nA média de idade da turma é: {media:.2f} anos")
