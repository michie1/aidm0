from scipy import stats
#K = 1 
#N = 10
#L = 5

#k = 2 # number of heads
#n = 2 # number of coin tosses
#p = 0.5 # probability of heads
k = 1
n = 10
l = 5
counts = [0] * l

for i in range(l):
	counts[i] = stats.binom.pmf(k, n, i) * n
	print stats.binom.pmf(k, n, i)

print counts
