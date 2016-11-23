# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

# game loop
while 1:
    # The remaining amount of turns Thor can move.
    remaining_turns = int(input())

    # A single line providing the move to be made: N NE E SE S SW W or NW
    direction = ''

    if thor_y > light_y:
        direction += 'N'
        thor_y -= 1
    elif thor_y < light_y:
        direction += 'S'
        thor_y += 1

    if thor_x > light_x:
        direction += 'W'
        thor_x -= 1
    elif thor_x < light_x:
        direction += 'E'
        thor_x += 1

    print(direction)
