

def fibonacci_dp(n, memo):
    """
    dp ≈ recursion + memorization
    :param memo: an empty dictionary
    :param n:the position of the fibonacci number we want to know
    :return:the fibonacci number at position n
    """
    if n in memo:
        return memo[n]
    else:
        if n <= 1:
            return n
        else:
            f = fibonacci_dp(n-1, memo) + fibonacci_dp(n-2, memo)
            memo[n] = f
            return f


if __name__ == '__main__':
    print(fibonacci_dp(6, {}))
