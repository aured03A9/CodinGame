# the number of temperatures to analyse
n = int(input())
# the n temperatures expressed as integers ranging from -273 to 5526
temps = [int(i) if i else 0 for i in input().split(' ')]

print(sorted(temps, key=lambda x: (abs(x), -x))[0])
#print(min(temps, default=0, key=lambda x: abs(x)))
