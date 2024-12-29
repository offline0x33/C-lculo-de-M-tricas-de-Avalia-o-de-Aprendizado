import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Passo 2: Criar um conjunto de dados fictício
X, y = make_classification(n_samples=1000, n_features=20, n_classes=10, n_clusters_per_class=1, n_informative=4, random_state=42)

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Passo 3: Treinar um modelo de classificação
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Passo 4: Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Passo 5: Gerar a matriz de confusão
cm = confusion_matrix(y_test, y_pred)

N = np.sum(cm)  # Número total de amostras

# Cálculo das métricas para cada classe
for i in range(cm.shape[0]):
    VP = cm[i, i]
    FN = np.sum(cm[i, :]) - VP
    FP = np.sum(cm[:, i]) - VP
    VN = N - VP - FN - FP

    if (VP + FN) == 0:
        sensibilidade = 0
    else:
        sensibilidade = VP / (VP + FN)

    if (VN + FP) == 0:
        especificidade = 0
    else:
        especificidade = VN / (VN + FP)

    if (VP + FP) == 0:
        precisao = 0
    else:
        precisao = VP / (VP + FP)

    if (precisao + sensibilidade) == 0:
        f_score = 0
    else:
        f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

    print(f"Classe {i}:")
    print(f"  Sensibilidade (Recall): {sensibilidade:.2f}")
    print(f"  Especificidade: {especificidade:.2f}")
    print(f"  Precisão: {precisao:.2f}")
    print(f"  F-score: {f_score:.2f}")

# Cálculo da Acurácia Global
VP_total = np.trace(cm)  # Soma dos Verdadeiros Positivos na diagonal principal
acuracia = VP_total / N

print(f"\nAcurácia Global: {acuracia:.2f}")

# Plotar a matriz de confusão
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title('Matriz de Confusão')
plt.show()