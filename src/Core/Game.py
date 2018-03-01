class Game:
    def __init__(self):
        pass

    def run(self):
        """
        Run one frame of the game, and return a boolean value indicating whether the game is still running.
        """

        self.update_model()
        self.compose_frame()

        return True

    def update_model(self):
        """
        Update game data.
        """
        pass

    def compose_frame(self):
        """
        Print current frame to output.
        """
        pass
