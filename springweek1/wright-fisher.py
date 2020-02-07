#!/usr/bin/env python3


# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# s = 0
N = 10000000
n1 = 0.5
def simulation(q,N, s, repetitions=1000):
    N= 2*int(N)
    n1 = np.ones(repetitions, dtype=np.uint64) * (q * N)
    # n1 = np.ones(repetitions, dtype=np.uint64) * (p* N)
    T = np.empty_like(n1)
    update = (n1 > 0) & (n1 < N)
    t = 0
    while update.any():
        t += 1
        p = n1 * (1 + s) / (N + n1 * s)
        n1[update] = np.random.binomial(N, p[update])
        T[update] = t
        update = (n1 > 0) & (n1 < N)
    return n1 == N, T
fixations, times = simulation(N=100, s=0, q= 0.5, repetitions=1000)
fixation_prob = fixations.mean()
fixation_time = times[fixations].mean()
w, h = plt.rcParams['figure.figsize']
fig, ax = plt.subplots(figsize=(2 * w, h))
sns.distplot(times[fixations], ax=ax)
ax.axvline(times[fixations].mean(), color='k', ls='--')
ax.set(xlabel='Fixation time', ylabel='Frequency')
sns.despine()
plt.show()

# # s = 0
# N = 100
# n1 = 0.5
# def simulation(q,N, s, repetitions=1000):
#     N= 2*int(N)
#     n1 = np.ones(repetitions, dtype=np.uint64) * (q * N)
#     # n1 = np.ones(repetitions, dtype=np.uint64) * (p* N)
#     T = np.empty_like(n1)
#     update = (n1 > 0) & (n1 < N)
#     t = 0
#     while update.any():
#         t += 1
#         p = n1 * (1 + s) / (N + n1 * s)
#         n1[update] = np.random.binomial(N, p[update])
#         T[update] = t
#         update = (n1 > 0) & (n1 < N)
#     return n1 == N, T
# fixations, times = simulation(N=100, s=0, q= 0.5, repetitions=1000)
# fixation_prob = fixations.mean()
# fixation_time = times[fixations].mean()
# w, h = plt.rcParams['figure.figsize']
# fig, ax = plt.subplots(figsize=(2 * w, h))
# sns.distplot(times[fixations], ax=ax)
# ax.axvline(times[fixations].mean(), color='k', ls='--')
# ax.set(xlabel='Fixation time', ylabel='Frequency')
# sns.despine()
# plt.show()




# # s = 0
# N = 1000
# n1 = 0.5
# def simulation(q,N, s, repetitions=1000):
#     N= 2*int(N)
#     n1 = np.ones(repetitions, dtype=np.uint64) * (q * N)
#     # n1 = np.ones(repetitions, dtype=np.uint64) * (p* N)
#     T = np.empty_like(n1)
#     update = (n1 > 0) & (n1 < N)
#     t = 0
#     while update.any():
#         t += 1
#         p = n1 * (1 + s) / (N + n1 * s)
#         n1[update] = np.random.binomial(N, p[update])
#         T[update] = t
#         update = (n1 > 0) & (n1 < N)
#     return n1 == N, T
# fixations, times = simulation(N=100, s=0, q= 0.5, repetitions=1000)
# fixation_prob = fixations.mean()
# fixation_time = times[fixations].mean()
# w, h = plt.rcParams['figure.figsize']
# fig, ax = plt.subplots(figsize=(2 * w, h))
# sns.distplot(times[fixations], ax=ax)
# ax.axvline(times[fixations].mean(), color='k', ls='--')
# ax.set(xlabel='Fixation time', ylabel='Frequency')
# sns.despine()
# plt.show()




# Input variables

# Number of trials
# trials = 1000
#
# # Number of independent experiments in each trial
# n = 100
#
# # Probability of success for each experiment
# p = 0.5
#
# # Function that runs our coin toss trials
# # heads is a list of the number of successes from each trial of n experiments
# def run_binom(trials, n, p):
#     alleles = []
#     for i in range(trials):
#         outcome = [np.random.random() for i in range(n)]
#         alleles.append(len([i for i in outcome if i>=0.50]))
#     return alleles
#
# # Run the function
# alleles = run_binom(trials, n, p)
#
# # Plot and save the results as a histogram
# fig, ax = plt.subplots(figsize=(14,7))
# ax = sns.distplot(alleles, bins=11, label='simulation results')
#
# ax.set_xlabel("Number of alleles",fontsize=16)
# ax.set_ylabel("Frequency",fontsize=16)
#
# # Plot the actual binomial distribution as a sanity check
# from scipy.stats import binom
# x = range(0,100)
# ax.plot(x, binom.pmf(x, n, p), 'ro', label='actual binomial distribution')
# ax.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
# plt.legend()
#
# # plt.savefig(fname='Binomial_Hist_2', dpi=150)
# plt.show()








# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# p = 0.5
# n = 100
# trials = 1000
#
#
# def run_binom(trials, n, p):
#     alleles = []
#     for i in range(trials):
#         outcome = [np.random.random() for i in range(n)]
#         alleles.append(len([i for i in outcome if i >= 0.5]))
#     return alleles
# # plot
# fig, ax = plt.subplots(figsize=(14,7))
# ax = sns.distplot(alleles, bins=11, label='simulation results')
#
# ax.set_xlabel("Number of alleles",fontsize=16)
# ax.set_ylabel("Frequency",fontsize=16)

# # Plot the actual binomial distribution as a sanity check
# from scipy.stats import binom
# x = range(0,11)
# ax.plot(x, binom.pmf(x, n, p), 'ro', label='actual binomial distribution')
# ax.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
# plt.legend()
#
# # plt.savefig(fname='Binomial_Hist_2', dpi=150)
# plt.show()
# pop = np.ones(N) + np.random.uniform (-0.5, 0.5 , N)
#
# for gen in range(generations):
#     fitnessprops = N/np.sum(N)
#     numoffspring = np.random.binomial(N,  fitnessprops)

    
# random sampling new individuals with fitnessprops (multinomial)
#     newpop = []
# for fitness,
# fig = plt.figure(5, figsize= (3,5))
# fig.clear()plt.subplot(2,1,1)
# plt.plot(mean_fitness,'-o')
# plt.ylabel('mean fitness')
# plt.subplot(2,1,2)
# plt.plot(std_fitness, '-o')
# plt.ylabel('std/dev.Fitness')
# plt.xlabel('geneartion')
# plt.tight_layout()
# plt.show()
#