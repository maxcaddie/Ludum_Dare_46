from Move import Move
from Tile import Tile


class Enemy:
    def makeMove(self, game_state):
        enemy_peices = game_state.getEnemyPeices()
        player_peices = game_state.getPlayerPeices()
        move = self.getBestMove(
            enemy_peices, player_peices, game_state)
        return move

    def calculate_score_of_board(self, enemy_peices, player_peices):
        # for e in enemy_peices:
        #     print("e: "+str(e.i), e.j)
        # for p in player_peices:
        #     print("p:", p.i, p.j)
        score = 0
        for enemy_peice in enemy_peices:
            score += self.calculate_score_of_peice(enemy_peice, player_peices)
            # print(score, enemy_peice.i, enemy_peice.j)
        return score

    def calculate_score_of_peice(self, enemy_peice, player_peices):
        min_score = 999999
        for player_piece in player_peices:
            # print(player_piece.i, player_piece.j)
            min_score = min(min_score, self.calculate_score_to_that_peice(
                enemy_peice, player_piece))*(enemy_peice.stack_size*-1)
        return min_score

    def calculate_score_to_that_peice(self, enemy_peice, player_peice):
        score = (abs(enemy_peice.i-player_peice.i) +
                 abs(enemy_peice.j-player_peice.j))
        # print(score)
        return score

    def getBestMove(self, enemy_peices, player_peices, game_state):
        min_score = 999999999
        min_move = None
        invalid_tiles = []q
        for peice in player_peices:
            invalid_tiles.append((peice.i, peice.j))
        for peice in enemy_peices:
            reachable = self.getReachable(
                peice, invalid_tiles, game_state.getState())
            for reach in reachable:
                for i in range(1, reach[1]+1):
                    this_move = Move(peice.i, peice.j,
                                     reach[0][0], reach[0][1], i*-1, False)
                    copy_state = game_state.copy()
                    copy_state.processMove(this_move)
                    this_score = self.getMax(copy_state, 1)

                    if this_score < min_score:
                        min_score = this_score
                        min_move = this_move

        game_state.printState()
        print(min_move.toString())
        return min_move

    def getMax(self, game_state, depth):
        max_score = -1
        max_move = None
        invalid_tiles = []
        enemy_peices = game_state.getEnemyPeices()
        player_peices = game_state.getPlayerPeices()

        for peice in enemy_peices:
            invalid_tiles.append((peice.i, peice.j))
        for peice in player_peices:
            reachable = self.getReachable(
                peice, invalid_tiles, game_state.getState())
            for reach in reachable:
                this_move = Move(peice.i, peice.j,
                                 reach[0][0], reach[0][1], reach[1], True)
                copy_state = game_state.copy()
                copy_state.processMove(this_move)
                new_copy = copy_state.copy()
                this_score = self.getMin(new_copy, depth-1)
                # print("max: "+str(this_score), this_move.toString()+"\n")
                if this_score > max_score:
                    max_score = this_score
                    max_move = this_move
        return max_score

    def getMin(self, game_state, depth):
        min_score = 999999999
        invalid_tiles = []
        player_peices = game_state.getPlayerPeices()
        enemy_peices = game_state.getEnemyPeices()
        for peice in player_peices:
            invalid_tiles.append((peice.i, peice.j))
        for peice in enemy_peices:
            # print("NEW PEICE")
            # print(peice.i, peice.j)
            reachable = self.getReachable(
                peice, invalid_tiles, game_state.getState())
            for reach in reachable:
                this_move = Move(peice.i, peice.j,
                                 reach[0][0], reach[0][1], reach[1]*-1, False)
                copy_state = game_state.copy()
                copy_state.processMove(this_move)
                if depth == 0:

                    this_score = self.calculate_score_of_board(
                        copy_state.getEnemyPeices(), copy_state.getPlayerPeices())
                    # print("Root: "+str(this_score), this_move.toString())
                else:
                    new_copy = copy_state.copy()
                    this_score = self.getMax(new_copy, depth)
                    # print("min: "+str(this_score), this_move.toString())
                min_score = min(min_score, this_score)

        return min_score

    def getReachable(self, peice, bad_tiles, state):

        reachable_nodes = []
        for i in range(1, abs(peice.stack_size)+1):
            left = (peice.i-i, peice.j)
            up = (peice.i, peice.j-i)
            right = (peice.i+i, peice.j)
            down = (peice.i, peice.j+i)

            if left[0] >= 0 and left not in bad_tiles:
                reachable_nodes.append((left, i))

            if up[1] >= 0 and up not in bad_tiles:
                reachable_nodes.append((up, i))

            if right[0] < len(state) and right not in bad_tiles:
                reachable_nodes.append((right, i))

            if down[1] < len(state[0]) and down not in bad_tiles:
                reachable_nodes.append((down, i))
        return reachable_nodes
