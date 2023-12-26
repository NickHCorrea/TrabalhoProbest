import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dataset_chromecast = pd.read_csv('dataset_chromecast.csv')
down_cc = dataset_chromecast['bytes_down'].apply(lambda x: np.log10(x) if x != 0 else 0)
up_cc = dataset_chromecast['bytes_up'].apply(lambda x: np.log10(x) if x != 0 else 0)
n_cc = int(dataset_chromecast.size / 4)

dataset_smartTv = pd.read_csv('dataset_smart-tv.csv')
down_tv = dataset_smartTv['bytes_down'].apply(lambda x: np.log10(x) if x != 0 else 0)
up_tv = dataset_smartTv['bytes_up'].apply(lambda x: np.log10(x) if x != 0 else 0)
n_tv = int(dataset_smartTv.size / 4)


# Histograma
binsNumber_cc = int(math.ceil(1 + math.log(n_cc, 10) * 3.322))

_, downBins_cc = np.histogram(down_cc, bins=binsNumber_cc)
_, upBins_cc = np.histogram(up_cc, bins=binsNumber_cc)

plt.figure()
plt.hist(down_cc, downBins_cc)
plt.title("Histograma - Download (Chromecast)")

plt.figure()
plt.hist(up_cc, upBins_cc)
plt.title("Histograma - Upload (Chromecast)")

binsNumber_tv = int(math.ceil(1 + math.log(n_tv, 10) * 3.322))

_, downBins_tv = np.histogram(down_cc, bins=binsNumber_tv)
_, upBins_tv = np.histogram(up_cc, bins=binsNumber_tv)

plt.figure()
plt.hist(down_tv, downBins_tv)
plt.title("Histograma - Download (Smart TV)")

plt.figure()
plt.hist(up_tv, upBins_tv)
plt.title("Histograma - Upload (Smart TV)")

#Função Distribuição Empirica
res_down_cc = stats.ecdf(down_cc)
plt.figure()
ax = plt.subplot()
res_down_cc.cdf.plot(ax)
ax.set_xlabel('Download (Chromecast)')
ax.set_ylabel('Função Distribuição Empírica')

res_up_cc = stats.ecdf(up_cc)
plt.figure()
ax = plt.subplot()
res_up_cc.cdf.plot(ax)
ax.set_xlabel('Upload (Chromecast)')
ax.set_ylabel('Função Distribuição Empírica')

res_down_tv = stats.ecdf(down_tv)
plt.figure()
ax = plt.subplot()
res_down_tv.cdf.plot(ax)
ax.set_xlabel('Download (SmartTV)')
ax.set_ylabel('Função Distribuição Empírica')

res_up_tv = stats.ecdf(up_tv)
plt.figure()
ax = plt.subplot()
res_up_tv.cdf.plot(ax)
ax.set_xlabel('Upload (SmartTV)')
ax.set_ylabel('Função Distribuição Empírica')

#Média
down_mean_cc = down_cc.mean()
up_mean_cc = up_cc.mean()

down_mean_tv = down_tv.mean()
up_mean_tv = up_tv.mean()

#Variância
down_var_cc = down_cc.var()
up_var_cc = up_cc.var()

down_var_tv = down_tv.var()
up_var_tv = up_tv.var()

#Desvio Padrão
down_std_cc = down_cc.std()
up_std_cc = up_cc.std()

down_std_tv = down_tv.std()
up_std_tv = up_tv.std()

#Boxplot

fig, axs = plt.subplots(2, 2)

axs[0, 0].boxplot(down_cc)
axs[0, 0].set_title('Download (Chromecast)')

axs[0, 1].boxplot(up_cc)
axs[0, 1].set_title('Upload (Chromecast)')

axs[1, 0].boxplot(down_tv)
axs[1, 0].set_title('Download (SmartTV)')

axs[1, 1].boxplot(up_tv)
axs[1, 1].set_title('Upload (SmartTV)')

#Mostrar todos os resultados
print("Estatísticas")
print("Chromecast")
print("Download")
print("Média: ", down_mean_cc)
print("Variância: ", down_var_cc)
print("Desvio padrão: ", down_std_cc)
print("Upload")
print("Média: ", up_mean_cc)
print("Variância: ", up_var_cc)
print("Desvio padrão: ", up_std_cc)
print("Smart TV")
print("Download")
print("Média: ", down_mean_tv)
print("Variância: ", down_var_tv)
print("Desvio padrão: ", down_std_tv)
print("Upload")
print("Média: ", up_mean_tv)
print("Variância: ", up_var_tv)
print("Desvio padrão: ", up_std_tv)

plt.show()
