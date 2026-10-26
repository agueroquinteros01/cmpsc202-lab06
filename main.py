import matplotlib.pyplot as plt
import statistics
import timeit


def coin_change_recursive(coin_values, amount):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if not coin_values:
        return 0

    return coin_change_recursive(coin_values, amount - coin_values[-1]) + coin_change_recursive(coin_values[:-1], amount)

def coin_change_memoized(coin_values, amount, memo=None):
    if memo is None:
        memo = {}
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if not coin_values:
        return 0

    key = (tuple(coin_values), amount)
    if key in memo:
        return memo[key]

    result = coin_change_memoized(coin_values, amount - coin_values[-1], memo) + coin_change_memoized(coin_values[:-1], amount, memo)
    memo[key] = result
    return result

def coin_change_dp(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] += dp[current_amount - coin]

    return dp[amount]

coins = [1, 2, 5]

if __name__ == "__main__":
    amounts = [50, 100, 200, 400]
    functions = [
        ("Naive recursive", coin_change_recursive),
        ("Memoized", coin_change_memoized),
        ("Bottom-up DP", coin_change_dp),
    ]
    timings = {label: [] for label, _ in functions}

    for amt in amounts:
        for label, function in functions:
            runs = timeit.repeat(
                lambda f=function, n=amt: f(coins, n),
                repeat=7,
                number=5,
            )
            timings[label].append(statistics.median(runs) / 5)

    print("Median runtime per call (milliseconds)")
    print(f"{'Amount':>8}" + "".join(f"{label:>20}" for label, _ in functions))
    for index, amt in enumerate(amounts):
        print(
            f"{amt:>8}"
            + "".join(
                f"{timings[label][index] * 1000:>20.6f}"
                for label, _ in functions
            )
        )

    for label, times in timings.items():
        plt.plot(amounts, times, marker="o", label=label)

    plt.xlabel("Amount")
    plt.ylabel("Execution time (seconds)")
    plt.title(f"Coin Change Runtime Comparison (coins={coins})")
    plt.yscale("log")
    plt.grid(True)
    plt.legend()
    plt.show()