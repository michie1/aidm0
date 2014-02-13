from numpy import *

def analyse_collisions(K, N, L):
	# K = 100 # # Objects
	# N = 1000 # # Buckets
	# L = 5 # Count size
	buckets = [0] * N # # of objects in bucket
	counts = [0] * (L + 1) # # of buckets with l objects
	rand_int = random.randint(1, N + 1, K) # Random objects
	
	# Count elements in buckets
	for i in rand_int:
		buckets[i] += 1

	# Count buckets with specific amount of objects in bucket
	for n in range(N):
		counts[buckets[n]] += 1

	return counts 
