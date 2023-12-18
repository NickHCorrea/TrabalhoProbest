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

#Boxplot
fig, ax = plt.subplots(figsize=(12, 6))

boxplot = dataset_chromecast.boxplot(column='downLog', by='hour', ax=ax)

plt.xlabel('Hora do Dia')
plt.ylabel('Download (Chromecast)')

fig, ax = plt.subplots(figsize=(12, 6))

boxplot = dataset_chromecast.boxplot(column='upLog', by='hour', ax=ax)

plt.xlabel('Hora do Dia')
plt.ylabel('Upload (Chromecast)')

fig, ax = plt.subplots(figsize=(12, 6))

boxplot = dataset_smartTv.boxplot(column='downLog', by='hour', ax=ax)

plt.xlabel('Hora do Dia')
plt.ylabel('Download (Smart TV)')

fig, ax = plt.subplots(figsize=(12, 6))

boxplot = dataset_smartTv.boxplot(column='upLog', by='hour', ax=ax)

plt.xlabel('Hora do Dia')
plt.ylabel('Upload (Smart TV)')

#Média
down_mean_cc = dataset_chromecast.groupby('hour')['downLog'].mean()
up_mean_cc = dataset_chromecast.groupby('hour')['upLog'].mean()

down_mean_tv = dataset_smartTv.groupby('hour')['downLog'].mean()
up_mean_tv = dataset_smartTv.groupby('hour')['upLog'].mean()

#Variância
down_var_cc = dataset_chromecast.groupby('hour')['downLog'].var()
up_var_cc = dataset_chromecast.groupby('hour')['upLog'].var()

down_var_tv = dataset_smartTv.groupby('hour')['downLog'].var()
up_var_tv = dataset_smartTv.groupby('hour')['upLog'].var()

#Desvio Padrão
down_std_cc = dataset_chromecast.groupby('hour')['downLog'].std()
up_std_cc = dataset_chromecast.groupby('hour')['upLog'].std()

down_std_tv = dataset_smartTv.groupby('hour')['downLog'].std()
up_std_tv = dataset_smartTv.groupby('hour')['upLog'].std()

# Gráficos para Chromecast - Download
plt.figure(figsize=(12, 6))
plt.plot(dataset_chromecast.groupby('hour')['downLog'].mean(), label='Média - Chromecast Download')
plt.plot(dataset_chromecast.groupby('hour')['downLog'].var(), label='Variância - Chromecast Download')
plt.plot(dataset_chromecast.groupby('hour')['downLog'].std(), label='Desvio Padrão - Chromecast Download')
plt.title('Estatísticas para Chromecast - Download')
plt.xlabel('Hora do Dia')
plt.ylabel('Valores')
plt.legend()

# Gráficos para Chromecast - Upload
plt.figure(figsize=(12, 6))
plt.plot(dataset_chromecast.groupby('hour')['upLog'].mean(), label='Média - Chromecast Upload')
plt.plot(dataset_chromecast.groupby('hour')['upLog'].var(), label='Variância - Chromecast Upload')
plt.plot(dataset_chromecast.groupby('hour')['upLog'].std(), label='Desvio Padrão - Chromecast Upload')
plt.title('Estatísticas para Chromecast - Upload')
plt.xlabel('Hora do Dia')
plt.ylabel('Valores')
plt.legend()

# Gráficos para Smart TV - Download
plt.figure(figsize=(12, 6))
plt.plot(dataset_smartTv.groupby('hour')['downLog'].mean(), label='Média - Smart TV Download')
plt.plot(dataset_smartTv.groupby('hour')['downLog'].var(), label='Variância - Smart TV Download')
plt.plot(dataset_smartTv.groupby('hour')['downLog'].std(), label='Desvio Padrão - Smart TV Download')
plt.title('Estatísticas para Smart TV - Download')
plt.xlabel('Hora do Dia')
plt.ylabel('Valores')
plt.legend()

# Gráficos para Smart TV - Upload
plt.figure(figsize=(12, 6))
plt.plot(dataset_smartTv.groupby('hour')['upLog'].mean(), label='Média - Smart TV Upload')
plt.plot(dataset_smartTv.groupby('hour')['upLog'].var(), label='Variância - Smart TV Upload')
plt.plot(dataset_smartTv.groupby('hour')['upLog'].std(), label='Desvio Padrão - Smart TV Upload')
plt.title('Estatísticas para Smart TV - Upload')
plt.xlabel('Hora do Dia')
plt.ylabel('Valores')
plt.legend()

plt.show()
