### Exercício 1: Avaliação de Expressões e Tipos de Resultados

( I ) A + B + C       - Inteiro (soma de inteiros resulta em inteiro)
( R ) A + B + Z       - Real (qualquer operação com um número Real torna o resultado Real)
( L ) NOME + RUA      - Literal (concatenação de textos)
( N ) A B             - Não definido (falta um operador entre as variáveis)
( N ) A Y             - Não definido (falta um operador)
( N ) NOME RUA        - Não definido (falta um operador)
( B ) L1 .OU. L2      - Lógico (operação booleana resulta em verdadeiro/falso)
( B ) RUA <> NOME     - Lógico (uma comparação de diferença resulta em verdadeiro/falso)
( R ) A + B / C       - Real (a divisão `/` geralmente resulta em real, mesmo entre inteiros)
( R ) A + X / Z       - Real
( R ) A + Z / A       - Real
( N ) A B = L1        - Não definido (erro de sintaxe no lado esquerdo)
( B ) (A = B)         - Lógico (uma comparação de igualdade resulta em booleano)
( R ) X + Y / Z       - Real
( B ) X = Z / A       - Lógico (é uma comparação: o valor de X é igual ao resultado da divisão?)
( N ) L1 ** L2        - Não definido (não existe potência `**` entre tipos lógicos)
( N ) A + B / L2      - Não definido (não se divide números por um valor lógico)
( N ) X < L1 / RUA    - Não definido (operação matematicamente impossível entre esses tipos)

### Exercício 2: Avaliação de Expressões (Continuação)

**Valores base:** A=1, B=2, C=3, X=2.0, Y=10.0, Z=-1.0, L1=.V., L2=.F., NOME="PEDRO", RUA="PEDRINHO"

**Resultados das Avaliações:**

* **A + C / B** → **2.5**
* **A + B + C** → **6**
* **C / B / A** → **1.5**
* **-28 - X ** B** → **-32.0** (Cálculo: -28 - 4.0)
* **- (X ** B)** → **-4.0** (Cálculo: -(2.0²))
* **(-X) ** B** → **4.0** (Cálculo: (-2.0)², base negativa com expoente par fica positiva)
* **NOME + RUA** → **"PEDROPEDRINHO"** (Concatenação de textos)
* **NOME = RUA** → **.F.** (Falso, pois as strings são diferentes)
* **L1 .OU. L2** → **.V.** (Verdadeiro ou Falso resulta em Verdadeiro)
* **(L1 .E. (.NÃO. L2))** → **.V.** (V e V resulta em Verdadeiro)
* **(L2 .E. (.NÃO. L1))** → **.F.** (F e F resulta em Falso)
* **(L1 .E. (.NÃO. L2)) .OU. (L2 .E. (.NÃO. L1))** → **.V.** (V ou F resulta em Verdadeiro)
* **X Y .E. C = B** → **Erro/Inválido** (Faltam operadores entre X e Y, e entre as expressões relacionais e lógicas)
* **(C - 3 * A) (X + 2 * Z)** → **0.0** (Cálculo: (3 - 3) * (2 + (-2)) = 0 * 0. Omitir o sinal de '*' entre parênteses é aceito em algumas lógicas como multiplicação)
