import sys
import bisect

def compute_anti_primes(limit):
    # Initialize the array to count divisors
    divisor_count = [0] * (limit + 1)
    
    # Compute number of divisors for each number
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            divisor_count[j] += 1
    
    # List to store anti-primes
    anti_primes = []
    max_divisors = 0
    
    # Identify anti-primes
    for i in range(1, limit + 1):
        if divisor_count[i] > max_divisors:
            anti_primes.append(i)
            max_divisors = divisor_count[i]
    
    return anti_primes

def main():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    queries = [int(data[i]) for i in range(1, T + 1)]
    
    # Precompute anti-primes
    limit = 10**7
    anti_primes = compute_anti_primes(limit)
    
    results = []
    for x in queries:
        idx = bisect.bisect_left(anti_primes, x)
        results.append(str(anti_primes[idx]))
    
    # Output all results
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
