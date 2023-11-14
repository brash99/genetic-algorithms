from problems import knapsack
from algorithms import bruteforce
import time

weight_limit = 3000

for i in range(25):
    things = knapsack.generate_things(i)
    start = time.time()
    bruteforce(things, weight_limit)
    end = time.time()

    print(f"{i}\t{end-start}")
