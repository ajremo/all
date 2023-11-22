#DAA-4 0/1 Knapsack Problem
def solve_knapsack():
    val = [50, 100, 150, 200]  
    wt = [8, 16, 32, 40]  
    W = 64
    n = len(val) - 1

    def knapsack(W, n): 
        # base case
        if n < 0 or W <= 0:
            return 0
        if wt[n] > W:
            return knapsack(W, n - 1)
        else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))
    print(knapsack(W, n))

if __name__ == "__main__":
    solve_knapsack()