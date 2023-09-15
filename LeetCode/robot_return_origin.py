
def robotComeback(moves) ->bool:
    """
    params
    moves : String (U|D|R|L)

    return
    Boolean : the robot return to it's initial position
    """

    horizontal_ = vertical_ = 0

    for command in moves:
        if command == 'R':
            horizontal_ += 1
        elif command == 'L':
            horizontal_ -= 1
        elif command == 'U':
            vertical_ += 1
        elif command == 'D':
            vertical_ -=1
    
    return horizontal_ == vertical_ == 0


moves = 'LRDDRDUUURLL' #robot start move to left, right, down twice, right, down, up three times, right, and last move to left twice
print(robotComeback(moves)) # True
