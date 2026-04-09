# Exercício 4: Converter horas e minutos para o total em minutos
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

# Cálculo: multiplica as horas por 60 e soma os minutos restantes
total_minutos = (horas * 60) + minutos

print(f"\nO valor total convertido é de {total_minutos} minutos.")
