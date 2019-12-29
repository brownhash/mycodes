"""
input map -

1 1 1 0
1 0 1 1
1 0 9 1
1 1 1 0

Possible paths -

1 1 1
    1
    9

1 1 1
    1 1
    9 1

1
1
1   9
1 1 1

"""

# get value of specified coordinates

def get_val(path, row, col):
    return(path.get(row)[col - 1])


# get the directions in which we can go from a particular point
# the coordinates are in order Right, Left, Up, Down

def get_movement(path, row, col):
    def right_coord(path, row, col):
        col_limit = len(path.get(row))
        if (col < col_limit):
            col += 1
            if (get_val(path, row, col) != 0):
                return ([row, col])
            else:
                return ([])
        else:
            return ([])

    def down_coord(path, row, col):
        row_limit = len(path)
        if (row < row_limit):
            row += 1
            if (get_val(path, row, col) != 0):
                return ([row, col])
            else:
                return ([])
        else:
            return ([])

    def left_coord(path, row, col):
        if (col > 1):
            col -= 1
            if (get_val(path, row, col) != 0):
                return ([row, col])
            else:
                return ([])
        else:
            return ([])

    def up_coord(path, row, col):
        if (row > 1):
            row -= 1
            if (get_val(path, row, col) != 0):
                return ([row, col])
            else:
                return ([])
        else:
            return ([])

    r_coord = right_coord(path, row, col)
    l_coord = left_coord(path, row, col)
    u_coord = up_coord(path, row, col)
    d_coord = down_coord(path, row, col)
    directions = []

    for coord in (r_coord, l_coord, u_coord, d_coord):
        if(coord):
            directions.append(coord)

    return(directions)


path = {
    1:[1,1,1,0],
    2:[1,0,1,1],
    3:[1,0,9,1],
    4:[1,1,1,0]
}

for row in path:
    for col in range(1,len(path.get(row))+1):
        start = [row, col]
        rail = [start]
        direction = get_movement(path, row, col)

        print(direction)
