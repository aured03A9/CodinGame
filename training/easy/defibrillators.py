import math

def to_radians(x):
    return math.radians(float(x.replace(',', '.')))

longitude_a = to_radians(input())
latitude_a = to_radians(input())
nb_defib = int(input())
defib = []
distance = []

for i in range(nb_defib):
    defib.append(input().split(';'))
    longitude_b = to_radians(defib[i][4])
    latitude_b = to_radians(defib[i][5])
    x = (longitude_b - longitude_a) * math.cos((latitude_a + latitude_b) / 2)
    y = (latitude_b - latitude_a)
    distance.append((math.sqrt(x**2 + y**2) * 6371))

print(defib[distance.index(min(distance))][1])
