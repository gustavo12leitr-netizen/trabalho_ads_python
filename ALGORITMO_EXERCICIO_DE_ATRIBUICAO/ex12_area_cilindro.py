# Exercício 12: Cálculo da Área Total de um Cilindro
# Fórmulas fornecidas:
# Area Base = 3.14 * R²
# Area Lateral = 2 * 3.14 * R * Altura
# Area Total = (2 * Area Base) + Area Lateral

raio = float(input("Digite o valor do raio do cilindro: "))
altura = float(input("Digite o valor da altura do cilindro: "))
pi = 3.14

# 1. Calculando a área da base
area_base = pi * (raio ** 2)

# 2. Calculando a área lateral
area_lateral = 2 * pi * raio * altura

# 3. Calculando a área total
area_total = (2 * area_base) + area_lateral

print(f"\n--- Resultados ---")
print(f"Área da Base (uma): {area_base:.2f}")
print(f"Área Lateral: {area_lateral:.2f}")
print(f"Área Total do Cilindro: {area_total:.2f}")
