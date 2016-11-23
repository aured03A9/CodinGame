n = int(input())
pi = sorted([int(input()) for i in range(n)])
print(min([abs(pi[i] - pi[i-1]) for i in range(n)]))
