class Board():
    '''constructor for board'''
    empty_cell = " "
    combinations = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
                    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    def __init__(self):
        self._field = [[Board.empty_cell for i in range(3)] for j in range(3)]
        self._lastMove = None
        self.availible_cells = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def __str__(self):
        s = "\n"
        s += "                    0     1     2\n\n"
        for i in range(3):
            for j in range(3):
                if j == 1:
                    s += "|  " + str(self._field[i][j]) + "  |"
                elif j == 0:
                    s += "               " + str(i) + "    " + str(self._field[i][j]) + "  "
                else:
                    s += "  " + str(self._field[i][j]) + " "
            if i < 2:
                s += "\n                  ------------------\n"
        return s

    def put(self, turn, coord):
        '''
        :param turn: num of turn
        :param coord: coords of the place
        :return: True or False(depends on availability of place)
        '''
        row = coord[0]
        col = coord[1]
        if coord in self.availible_cells:
            self._field[row][col] = turn
            self._lastMove = (turn, coord)
            self.availible_cells.remove(coord)
            return True
        else:
            return False

    def check_winner(self):
        '''
        :return: name of winner or "DRAW" if game if finished in a draw
        '''
        def get_value(coord):
            return self._field[coord[0]][coord[1]]
        counter = 0
        for comb in Board.combinations:
            if get_value(comb[0]) == get_value(comb[1]) == get_value(comb[2]) != Board.empty_cell:
                counter += 1
                winner = get_value(comb[0])
        if counter > 0:
            return winner
        draw_counter = 0
        if self.availible_cells == []:
            return "DRAW"
        return None
