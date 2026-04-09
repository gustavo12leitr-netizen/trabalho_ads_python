# Exercício 3: Média de Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

# O :.2f faz com que o Python mostre apenas 2 casas após a vírgula
print(f"A média aritmética das notas é: {media:.2f}")
