import numpy as np


def biased_coin():
    return np.random.choice([0, 1], p=[1 - r, r])


def unbiased_coin():
    c1 = biased_coin()
    c2 = biased_coin()

    while c1 == c2:
        c1 = biased_coin()
        c2 = biased_coin()

    return c1


if __name__ == '__main__':
    count_head_b = 0
    count_head_u = 0
    iterations = 10000
    r = 0.3
    for i in range(iterations):
        b = biased_coin()
        u = unbiased_coin()
        count_head_b += b
        count_head_u += u
    print(count_head_b / iterations)
    print(count_head_u / iterations)

