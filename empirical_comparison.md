# Coin Change Performance Comparison

I compared the naive recursive, memoized, and bottom-up dynamic-programming approaches using coins `[1, 2, 5]` and amounts 50, 100, 200, and 400. Each time is the median per-call runtime in milliseconds from seven repetitions of five calls; all three approaches returned the same number of combinations for each amount.

| Amount | Naive recursive (ms) | Memoized (ms) | Bottom-up DP (ms) | Combinations |
|---:|---:|---:|---:|---:|
| 50 | 0.380300 | 0.091900 | 0.006420 | 146 |
| 100 | 3.338900 | 0.086660 | 0.013640 | 541 |
| 200 | 29.876140 | 0.143960 | 0.023900 | 2,081 |
| 400 | 261.080760 | 0.371680 | 0.061220 | 8,161 |

The naive recursive approach became substantially slower as the amount increased, reaching about 261 ms at 400. Memoization was much faster, and bottom-up dynamic programming was the fastest at every tested amount. The bottom-up implementation counts combinations, so all three approaches solve the same problem.