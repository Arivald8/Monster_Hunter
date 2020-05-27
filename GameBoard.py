def draw_board(board):
    """
    This function takes board as a parameter, which is a list of empty strings -> ' '. It holds 99 indices.
    This function also checks whether the player encountered a monster and if he did, it changes the position of the
    monster from hidden to monster_name.
    """
    line = '----------------------------------------'
    
    print(f'{line}\n{line}', end='')

    # defines the row in 10s, goes from 90 to 0
    for row in range(9, -1, -1):
        print(f'\n{line}')

        # counts in 1s e.g. 90 to 90 + 9
        for pos in range(row*10, row*10 + 10):
            # ' B |' + ' X |' = ' B | X |'
            print(f' {board[pos]} |', end='')
            
    print(f'\n{line}\n{line}\n{line}')


# --- Create the board --- #
theBoard = [' ' for i in range(0, 100)]
