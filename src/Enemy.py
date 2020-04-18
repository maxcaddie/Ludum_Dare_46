from Move import Move


class Enemy:
    def makeMove(self, game_state):
        enemy_peices = game_state.getEnemyPeices()
        player_peices = game_state.getPlayerPeices()
        print(self.calculate_score_of_board(enemy_peices, player_peices))
        self.getMinScore(enemy_peices, player_peices, game_state.getState())
        return None

    def calculate_score_of_board(self, enemy_peices, player_peices):
        score = 0
        for enemy_peice in enemy_peices:
            score += self.calculate_score_of_peice(enemy_peice, player_peices)
        return score

    def calculate_score_of_peice(self, enemy_peice, player_peices):
        min_score = 999999
        for player_piece in player_peices:
            min_score = min(min_score, self.calculate_score_to_that_peice(
                enemy_peice, player_piece))
        return min_score

    def calculate_score_to_that_peice(self, enemy_peice, player_peice):
        return pow(abs(enemy_peice.i-player_peice.i)+abs(enemy_peice.j-player_peice.j), 2)

    def getMinScore(self, enemy_peices, player_peices, state):
        print(self.everyPossibleBoard(enemy_peices, player_peices, state))

    def everyPossibleBoard(self, peices_to_move, peices_to_reach, state):
        moves_possible = []
        invalid_tiles = []
        for peice in peices_to_reach:
            invalid_tiles.append((peice.i, peice.j))

        for peice in peices_to_move:
            this_peice_reach = self.getReachable(peice, invalid_tiles, state)
            for reachable in this_peice_reach:
                possible_move = Move(
                    peice.i, peice.j, reachable[0][0], reachable[0][1], reachable[1], False)
                moves_possible.append(possible_move)

        # DO moves on a fake board?

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
