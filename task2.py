from numpy import *
K = 100
N = 1000
L = 5
buckets = random.binomial(K, 1.0/N, N)
counts = [0] * (L + 1) # # of buckets with l objects

# Count buckets with specific amount of objects in bucket
for n in range(N):
	counts[buckets[n]] += 1

print counts
