## Métricas de Avaliação de Modelos de Classificação

### Entendendo os termos:

Primeiro, precisamos entender o que significam as siglas que aparecem nas fórmulas:

*   **VP (Verdadeiro Positivo):** O modelo previu corretamente que algo é positivo (ex: o paciente tem a doença) e isso era verdadeiro.
*   **VN (Verdadeiro Negativo):** O modelo previu corretamente que algo é negativo (ex: o paciente não tem a doença) e isso era verdadeiro.
*   **FP (Falso Positivo):** O modelo previu incorretamente que algo é positivo (ex: o modelo disse que o paciente tem a doença), mas na realidade era negativo (o paciente não tem a doença). Também conhecido como "Erro Tipo I".
*   **FN (Falso Negativo):** O modelo previu incorretamente que algo é negativo (ex: o modelo disse que o paciente não tem a doença), mas na realidade era positivo (o paciente tem a doença). Também conhecido como "Erro Tipo II".
*   **N:** Número total de amostras (N = VP + VN + FP + FN).
*   **P:** Precisão
*   **S:** Sensibilidade (também chamada de Recall ou Revocação)

### As fórmulas:

#### Sensibilidade (Recall ou Revocação):

*   **Fórmula:** VP / (VP + FN)
*   **O que mede:** A capacidade do modelo de identificar corretamente todos os casos positivos. Em outras palavras, de todas as instâncias que *realmente* são positivas, qual proporção o modelo conseguiu classificar corretamente como positivas.
*   **Exemplo:** Em um teste para detectar uma doença, a sensibilidade mede a proporção de pessoas *doentes* que foram corretamente identificadas pelo teste. Uma alta sensibilidade significa que o teste é bom em detectar a doença, minimizando falsos negativos (pessoas doentes que o teste diz que não estão).

#### Especificidade:

*   **Fórmula:** VN / (FP + VN)
*   **O que mede:** A capacidade do modelo de identificar corretamente todos os casos negativos. De todas as instâncias que *realmente* são negativas, qual proporção o modelo classificou corretamente como negativas.
*   **Exemplo:** No mesmo teste de doença, a especificidade mede a proporção de pessoas *saudáveis* que foram corretamente identificadas pelo teste como não tendo a doença. Uma alta especificidade significa que o teste é bom em identificar pessoas saudáveis, minimizando falsos positivos (pessoas saudáveis que o teste diz que estão doentes).

#### Acurácia:

*   **Fórmula:** (VP + VN) / N
*   **O que mede:** A proporção de classificações corretas (tanto positivas quanto negativas) em relação ao total de amostras.
*   **Exemplo:** A acurácia geral do modelo. No entanto, a acurácia pode ser enganosa em conjuntos de dados desbalanceados (onde há muito mais exemplos de uma classe do que da outra). Por exemplo, se 95% das amostras são negativas, um modelo que sempre prevê negativo terá uma acurácia de 95%, mesmo que seja inútil para identificar casos positivos.

#### Precisão:

*   **Fórmula:** VP / (VP + FP)
*   **O que mede:** De todas as instâncias que o modelo classificou como positivas, qual proporção *realmente* era positiva.
*   **Exemplo:** No teste de doença, a precisão mede a proporção de pessoas que o teste identificou como doentes que *realmente* estão doentes. Uma alta precisão significa que, quando o teste diz que alguém está doente, é mais provável que esteja correto.

#### F-score (ou F1-score):

*   **Fórmula:** 2 x (Precisão x Sensibilidade) / (Precisão + Sensibilidade) ou 2VP / (2VP + FP + FN)
*   **O que mede:** A média harmônica entre a precisão e a sensibilidade. É uma métrica útil quando você precisa equilibrar a precisão e a sensibilidade, especialmente em conjuntos de dados desbalanceados. O F-score varia de 0 a 1, sendo 1 o melhor valor.
*   **Por que média harmônica?** A média aritmética pode ser influenciada por valores extremos. A média harmônica penaliza valores baixos em qualquer uma das métricas (precisão ou sensibilidade), o que a torna mais adequada para avaliar o equilíbrio entre elas.

### Em resumo:

*   **Sensibilidade:** Quão bem o modelo encontra todos os positivos reais.
*   **Especificidade:** Quão bem o modelo encontra todos os negativos reais.
*   **Acurácia:** Quão bem o modelo classifica no geral.
*   **Precisão:** Das previsões positivas, quantas estavam corretas.
*   **F-score:** Um equilíbrio entre precisão e sensibilidade.

