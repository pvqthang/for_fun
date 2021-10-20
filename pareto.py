import random
import numpy as np
from matplotlib import pyplot as plt

def normal_dist():
    N=1000 #number of players
    R=100 # range of income
    K=1000 # number of game
    L=np.zeros(N)
    r_ratio=49/100 #ratio of rich/total
    numb_of_poor=N-int(N*r_ratio)
    for j in range(K):
        for i in range(N):
            L[i] +=random.randint(0,R)
    L=np.sort(L)
    print("1st game mean = {}".format(np.mean(L)))
    print("1st game standard deviation = {}".format(np.std(L)))

    print("sum the rich={}".format(L[numb_of_poor:].sum()))
    print("sum the poor={}".format(L[:numb_of_poor].sum()))
    print("top 1 = {}".format(L[-1]))
    print("top 1000 = {}".format(L[0]))

    # a = np.hstack((rng.normal(size=1000),
    # rng.normal(loc=5, scale=2, size=1000)))
    # a= np.hstack(L)
    _ = plt.hist(L, bins='auto')  # arguments are passed to np.histogram
    plt.title("1st game wealth distribution ")
    plt.show()
    x = np.linspace(1, N, N)
    plt.plot(x, L)
    plt.plot(x, L, 'o')
    plt.show()


def pareto_dist():
    print("===============================")
    N=1000 #number of players
    R=1 # game reward range
    K=5000 # number of game
    C=100#initial capital
    L=np.full((N),C)
    for j in range(0,K):
        for i in range(int(N/2)):
            r=random.randint(-R,R) #random bet
            L[2*i] += r
            L[2*i+1] -= r
           

    L=np.sort(L)
    print("2nd game mean = {}".format(np.mean(L)))
    print("2nd game standard deviation = {}".format(np.std(L)))
    r_ratio=30/100 #ratio of rich/total
    numb_of_poor=N-int(N*r_ratio)
    print("numb_of_poor={}".format(numb_of_poor))
    print("sum of rich={}".format(L[numb_of_poor:].sum()))
    print("sum of the poor={}".format(L[:numb_of_poor].sum()))
    print("top 1 = {}".format(L[-1]))
    print("top 1000 = {}".format(L[0]))

    _ = plt.hist(L, bins='auto')  # arguments are passed to np.histogram
    plt.title("2nd game wealth distribution ")
    plt.show()
    x = np.linspace(1, N, N)
    plt.plot(x, L)
    plt.plot(x, L, 'o')
    plt.show()
    

def mix_dist():
    print("===============================")
    N=1000 #number of players
    R=100 # game reward range
    K=1000 # number of game
    L=np.zeros(N)
    for j in range(0,K):
        for i in range(int(N/2)):
            r=random.randint(-R,R) #random bet
            L[2*i] += r
            L[2*i]+=random.randint(0,R)
            L[2*i+1] -= r
            L[2*i+1] += random.randint(0,R)

    L=np.sort(L)
    print("3rd game mean = {}".format(np.mean(L)))
    print("3rd game standard deviation = {}".format(np.std(L)))
    r_ratio=8/100 #ratio of rich/total
    numb_of_poor=N-int(N*r_ratio)
    print("numb_of_poor={}".format(numb_of_poor))

    print("sum of the rich ={}".format(L[numb_of_poor:].sum()))
    print("sum of the poor ={}".format(L[:numb_of_poor-1].sum()))
    print("top 1 = {}".format(L[-1]))
    print("top 1000 = {}".format(L[0]))

    _ = plt.hist(L, bins='auto')  # arguments are passed to np.histogram
    plt.title("3rd game wealth distribution ")
    plt.show()
    x = np.linspace(1, N, N)
    plt.plot(x, L)
    plt.plot(x, L, 'o')
    plt.show()
    
if __name__ == '__main__':
    normal_dist()
    pareto_dist()
    mix_dist()
