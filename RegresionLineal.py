import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x_train = np.array([1, 2, 3, 4, 5], dtype=float)
y_train = np.array([2, 4, 6, 8, 10], dtype=float)  


model = Sequential()
model.add(Dense(units=1, input_shape=[1]))  


model.compile(optimizer='sgd', loss='mean_squared_error')


history = model.fit(x_train, y_train, epochs=200, verbose=0)


x_test = np.array([6, 7, 8], dtype=float)
y_pred = model.predict(x_test)
print("Predicciones:", y_pred.flatten())


plt.scatter(x_train, y_train, color='blue', label='Datos de entrenamiento')
plt.plot(x_test, y_pred, color='red', label='Predicción del modelo')
plt.title('Regresión lineal con red neuronal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()