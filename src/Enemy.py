from Move import Move


class Enemy:
    def makeMove(self, game_state):
        enemy_peices = game_state.getEnemyPeices()
        player_peices = game_state.getPlayerPeices()
        print(self.calculate_score_of_board(enemy_peices, player_peices))
        self.getMinScore(enemy_peices, player_peices)
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

    def getMinScore(self, enemy_peices, player_peices):
        print(self.every_possible_board(enemy_peices, player_peices))

    def every_possible_board(self, peices_to_move, peices_to_reach):
        moves_possible = []
        invalid_tiles = []
        for peice in peices_to_reach:
            invalid_tiles.append((peice.i, peice.j))
        for peice in peices_to_move:
            current_i = peice.i
            current_j = peice.j
            
