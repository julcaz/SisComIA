from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

def cargar_datos():
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

def dividir_datos(X, y, test_size=0.2, random_state=42):
    
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def entrenar_knn(X_train, y_train, n_neighbors=3):
    
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    return knn

def evaluar_modelo(knn, X_test, y_test):
    
    y_pred = knn.predict(X_test)
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))
    print("\nReporte de clasificación:")
    print(classification_report(y_test, y_pred))

def validacion_cruzada(X, y, n_neighbors=3, cv=5):
    
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(knn, X, y, cv=cv)
    print(f"Accuracy promedio con validación cruzada ({cv} folds): {np.mean(scores):.4f}")

def main():
    X, y = cargar_datos()
    X_train, X_test, y_train, y_test = dividir_datos(X, y)
    knn = entrenar_knn(X_train, y_train)
    evaluar_modelo(knn, X_test, y_test)
    validacion_cruzada(X, y)

if __name__ == "__main__":
    main()