É importante escolher as métricas apropriadas dependendo do problema em questão. Por exemplo, em um diagnóstico de uma doença grave, a sensibilidade é crucial (é melhor ter alguns falsos positivos do que perder um caso real da doença - falso negativo). Em um filtro de spam, a precisão pode ser mais importante (é melhor deixar passar alguns spams do que classificar um e-mail importante como spam - falso positivo). O F-score é útil quando você precisa equilibrar ambas.

# Matriz de Confusão

A matriz de confusão é uma ferramenta útil para avaliar o desempenho de um modelo de classificação. Ela permite visualizar a performance do modelo em termos de classes previstas versus classes reais.

## Estrutura da Matriz de Confusão

Uma matriz de confusão é uma tabela com quatro combinações de valores para um problema de classificação binária:
```sh
Predicted
               | Positive | Negative |
Actual Positive|    TP    |    FN    |
Negative       |    FP    |    TN    |
```

- **TP (True Positive)**: O modelo previu positivo e a classe real é positiva.
- **TN (True Negative)**: O modelo previu negativo e a classe real é negativa.
- **FP (False Positive)**: O modelo previu positivo, mas a classe real é negativa.
- **FN (False Negative)**: O modelo previu negativo, mas a classe real é positiva.

## Exemplo

Vamos usar um exemplo para entender melhor. Suponha que você tem um conjunto de dados de teste com 10 amostras e um modelo que faz previsões sobre se uma pessoa tem uma doença (Positivo) ou não (Negativo):

| Real     | Previsto |
|----------|----------|
| Positivo | Positivo |
| Negativo | Negativo |
| Positivo | Negativo |
| Negativo | Negativo |
| Negativo | Positivo |
| Positivo | Positivo |
| Positivo | Positivo |
| Negativo | Negativo |
| Negativo | Negativo |
| Positivo | Negativo |

A matriz de confusão será:
```sh
Predicted
               | Positive | Negative |
Actual Positive|     3    |     2    |
Negative       |     1    |     4    |
```
## Interpretação

- **True Positives (TP)**: 3
- **True Negatives (TN)**: 4
- **False Positives (FP)**: 1
- **False Negatives (FN)**: 2

## Métricas Derivadas

Com base nos valores da matriz de confusão, você pode calcular várias métricas de desempenho do modelo:

1. **Acurácia (Accuracy)**: A proporção de previsões corretas (TP + TN) em relação ao total de casos.
   \[
   \text{Acurácia} = \frac{TP + TN}{TP + TN + FP + FN}
   \]

2. **Precisão (Precision)**: A proporção de verdadeiros positivos em relação ao total de positivos previstos.
   \[
   \text{Precisão} = \frac{TP}{TP + FP}
   \]

3. **Recall (Sensibilidade ou TPR - True Positive Rate)**: A proporção de verdadeiros positivos em relação ao total de positivos reais.
   \[
   \text{Recall} = \frac{TP}{TP + FN}
   \]

4. **F1-Score**: A média harmônica da precisão e do recall.
   \[
   \text{F1-Score} = 2 \times \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}
   \]

## Exemplos de Cálculo

Para os valores da matriz de confusão do exemplo acima:

- **Acurácia**:
  \[
  \text{Acurácia} = \frac{3 + 4}{3 + 4 + 1 + 2} = \frac{7}{10} = 0.7
  \]

- **Precisão**:
  \[
  \text{Precisão} = \frac{3}{3 + 1} = \frac{3}{4} = 0.75
  \]

- **Recall**:
  \[
  \text{Recall} = \frac{3}{3 + 2} = \frac{3}{5} = 0.6
  \]

- **F1-Score**:
  \[
  \text{F1-Score} = 2 \times \frac{0.75 \times 0.6}{0.75 + 0.6} \approx 0.6667
  \]

## Na prática 
A matriz de confusão é uma ferramenta poderosa para avaliar o desempenho de modelos de classificação, e suas aplicações no mundo real são vastas. Ela ajuda a entender onde o modelo acerta e, crucialmente, onde ele erra, permitindo identificar áreas de melhoria e tomar decisões mais informadas. Vamos ver um exemplo concreto e as "dores" que ela ajuda a resolver:

