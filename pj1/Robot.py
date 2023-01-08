MOVE = 20

Ndir = [-1, 0] #sang trai
Sdir = [1, 0]  #sang phai
Wdir = [0, -1] #xuong duoi
Edir = [0, 1]  #len tren

NEdir = [-1, 1]
NWdir = [-1, -1]
SEdir = [1, 1]
SWdir = [1, -1]


class Rb():
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.move1 = True
        self.path = [(0, 0)]
        self.backTrackList = []

        # self.dir =

    def BoustrophedonMove(self, board_state):
        x = self.posX
        y = self.posY

        N_cell = [x + Ndir[0], y + Ndir[1]]
        S_cell = [x + Sdir[0], y + Sdir[1]]
        E_cell = [x + Edir[0], y + Edir[1]]
        W_cell = [x + Wdir[0], y + Wdir[1]]

        if self.CheckAvailableCell(board_state, N_cell[0], N_cell[1]):
            move = Ndir
        elif self.CheckAvailableCell(board_state, S_cell[0], S_cell[1]):
            move = Sdir
        elif self.CheckAvailableCell(board_state, E_cell[0], E_cell[1]):
            move = Edir
        elif self.CheckAvailableCell(board_state, W_cell[0], W_cell[1]):
            move = Wdir
        else:
            move = [0, 0]
            self.move1 = False

        self.posX += move[0]
        self.posY += move[1]
        self.path.append((self.posX, self.posY))

    def CheckAvailableCell(self, board_state, x, y):
        if 0 <= x <= 39 and 0 <= y <= 39:
            if board_state.board[x][y] == '0':
                return True
            else:
                return False

        return False

    # def getBackTrackingList(self, board_state):
    #
    #     for pos in self.path:
    #         if self.evaluatePathPos(board_state, pos[0], pos[1]) >= 1:
    #             self.backTrackList.append(pos)
    #
    # def evaluatePathPos(self, board_state, x, y):
    #
    #     c1 = [x + Edir[0], y + Edir[1]]
    #     c2 = [x + NEdir[0], y + NEdir[1]]
    #     c3 = [x + Ndir[0], y + Ndir[1]]
    #     c4 = [x + NWdir[0], y + NWdir[1]]
    #     c5 = [x + Wdir[0], y + Wdir[1]]
    #     c6 = [x + SWdir[0], y + SWdir[1]]
    #     c7 = [x + Sdir[0], y + Sdir[1]]
    #     c8 = [x + SEdir[0], y + SEdir[1]]
    #
    #     return self.fB(board_state, c1, c8) + self.fB(board_state, c1, c2) + self.fB(board_state, c5, c6) + self.fB(
    #         board_state, c5, c4) + self.fB(board_state, c7, c6) + self.fB(board_state, c7, c8)

    # caculate function b(si, sj)
    # def fB(self, board_state, cel1, cel2):
    #
    #     if 0 <= cel1[0] <= 19 and 0 <= cel1[1] <= 19 and board_state.board[cel1[0]][cel1[1]] == '0':
    #         if not (0 <= cel2[0] <= 19 and 0 <= cel2[1] <= 19) or board_state.board[cel2[0]][cel2[1]] == '1':
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         return 0