class Player(): 
    """---MAY 4th HEAVY WIP. UNTESTED---"""
    
    """Represents the player of a grid based game. """

    def __init__(self, pos_x, pos_y):
        """Constructor: Creates player with supplied values. """

        #self.rows = reference to grid.rows
        #self.cols = reference to grid.cols

        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, direction):
        """Moves the player in some direction. Called by event handler."""

        if direction == "up":
            if self.pos_y > 0:
                self.pos_y -= 1
            else:
                print("Player at top, cannot move up")

        elif direction == "down":
            if self.pos_y < self.cols:
                self.pos_y += 1
            else:
                print("Player at bottom, cannot move down")

        elif direction == "left":
            if self.pos_x > 0:
                self.pos_x -= 1
            else:
                print("Player at left edge, cannot move left")

        elif direction == "right":
            if self.pos_x < self.rows:
                self.pos_x += 1
            else:
                print("Player at right edge, cannot move right")

    def is_valid(self):
        """Checks if a move is valid. """