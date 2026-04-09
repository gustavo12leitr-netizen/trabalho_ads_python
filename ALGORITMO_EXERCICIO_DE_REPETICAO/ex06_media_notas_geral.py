# Exercício 6: Média das notas de uma turma de tamanho qualquer
soma_total = 0

# Pergunta o tamanho da turma
total_alunos = int(input("Qual a quantidade de alunos na turma? "))

# Validação simples: evita erro se o usuário digitar 0
if total_alunos > 0:
    for i in range(total_alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        soma_total += nota

    media = soma_total / total_alunos
    print(f"\nA média das notas da turma é: {media:.2f}")
else:
    print("A quantidade de alunos deve ser maior que zero.")
