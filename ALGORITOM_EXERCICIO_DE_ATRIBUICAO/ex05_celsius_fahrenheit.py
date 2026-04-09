# Exercício 5: Converter Celsius para Fahrenheit
# Dado: F = 32 + (1.8 * C)

celsius = float(input("Digite a temperatura em graus Celsius: "))

# Aplicando a fórmula fornecida
fahrenheit = 32 + (1.8 * celsius)

print(f"\nA temperatura de {celsius:.1f}°C equivale a {fahrenheit:.1f}°F")
