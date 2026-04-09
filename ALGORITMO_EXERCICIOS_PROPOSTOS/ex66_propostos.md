### Exercício 1: 

#### 1. Pseudocódigo
```portugol
ALGORITMO "MediaQuatroNumeros"
VAR
    n1, n2, n3, n4 : Inteiro
    media : Real
INICIO
    ESCREVA("Digite o primeiro número: ")
    LEIA(n1)
    ESCREVA("Digite o segundo número: ")
    LEIA(n2)
    ESCREVA("Digite o terceiro número: ")
    LEIA(n3)
    ESCREVA("Digite o quarto número: ")
    LEIA(n4)
    
    media <- (n1 + n2 + n3 + n4) / 4
    
    ESCREVA("A média aritmética é: ", media)
FIMALGORITMO

### Exercício 2: 

#### 1. Pseudocódigo
```portugol
ALGORITMO "ConversorCelsiusFahrenheit"
VAR
    C, F : Real
INICIO
    ESCREVA("Digite a temperatura em Celsius (C): ")
    LEIA(C)
    
    F <- (9 / 5) * C + 32
    
    ESCREVA("A temperatura em Fahrenheit é: ", F)
FIMALGORITMO

### Exercício 3: Conversão de Chuva (Polegadas para Milímetros)

```portugol
ALGORITMO "ConverteChuva"
VAR
    pol, mm : Real
INICIO
    ESCREVA("Quantidade de chuva em polegadas: ")
    LEIA(pol)
    mm <- pol * 25.4
    ESCREVA("Equivalente em milímetros: ", mm)
FIMALGORITMO

### Exercício 4:

ALGORITMO "QuadradoNumero"
VAR
    num, res : Real
INICIO
    ESCREVA("Digite um número: ")
    LEIA(num)
    res <- num * num
    ESCREVA("O quadrado é: ", res)
FIMALGORITMO

### Exercício 5:

ALGORITMO "CustoConsumidor"
VAR
    custoFabrica, custoFinal : Real
INICIO
    ESCREVA("Custo de fábrica: ")
    LEIA(custoFabrica)
    custoFinal <- custoFabrica + (custoFabrica * 0.12) + (custoFabrica * 0.45)
    ESCREVA("Custo final ao consumidor: ", custoFinal)
FIMALGORITMO

### Exercício 6:

ALGORITMO "ContaLanchonete"
VAR
    qH, qC, qF, qR, qM : Inteiro
    total : Real
INICIO
    ESCREVA("Quantos Hambúrgueres?") LEIA(qH)
    ESCREVA("Quantos Cheeseburgers?") LEIA(qC)
    ESCREVA("Quantas Fritas?") LEIA(qF)
    ESCREVA("Quantos Refrigerantes?") LEIA(qR)
    ESCREVA("Quantos Milkshakes?") LEIA(qM)
    
    total <- (qH * 3.00) + (qC * 2.50) + (qF * 2.50) + (qR * 1.00) + (qM * 3.00)
    
    ESCREVA("Total da conta: R$ ", total)
FIMALGORITMO

### Exercício 7

ALGORITMO "SalarioVendedor"
VAR
    nome : Literal
    numCarros : Inteiro
    valorVendas, salarioFinal : Real
INICIO
    ESCREVA("Nome do vendedor: ") LEIA(nome)
    ESCREVA("Carros vendidos: ") LEIA(numCarros)
    ESCREVA("Valor total das vendas: ") LEIA(valorVendas)
    
    salarioFinal <- 500 + (numCarros * 50) + (valorVendas * 0.05)
    
    ESCREVA("O vendedor ", nome, " receberá R$ ", salarioFinal)
FIMALGORITMO

### Exercício 8:

ALGORITMO "MediaMDS"
VAR
    nome : Literal
    nProva, nQuali, media : Real
INICIO
    ESCREVA("Nome do aluno: ") LEIA(nome)
    ESCREVA("Nota da prova: ") LEIA(nProva)
    ESCREVA("Nota qualitativa: ") LEIA(nQuali)
    
    media <- (nProva * 2 + nQuali * 1) / 3
    
    ESCREVA("A média de ", nome, " é: ", media)
FIMALGORITMO

