# Author : Medric Sonwa

from matplotlib import pyplot as plt

with open('result_file.txt', 'r') as result:
    result = result.read().split('\n')

ns = []
mins = []
maxs = []
means = []

for r in result:
    if r == '':
        continue
    n, min_v, max_v, mean_v = r.split(' ')
    ns.append(int(n))
    mins.append(float(min_v))
    maxs.append(float(max_v))
    means.append(float(mean_v))

fig, axes = plt.subplots(1, 3, figsize=(20, 5))


axes[0].plot(ns, mins, color='red')
axes[0].set_ylabel('Min perplexity')
axes[0].set_xlim(1)
axes[0].set_xlabel('Nb. tranches')

axes[1].plot(ns, maxs, color='blue')
axes[1].set_ylabel('Max perplexity')
axes[1].set_xlim(1)
axes[1].set_xlabel('Nb. tranches')

axes[2].plot(ns, means, color='green')
axes[2].set_ylabel('Mean perplexity')
axes[2].set_xlim(1)
axes[2].set_xlabel('Nb. tranches')

plt.show()

