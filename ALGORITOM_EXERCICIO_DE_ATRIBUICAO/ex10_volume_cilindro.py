# Exercício 10: Cálculo do Volume de um Cilindro
# Fórmulas: Área da Base = 3.14 * R² | Volume = Área da Base * Altura

raio = float(input("Digite o valor do raio do cilindro: "))
altura = float(input("Digite o valor da altura do cilindro: "))

# Calculando primeiro a área da base
pi = 3.14
area_base = pi * (raio ** 2)

# Calculando o volume final
volume = area_base * altura

print(f"\nA área da base é: {area_base:.2f}")
print(f"O volume total do cilindro é: {volume:.2f}")
