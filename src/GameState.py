from Tile import Tile
from Move import Move


class GameState:

    def __init__(self):
        self.state = [[Tile(i_counter, j_counter) for i_counter in range(
            0, 9)] for j_counter in range(0, 9)]

    def move(self, from_tile, to_tile, player):
        new_move = Move(from_tile.j, from_tile.i, to_tile.j,
                        to_tile.i, from_tile.stack_size, player)
        self.processMove(new_move)

    def addPeices(self, i, j, number, player):
        if self.isValidIJ(i, j):
            tile = self.getTile(i, j)
            print(i == tile.i)
            tile.stack_size += number
            tile.reset_tile_colour()

    def removePeices(self, i, j, number, player):
        self.addPeices(i, j, number*-1, player)

    def processMove(self, move):
        # self.printState()
        from_i = move.from_pos[1]
        from_j = move.from_pos[0]
        # print(self.state[from_i][from_j].stack_size)
        self.removePeices(from_i, from_j, move.size, move.player)

        to_i = move.to_pos[1]
        to_j = move.to_pos[0]

        self.addPeices(to_i, to_j, move.size, move.player)
        # self.printState()

    def getNumberOfPeices(self, positve):
        count = 0
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[0])):
                if self.state[i][j].stack_size == 0:
                    continue
                elif self.state[i][j].stack_size > 0 and positve:
                    count += 1
                elif self.state[i][j].stack_size < 0 and not positve:
                    count += 1
        return count

    def getState(self):
        return self.state

    def copy(self):
        temp_state = GameState()
        for player in self.getPlayerPeices():
            temp_state.addPeices(player.i, player.j, player.stack_size, True)
        for enemy in self.getEnemyPeices():
            temp_state.addPeices(enemy.i, enemy.j, enemy.stack_size, True)

        return temp_state

    def getTile(self, i, j):
        if self.isValidIJ(j, i):
            return self.state[j][i]
        return None

    def isValidIJ(self, i, j):
        return i < len(self.state) and j < len(self.state[0]) and i >= 0 and j >= 0

    def getEnemyPeices(self):
        enemy_peices = []
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[0])):
                tile = self.getTile(i, j)
                if tile.isEnemy():
                    enemy_peices.append(tile)
        return enemy_peices

    def getPlayerPeices(self):
        player_peices = []
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[0])):
                tile = self.getTile(i, j)
                if tile.isPlayer():
                    player_peices.append(tile)
        return player_peices

    def printState(self):
        nums = []
        for row in self.state:
            temp_row = []
            for tile in row:
                temp_row.append(tile.stack_size)
            nums.append(temp_row)
        for row in nums:
            print(row)
