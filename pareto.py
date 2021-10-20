import random
import numpy as np
from matplotlib import pyplot as plt

def normal_dist():
    N=100 #number of players
    R=100 # range of income
    K=1000 # number of game
    L=np.zeros(N)
    for j in range(0,K):
        for i in range(N):
            L[i] +=random.randint(0,R)
    L=np.sort(L)
    print("mean = {}".format(np.mean(L)))
    print("standard deviation = {}".format(np.std(L)))
    x = np.linspace(1, N, N)
    plt.plot(x, L)
    plt.plot(x, L, 'o')
    plt.show()


def pareto_dist():
    N=100 #number of players
    R=100 # game reward range
    K=1000 # number of game
    L=np.zeros(N)
    for j in range(0,int(K/2)):
        for i in range(N):
            for k in range(N-1):
                if (random.randint(0,1)):
                    r=random.randint(0,R) #random bet
                    L[i] += r
                    L[k] -= r
                else:
                    r=random.randint(0,R)
                    L[k] += r
                    L[i] -= r

    L=np.sort(L)
    print("mean = {}".format(np.mean(L)))
    print("standard deviation = {}".format(np.std(L)))
    x = np.linspace(1, N, N)
    plt.plot(x, L)
    plt.plot(x, L, 'o')
    plt.show()
    

def mix_dist():
    N=100 #number of players
    R=100 # game reward range
    K=1000 # number of game
    L=np.zeros(N)
    for j in range(0,int(K/2)):
        for i in range(N):
            for k in range(N-1):
                if (random.randint(0,1)):
                    r=random.randint(0,R) #random bet
                    L[i] += r +random.randint(0,R)
                    L[k] -= r +random.randint(0,R)
                else:
                    r=random.randint(0,R)
                    L[k] += r +random.randint(0,R)
                    L[i] -= r +random.randint(0,R)

    L=np.sort(L)
    print("mean = {}".format(np.mean(L)))
    print("standard deviation = {}".format(np.std(L)))
    x = np.linspace(1, N, N)
    plt.plot(x, L)
    plt.plot(x, L, 'o')
    plt.show()
    
if __name__ == '__main__':
    normal_dist()
    pareto_dist()
    mix_dist()