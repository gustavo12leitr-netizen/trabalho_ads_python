# Exercício 10: Média de idades entre 25 e 40 anos
soma_idades = 0
contador = 0

total = int(input("Quantidade de alunos na turma: "))

for i in range(total):
    idade = int(input(f"Idade do aluno {i+1}: "))
    
    # Verifica se está no intervalo: mais de 25 E menos de 40
    if idade > 25 and idade < 40:
        soma_idades += idade
        contador += 1

if contador > 0:
    media = soma_idades / contador
    print(f"\nA média das idades entre 25 e 40 anos é: {media:.2f}")
else:
    print("\nNenhum aluno atende aos critérios (25 < idade < 40).")
