'''

'''

import numpy as np

def simulating_coin():
    np.random.seed(42)
    random_numbers = np.random.random(size=4)
    print(random_numbers)
    heads = random_numbers < 0.5
    print(heads)
    print(np.sum(heads))

# Se lanza 10000 veces
def simulating_coins():
    n_all_heads = 0  # Initialize number of 4-heads trials
    for _ in range(10000):
        heads = np.random.random(size=4) < 0.5
        n_heads = np.sum(heads)
        if n_heads == 4:
            n_all_heads += 1
    print(n_all_heads / 10000)


# La distribucion Uniforme

# funcion de probabilidad uniforme discreta
#  P(X=x) = 1/n

#The bus arrives at station one time in 20 minutes.
#Some passenger came to the station at random time,
#what the probability that passenger gets on the bus in 5
#minutes interval? This time I will show this without code.


def ecdf(data):
    """ Compute ECDF """
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return(x,y)


# La distribucion Binomial
def distribucion_binomial():
    a = np.random.binomial(4, 0.5)
    print(a)
    a = np.random.binomial(4, 0.5, size=10)
    print(a)
    samples = np.random.binomial(60, 0.1, size=10000)
    print(samples)

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set()
    x, y = ecdf(samples)
    plt.plot(x, y, marker='.', linestyle='none')
    plt.margins(0.02)
    plt.xlabel('number of successes')
    plt.ylabel('CDF')
    plt.show()


# La distribucion Poisson
def distribucion_poisson():
    samples = np.random.poisson(6, size=10000)
    x, y = ecdf(samples)

    import matplotlib.pyplot as plt

    plt.plot(x, y, marker='.', linestyle='none')
    plt.margins(0.02)
    plt.xlabel('number of successes')
    plt.ylabel('CDF')
    plt.show()


if __name__ == '__main__':
    distribucion_poisson()