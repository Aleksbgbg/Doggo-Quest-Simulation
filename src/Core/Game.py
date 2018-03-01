import numpy
# import random

from .Dog import Dog
from .Player import Player

class Game:
    def __init__(self):
        dogs = [Dog(f"Dog{iteration}", iteration) for iteration in range(1, 11)]

        player_1 = Player("Player1", numpy.random.choice(dogs, 5, replace=False))
        player_2 = Player("Player2", numpy.random.choice(dogs, 5, replace=False))

        player_1.print_deck()
        player_2.print_deck()
        print()

        self.players = [player_1, player_2]

    def run(self):
        """
        Run one frame of the game, and return a boolean value indicating whether the game is still running.
        """

        self.update_model()
        self.compose_frame()

        is_win_state = any(len(player.deck) == 0 for player in self.players)

        if is_win_state:
            if len(self.players[0].deck) == 0:
                return 1

            return 0

        return -1

    def update_model(self):
        """
        Play one round of the game (and update state).
        """
        fighting_player = self.players[0]
        fighting_player.fight(self.players[1])

    def compose_frame(self):
        """
        Print current frame to output.
        """
        pass
