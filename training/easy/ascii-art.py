l = int(input())
h = int(input())
t = input().upper()
row = [input() for i in range(h)]

for i in range(h):
    for c in t:
        c = ord(c) - 65 if c.isalpha() else 26
        print(row[i][l*c:l*(c+1)], end='')
    print()
