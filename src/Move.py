class Move:
    def __init__(self, from_i, from_j, to_i, to_j, size, player):
        self.from_pos = (from_i, from_j)
        self.to_pos = (to_i, to_j)
        self.size = size
        self.player = player

    def toString(self):
        return "F: "+str(self.from_pos)+" T: "+str(self.to_pos)+" S: "+str(self.size)+" P: "+str(self.player)
