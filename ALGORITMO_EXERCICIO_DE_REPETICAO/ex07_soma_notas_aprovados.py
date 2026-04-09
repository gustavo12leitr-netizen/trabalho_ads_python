# Exercício 7: Soma das notas >= 5.0 (Turma de tamanho qualquer)
soma_notas = 0

total_alunos = int(input("Quantos alunos tem na turma? "))

for i in range(total_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    # Condição: apenas notas maiores ou iguais a 5.0 entram na soma
    if nota >= 5.0:
        soma_notas += nota

print(f"\nA soma das notas dos alunos aprovados (>= 5.0) é: {soma_notas:.2f}")
