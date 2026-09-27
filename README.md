# Pesquisa de Satisfação de Atendimento - TudoWeb

Este projeto consiste em um script desenvolvido em Python para coletar opiniões de clientes sobre o grau de satisfação no atendimento prestado pela empresa.

---

## 🎯 Objetivo

O objetivo principal é automatizar o processo de coleta e contagem de avaliações de atendimento aos clientes, registrando o perfil básico do participante (nome e idade) e sua respectiva classificação de satisfação. 

Ao término da coleta de dados, o programa exibe um relatório com o resumo estatístico contendo:
- Quantidade total de avaliações **EXCELENTE** (Opção 1);
- Quantidade total de avaliações **RUIM** (Opção 3);
- Contagem informativa de avaliações **BOM** (Opção 2).

---

## 🛠️ Metodologia e Tecnologias

O programa foi desenvolvido em **Python 3** utilizando conceitos fundamentais de lógica de programação:

- **Estruturas de Repetição (`for` e `while`):** 
  - Um laço `for` itera sobre o total de entrevistados definidos na constante de controle (`TOTAL_ENTREVISTADOS`)[cite: 1].
  - Laços `while` são empregados para garantir a validação de entrada, impedindo que dados incorretos interrompam a execução do programa (ex: tratamento com `try/except` para idades não numéricas ou menores/iguais a zero)
- **Estruturas de Decisão (`if/elif/else`):** 
  - Avaliação da opção escolhida pelo usuário (1, 2 ou 3) para incrementar os respectivos contadores (`qtd_excelente`, `qtd_bom`, `qtd_ruim`).
- **Parâmetros e Testes:**
  - O enunciado prevê a aplicação para 50 entrevistados, com uma amostragem de teste configurada para 10 entrevistados (`TOTAL_ENTREVISTADOS = 10`) com o intuito de validação funcional do algoritmo
