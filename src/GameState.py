class GameState:

    def __init__(self):
        self.state = [[0 for i_counter in range(
            0, 9)] for j_counter in range(0, 9)]
        self.addPeices(4, 4, 2, True)

    def addPeices(self, i, j, number, player):
        if isValidIJ(i, j):
            if not player:
                number *= -1
            self.state[i][j] += number

    def removePeices(self, i, j, number, player):
        self.addPeices(i, j, number*-1, player)

    def processMove(self, move):
        from_i = move.from_pos[0]
        from_j = move.from_pos[1]

        self.removePeices(from_i, from_j, move.size, move.player)

        to_i = move.to_pos[0]
        to_j = move.to_pos[1]

        self.addPeices(to_i, to_j, move.size, move.player)

    def getNumberOfPeices(self, positve):
        count = 0
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[0])):
                if self.state[i][j] == 0:
                    continue
                elif self.state[i][j] > 0 and positve:
                    count += 1
                elif self.state[i][j] < 0 and not positve:
                    count += 1
        return count

    def getState(self):
        return self.state

    def getTile(self, i, j):
        if self.isValidIJ(i, j):
            return self.state[i][j]
        return None

    def isValidIJ(self, i, j):
        return i < len(self.state) and j < len(self.state[0]) and i >= 0 and j >= 0
