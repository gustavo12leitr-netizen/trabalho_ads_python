# Exercício: Soma das notas >= 5.0 de uma turma de tamanho qualquer
soma_notas = 0

# Primeiro, perguntamos quantos alunos a turma tem
total_alunos = int(input("Quantos alunos tem na turma? "))

for i in range(total_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    # Só somamos se a nota for maior ou igual a 5.0
    if nota >= 5.0:
        soma_notas += nota

print(f"\nA soma das notas maiores ou iguais a 5.0 é: {soma_notas:.2f}")
