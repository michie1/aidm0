from scipy import stats
#K = 1 
#N = 10
#L = 5

#k = 2 # number of heads
#n = 2 # number of coin tosses
#p = 0.5 # probability of heads

# 5 elementen in 10 buckets, hoeveel buckets met 1 element (of 0).
# k = aantal element in een bucket
# n = 5 el
# l is lengte van de lijst

k = 5
n = 10
l = 5
counts = [0] * l

rv = stats.binom(k, 1/float(n));
print rv.dist



for i in range(l):
	counts[i] = stats.binom.pmf(i, k, 1/float(n)) * n
	#counts[i] = rv.pmf(i) * n
	#print stats.binom.pmf(k, 1/float(n), i)

print counts
