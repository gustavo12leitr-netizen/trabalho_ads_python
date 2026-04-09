# Exercício 11: Média de notas entre 5.0 e 7.0 (Turma qualquer)
soma_notas = 0
contador = 0

total = int(input("Informe a quantidade de alunos: "))

for i in range(total):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    # Verifica se a nota é maior que 5.0 E menor que 7.0
    if nota > 5.0 and nota < 7.0:
        soma_notas += nota
        contador += 1

if contador > 0:
    media = soma_notas / contador
    print(f"\nA média das notas entre 5.0 e 7.0 é: {media:.2f}")
else:
    print("\nNenhuma nota encontrada no intervalo de 5.0 a 7.0.")
