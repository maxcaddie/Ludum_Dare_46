from Move import Move
from Tile import Tile


class Enemy:
    def makeMove(self, game_state):
        enemy_peices = game_state.getEnemyPeices()
        player_peices = game_state.getPlayerPeices()
        print(self.calculate_score_of_board(enemy_peices, player_peices))
        move = self.getMinScore(
            enemy_peices, player_peices, game_state)
        return move

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
        return (abs(enemy_peice.i-player_peice.i)+abs(enemy_peice.j-player_peice.j))*(enemy_peice.stack_size*-1)

    def getMinScore(self, enemy_peices, player_peices, game_state):
        temp_state = game_state.copy()
        min_move = self.minMove(
            enemy_peices, player_peices, temp_state, 1)
        temp_state.processMove(min_move)
        return min_move

    def minMove(self, peices_to_move, peices_to_reach, game_state, depth):
        state = game_state.getState()
        moves_possible = []
        invalid_tiles = []
        for peice in peices_to_reach:
            invalid_tiles.append((peice.i, peice.j))

        score_current = self.calculate_score_of_board(
            peices_to_move, peices_to_reach)
        best_new_score = score_current+99999999
        move_to_make = None

        for peice in peices_to_move:
            this_peice_reach = self.getReachable(
                peice, invalid_tiles, state)
            this_peice_score = self.calculate_score_of_peice(
                peice, peices_to_reach)
            best_temp = None
            best_score_moving_this = 9999999
            for reachable in this_peice_reach:
                for i in range(reachable[1], (peice.stack_size*-1)+1):
                    temp = Tile(reachable[0][0], reachable[0][1])
                    temp.stack_size = i*-1

                    if depth == 0:
                        temp_score = self.calculate_score_of_peice(
                            temp, peices_to_reach)+((this_peice_score/peice.stack_size)*(peice.stack_size-temp.stack_size))
                        print("(", peice.i, peice.j, ")",
                              "(", temp.i, temp.j, ")", temp_score, temp.stack_size)
                    else:
                        game_state_copy = game_state.copy()
                        temp_move = Move(
                            peice.i, peice.j, temp.i, temp.j, temp.stack_size, False)
                        game_state_copy.processMove(temp_move)
                        temp_score = self.maxMove(
                            peices_to_reach, peices_to_move, game_state_copy, depth)

                    if temp_score < best_score_moving_this:
                        best_score_moving_this = temp_score
                        best_temp = temp.copy()
                    del(temp)

            score_after_making_best_move = (
                score_current+best_score_moving_this-this_peice_score)
            if (best_new_score > score_after_making_best_move):
                best_new_score = score_after_making_best_move
                move_to_make = Move(
                    peice.i, peice.j, best_temp.i, best_temp.j, best_temp.stack_size, False)
        print("Move chosen", move_to_make.from_pos,
              move_to_make.to_pos, best_new_score)
        return move_to_make

    def maxMove(self, peices_to_move, peices_to_reach, game_state, depth):
        state = game_state.getState()
        moves_possible = []
        invalid_tiles = []
        for peice in peices_to_reach:
            invalid_tiles.append((peice.i, peice.j))

        score_current = self.calculate_score_of_board(
            peices_to_move, peices_to_reach)
        best_new_score = score_current-99999999
        move_to_make = None

        for peice in peices_to_move:
            this_peice_reach = self.getReachable(
                peice, invalid_tiles, state)
            this_peice_score = self.calculate_score_of_peice(
                peice, peices_to_reach)
            best_temp = None
            best_score_moving_this = -99999999
            for reachable in this_peice_reach:
                for i in range(reachable[1], (peice.stack_size)+1):
                    temp = Tile(reachable[0][0], reachable[0][1])
                    temp.stack_size = i

                    game_state_copy = game_state.copy()
                    temp_move = Move(
                        peice.i, peice.j, temp.i, temp.j, temp.stack_size, True)
                    game_state_copy.processMove(temp_move)
                    temp_move = self.minMove(
                        peices_to_reach, peices_to_move, game_state_copy, depth-1)
                    game_state_copy.processMove(temp_move)
                    temp_score = self.calculate_score_of_board(
                        game_state_copy.getEnemyPeices(), game_state_copy.getPlayerPeices())

                    if temp_score > best_score_moving_this:
                        best_score_moving_this = temp_score
                        best_temp = temp.copy()
                    del(temp)

            score_after_making_best_move = (
                score_current+best_score_moving_this-this_peice_score)
            if (best_new_score > score_after_making_best_move):
                best_new_score = score_after_making_best_move
                move_to_make = Move(
                    peice.i, peice.j, best_temp.i, best_temp.j, best_temp.stack_size, True)

        return best_new_score

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
