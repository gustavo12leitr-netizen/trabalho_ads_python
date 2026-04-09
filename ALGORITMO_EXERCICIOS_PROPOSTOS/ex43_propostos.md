### Exercício 1: Identificadores (Variáveis)

( C ) valor          - Correto.
( C ) _b248          - Correto (começa com underline).
( I ) nota*do*aluno  - Incorreto (o asterisco `*` é um operador de multiplicação).
( C ) a1b2c3          - Correto.
( I ) 3 x 4          - Incorreto (começa com número e contém espaços).
( C ) Maria          - Correto.
( I ) km/h           - Incorreto (a barra `/` é um operador de divisão).
( C ) xyz            - Correto.
( I ) nome empresa   - Incorreto (contém espaço em branco).
( C ) sala_215       - Correto.
( I ) “nota”         - Incorreto (identificadores não usam aspas; aspas são para strings).
( I ) ah!            - Incorreto (o ponto de exclamação `!` é um caractere especial).

### Exercício 2: Declaração de Variáveis

Para armazenar os dados propostos, a declaração correta seria:

```portugol
VAR
    NB   : Real      (ou Inteiro, dependendo da precisão da nota)
    NA   : Literal   (ou String)
    NMAT : Inteiro   (ou Literal, caso contenha letras)
    SX   : Literal   (ou Caractere, para 'M'/'F')
