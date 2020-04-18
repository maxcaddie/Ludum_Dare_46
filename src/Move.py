class Move:
    def __init__(self, from_i, from_j, to_i, to_j, size, player):
        self.from_pos = (from_i, from_j)
        self.to_pos = (to_i, to_j)
        self.size = size
        self.player = player
