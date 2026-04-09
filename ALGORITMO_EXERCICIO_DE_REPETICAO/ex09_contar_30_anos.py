# Exercício 9: Contar quantos alunos têm 30 anos (Turma qualquer)
contador_30 = 0

# Primeiro, definimos o tamanho da turma
total_alunos = int(input("Quantos alunos existem na turma? "))

for i in range(total_alunos):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    
    # Se a idade for exatamente 30, aumentamos o contador
    if idade == 30:
        contador_30 += 1

print(f"\nTotal de alunos com 30 anos encontrados: {contador_30}")
