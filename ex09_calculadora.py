def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

while True:
    print("\n--- Calculadora ---")
    print("1. Somar | 2. Subtrair | 3. Multiplicar | 4. Dividir | 0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '0': break
    
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    if opcao == '1': print(f"Resultado: {somar(n1, n2)}")
    elif opcao == '2': print(f"Resultado: {subtrair(n1, n2)}")
    elif opcao == '3': print(f"Resultado: {multiplicar(n1, n2)}")
    elif opcao == '4': print(f"Resultado: {dividir(n1, n2)}")
    else: print("Opção inválida!")
