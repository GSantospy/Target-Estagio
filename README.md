# Target Sistemas - Teste técnico

Este repositório contém soluções para os problemas propostos. Abaixo estão os detalhes propostos e os resultados obtidos.

## 1. Soma Sequencial
### Enunciado
Observe o trecho de código abaixo:
```js
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável `SOMA`?

#### Resultado
O valor final da variável `SOMA` é `91`.<br>
[Código](https://github.com/GSantospy/Target-Estagio/blob/main/tecnica_1.py)


## 2. Sequência de Fibonacci
### Enunciado
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#### Resultado
```
Informe um número: 8
O número 8 pertence à sequência Fibonacci.
------------------
Informe um número: 9
O número 9 não pertence à sequência Fibonacci.
```
[Código](https://github.com/GSantospy/Target-Estagio/blob/main/tecnica_2.py)


## 3. Análise de Faturamento Diário
### Enunciado
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:<br>
• O menor valor de faturamento ocorrido em um dia do mês;<br>
• O maior valor de faturamento ocorrido em um dia do mês;<br>
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#### Resultado
```
Menor valor de faturamento: R$ 19848.53
Maior valor de faturamento: R$ 67836.43
Número de dias com faturamento acima da média: 2
```
[Código](https://github.com/GSantospy/Target-Estagio/blob/main/tecnica_3.py)



## 4. Percentual de Representação por Estado
### Enunciado
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:<br>
• SP – R$67.836,43<br>
• RJ – R$36.678,66<br>
• MG – R$29.229,88<br>
• ES – R$27.165,48<br>
• Outros – R$19.849,53<br>

Escreva um programa onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

#### Resultado
```
SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
OUTROS: 10.98%
```
[Código](https://github.com/GSantospy/Target-Estagio/blob/main/tecnica_4.py)



## 5. Inversão de String
### Enunciado
Escreva um programa que inverta os caracteres de um string.

#### Resultado
```
Digite algo: algo

String original: algo
String invertida: ogla
```
[Código](https://github.com/GSantospy/Target-Estagio/blob/main/tecnica_5.py)