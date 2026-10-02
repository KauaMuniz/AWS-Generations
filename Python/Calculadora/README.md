# Calculadora em Python

Aplicação de terminal para realizar operações matemáticas básicas. O projeto
separa o menu da calculadora das funções responsáveis pelos cálculos, servindo
como exercício de modularização e entrada de dados em Python.

## Funcionalidades

- Adição;
- Subtração;
- Multiplicação;
- Divisão;
- Tratamento de divisão por zero;
- Menu interativo no terminal.

## Estrutura

```text
Calculadora/
├── Calculadora.py
├── operacoes.py
└── README.md
```

- `Calculadora.py`: executa o menu e recebe os valores digitados pelo usuário.
- `operacoes.py`: contém as funções de adição, subtração, multiplicação e divisão.

## Como executar

Abra o terminal na pasta `python/Calculadora` e execute:

```bash
python Calculadora.py
```

Também é possível executar a partir da raiz do repositório:

```bash
python python/Calculadora/Calculadora.py
```

Escolha uma operação, informe os dois valores e selecione se deseja voltar ao
menu ou encerrar o programa.

## Conceitos praticados

- Criação e importação de módulos;
- Funções e parâmetros;
- Estruturas de decisão;
- Laços de repetição;
- Tratamento de exceções;
- Entrada e saída de dados no terminal.
