# game loop
while True:
    mountains = [input() for i in range(8)]
    print(mountains.index(max(mountains)))
