from math import factorial as f, log10


def binomial_random_variable(n, k, p):
    return (f(n) / (f(k) * f(n-k))) * p**k * (1-p)**(n-k)


n = int(input())
prob = [binomial_random_variable(n*2, k, 0.5) for k in range(2*n, -1, -1)]
print(*(str(round(log10(sum(prob[:i])), 3)) for i in range(2*n, 0, -1)))
