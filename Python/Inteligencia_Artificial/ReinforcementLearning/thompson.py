#%% Dataset
import numpy as np
import pandas as pd
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")
#%% Algoritmo
import random
N = 10000
d = 10
n_rewards_0 = [0 for i in range(d)]
n_rewards_1 = [0 for i in range(d)]
ads_selected = []
total_reward = 0
for n in range(0, N):
    max_random = 0
    ad = 0
    for i in range(0, d):
        random_beta = random.betavariate(n_rewards_1[i]+1, n_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        n_rewards_1[ad] +=1
    else:
        n_rewards_0[ad] += 1
    total_reward += reward
#%% visualizacion
import matplotlib.pyplot as plt
plt.hist(ads_selected)
plt.title("Historgama de anuncios")
plt.xlabel("ID del anuncio")
plt.ylabel("Frecuencia de visualizacion del anuncio")
plt.show()
# %%
