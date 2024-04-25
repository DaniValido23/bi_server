import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {

}
df = pd.DataFrame(data)

# Análisis de ratings
plt.figure(figsize=(10, 6))
sns.barplot(x='business', y='rating', data=df)
plt.title('Rating promedio por plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Rating promedio')
plt.show()

# Análisis de reviews
plt.figure(figsize=(10, 6))
sns.barplot(x='business', y='num_reviews', data=df)
plt.title('Número de reviews por plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Número de reviews')
plt.show()

# Comparación entre plataformas
plt.figure(figsize=(10, 6))
sns.boxplot(x='business', y='rating', data=df)
plt.title('Distribución de ratings por plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Rating')
plt.show()
