import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

dataset_chromecast = pd.read_csv('dataset_chromecast.csv')
dataset_chromecast['downLog'] = dataset_chromecast['bytes_down'].apply(lambda x: np.log10(x) if x != 0 else 0)
dataset_chromecast['upLog'] = dataset_chromecast['bytes_up'].apply(lambda x: np.log10(x) if x != 0 else 0)
dataset_chromecast['hour'] = dataset_chromecast["date_hour"].apply(lambda x: int(x.split(" ")[1].split(":")[0]))

dataset_smartTv = pd.read_csv('dataset_smart-tv.csv')
dataset_smartTv['downLog'] = dataset_smartTv['bytes_down'].apply(lambda x: np.log10(x) if x != 0 else 0)
dataset_smartTv['upLog'] = dataset_smartTv['bytes_up'].apply(lambda x: np.log10(x) if x != 0 else 0)
dataset_smartTv['hour'] = dataset_smartTv["date_hour"].apply(lambda x: int(x.split(" ")[1].split(":")[0]))

DATASET1 = dataset_smartTv[dataset_smartTv['hour'] == 20][['upLog']]
DATASET2 = dataset_smartTv[dataset_smartTv['hour'] == 20][['downLog']]

DATASET3 = dataset_chromecast[dataset_chromecast['hour'] == 23][['upLog']]
DATASET4 = dataset_chromecast[dataset_chromecast['hour'] == 23][['downLog']]

#Calculo do coeficiente de correlação amostral

correlation_coefficient, p_value = pearsonr(DATASET1['upLog'], DATASET2['downLog'])
print(f"Coeficiente de Correlação: {correlation_coefficient}")
print(f"P-value: {p_value}")

correlation_coefficient, p_value = pearsonr(DATASET3['upLog'], DATASET4['downLog'])
print(f"Coeficiente de Correlação: {correlation_coefficient}")
print(f"P-value: {p_value}")

#Gráfico ScatterPlot

DATA1_sorted = np.sort(DATASET1, axis=0)
DATA2_sorted = np.sort(DATASET2, axis=0)
DATA3_sorted = np.sort(DATASET3, axis=0)
DATA4_sorted = np.sort(DATASET4, axis=0)

plt.scatter(DATA1_sorted, DATA2_sorted)
plt.xlabel('upLog')
plt.ylabel('downLog')
plt.title('Scatterplot entre DATASET1 e DATASET2')
plt.show()

plt.scatter(DATA3_sorted, DATA4_sorted)
plt.xlabel('upLog')
plt.ylabel('downLog')
plt.title('Scatterplot entre DATASET3 e DATASET4')
plt.show()
