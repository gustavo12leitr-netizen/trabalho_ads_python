# Exercício: Soma das notas de todos os alunos de uma turma de tamanho qualquer
soma_total = 0

# Pergunta o tamanho da turma
total_alunos = int(input("Qual a quantidade de alunos na turma? "))

for i in range(total_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    # Aqui somamos todas as notas, sem filtros
    soma_total += nota

print(f"\nA soma de todas as notas da turma é: {soma_total:.2f}")
