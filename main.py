import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

edades = np.array([
    18, 19, 19, 19, 19,
    19, 19, 19, 19, 19,
    19, 19, 19, 19, 19,
    19, 20, 20, 20, 20,
    20, 20, 20, 20, 20,
    20, 21, 21, 21, 21,
    21, 21, 22, 22, 23,
    24, 24, 25, 25, 25,
    25, 25, 26, 27, 28,
    30, 34
])

print("Edades de los estudiantes:")
print(edades)

print("\nTipo de variable: Cuantitativa discreta ya que representan valores numéricos que expresan una magnitud medible (el tiempo de vida en años).")

media = np.mean(edades)
mediana = np.median(edades)
varianza = np.var(edades)
desviacion_estandar = np.std(edades)
rango = np.max(edades) - np.min(edades)

moda = pd.Series(edades).mode()[0]

print("\n--- Medidas Estadísticas ---")
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion_estandar)
print("Rango:", rango)

print("\n--- Interpretación ---")

if abs(media - mediana) < 1:
    print("Si la media y la mediana presentan valores aproximadamente iguales, se infiere que la distribución es simétrica, sin influencia significativa de valores extremos.")
else:
    print("Si existe una diferencia considerable entre ambas, esto indica la presencia de asimetría (sesgo), ya sea positiva o negativa, generalmente causada por valores atípicos.")

print("La desviación estándar indica cuánto se dispersan las edades respecto a la media")

if rango > 10:
    print("El rango es alto → hay mucha diferencia entre edades")
else:
    print("El rango es bajo → edades bastante homogéneas")


Q1 = np.percentile(edades, 25)
Q2 = np.percentile(edades, 50)
Q3 = np.percentile(edades, 75)

print("\n--- Percentiles ---")
print("Q1 (25%):", Q1)
print("Q2 (50%):", Q2)
print("Q3 (75%):", Q3)

print("\nInterpretación:")
print("El 25% de los alumnos tiene edad menor o igual a Q1")
print("Q2 representa la mediana de las edades")
print("El 75% de los alumnos tiene edad menor o igual a Q3")


plt.hist(edades, bins=range(min(edades), max(edades)+2), edgecolor="black")
plt.title("Distribución de edades de estudiantes")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.xticks(range(min(edades), max(edades)+1))
plt.show()

print("\nLa mayor concentración de edades se observa en los intervalos con mayor frecuencia del histograma.")

print("\nEn resumen, la mayoría de los estudiantes tienen edades entre 19 y 25 años, con una media de aproximadamente 21 años. La distribución es relativamente simétrica, aunque hay algunos valores atípicos que podrían influir en la media. La desviación estándar indica que las edades están bastante dispersas alrededor de la media.")