**Exemplo: Diagnóstico Médico de uma Doença (ex: Diabetes)**

Imagine um sistema de aprendizado de máquina desenvolvido para diagnosticar diabetes a partir de exames de sangue. O modelo classifica os pacientes em duas categorias: "Diabético" ou "Não Diabético".

Uma matriz de confusão para este cenário poderia ser:

```sh
Previsão do Modelo
                  | Diabético | Não Diabético |
Real    Diabético |     80    |      20       |
Não Diabético     |     10    |      90       |
```
**Interpretação:**

*   **Verdadeiros Positivos (TP = 80):** O modelo corretamente diagnosticou 80 pacientes como diabéticos.
*   **Falsos Positivos (FP = 10):** O modelo incorretamente diagnosticou 10 pacientes saudáveis como diabéticos.
*   **Falsos Negativos (FN = 20):** O modelo incorretamente diagnosticou 20 pacientes diabéticos como não diabéticos.
*   **Verdadeiros Negativos (TN = 90):** O modelo corretamente diagnosticou 90 pacientes como não diabéticos.

**"Dores" que a Matriz de Confusão ajuda a resolver no dia a dia (neste contexto médico):**

*   **Identificar a taxa de erros graves:** No contexto médico, um Falso Negativo (FN) é geralmente mais grave do que um Falso Positivo (FP). Deixar de diagnosticar um paciente diabético (FN) pode levar a sérias complicações de saúde por falta de tratamento. A matriz de confusão quantifica esses erros, permitindo priorizar a redução de FNs. Neste exemplo, temos 20 FNs, o que indica um problema sério que precisa ser investigado.
*   **Avaliar a precisão do teste:** A matriz de confusão permite calcular métricas como Precisão (de todas as previsões "Diabético", quantas estavam corretas?), Recall (de todos os pacientes realmente diabéticos, quantos foram corretamente identificados?), Especificidade (de todos os pacientes não diabéticos, quantos foram corretamente identificados?) e Acurácia (taxa geral de acertos). Essas métricas fornecem uma visão mais completa do desempenho do modelo do que apenas a acurácia isoladamente.
*   **Comparar diferentes modelos:** Se você tiver dois modelos diferentes para diagnosticar diabetes, a matriz de confusão permite compará-los lado a lado e escolher o que apresenta o melhor equilíbrio entre Precisão e Recall, ou o que minimiza mais os Falsos Negativos, dependendo da prioridade.
*   **Ajustar o limiar de decisão:** Muitos modelos de classificação fornecem uma probabilidade de pertencimento a cada classe. Um limiar (geralmente 0.5) é usado para decidir a qual classe a amostra pertence. A matriz de confusão pode ajudar a ajustar esse limiar. Por exemplo, em um contexto médico, você pode querer diminuir o limiar para aumentar o Recall (detectar mais casos de diabetes), mesmo que isso aumente os Falsos Positivos (diagnosticar mais pessoas saudáveis como diabéticas, que precisarão de exames adicionais para confirmação).

**Outros exemplos de aplicação:**

*   **Detecção de spam em e-mails:** A matriz de confusão ajuda a entender quantos e-mails legítimos estão sendo marcados como spam (FP) e quantos spams estão passando pela filtragem (FN).
*   **Reconhecimento facial:** Avalia quantos rostos são incorretamente identificados (FP) e quantos rostos conhecidos não são reconhecidos (FN).
*   **Detecção de fraudes em transações bancárias:** Ajuda a identificar quantas transações legítimas são marcadas como fraudulentas (FP) e quantas transações fraudulentas não são detectadas (FN).
*   **Manutenção preditiva em indústrias:** Auxilia na identificação de falhas em equipamentos antes que elas ocorram, minimizando paradas na produção.

Em resumo, a matriz de confusão não apenas quantifica os erros de um modelo, mas também fornece *insights* valiosos sobre a natureza desses erros, permitindo tomar decisões estratégicas para melhorar o desempenho do modelo e minimizar os impactos negativos no mundo real. Ela nos ajuda a entender as nuances do desempenho de um modelo de classificação, indo além da simples taxa de acertos.

## Conclusão

A matriz de confusão é uma excelente ferramenta para entender onde o seu modelo está errando, permitindo identificar se ele está confundindo classes específicas e como melhorar a performance. É fundamental para avaliar a precisão, recall, e outras métricas de desempenho de modelos de classificação.
