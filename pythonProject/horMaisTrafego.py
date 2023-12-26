import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

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

DATASET3 = dataset_chromecast[dataset_chromecast['hour'] == 22][['upLog']]
DATASET4 = dataset_chromecast[dataset_chromecast['hour'] == 23][['downLog']]

#Histogramas

n_1 = DATASET1.size
binsNumber_1 = int(math.ceil(1 + math.log(n_1, 10) * 3.322))
_, bins_1 = np.histogram(DATASET1, bins=binsNumber_1)
plt.figure()
plt.hist(DATASET1, bins_1)
plt.title("Histograma - Dataset 1")

n_2 = DATASET2.size
binsNumber_2 = int(math.ceil(1 + math.log(n_2, 10) * 3.322))
_, bins_2 = np.histogram(DATASET2, bins=binsNumber_2)
plt.figure()
plt.hist(DATASET2, bins_2)
plt.title("Histograma - Dataset 2")

n_3 = DATASET3.size
binsNumber_3 = int(math.ceil(1 + math.log(n_3, 10) * 3.322))
_, bins_3 = np.histogram(DATASET3, bins=binsNumber_3)
plt.figure()
plt.hist(DATASET3, bins_3)
plt.title("Histograma - Dataset 3")

n_4 = DATASET4.size
binsNumber_4 = int(math.ceil(1 + math.log(n_4, 10) * 3.322))
_, bins_4 = np.histogram(DATASET4, bins=binsNumber_4)
plt.figure()
plt.hist(DATASET4, bins_4)
plt.title("Histograma - Dataset 4")

print(n_1, n_2, n_3, n_4)

data1_sorted = np.sort(DATASET1)
data2_sorted = np.sort(DATASET3)

quantis_teoricos = stats.norm.ppf(np.linspace(0.01, 0.99, 100))

plt.scatter(quantis_teoricos, data1_sorted, label='DATASET1')
plt.scatter(quantis_teoricos, data2_sorted, label='DATASET3')

plt.plot(quantis_teoricos, quantis_teoricos, color='red', linestyle='--', label='Diagonal de referência')

plt.title('Q-Q Plot')
plt.xlabel('Quantis teóricos')
plt.ylabel('Quantis dos dados')
plt.legend()

plt.show()
