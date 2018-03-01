import random

from .Dog import Dog
from .Player import Player

class Game:
    def __init__(self):
        # Predictable random state
        random.seed(0)

        def get_probability_generator():
            index = 0
            probabilities = [0.3, 0.22, 0.18, 0.13, 0.07, 0.05, 0.04, 0.005, 0.003, 0.002]

            assert sum(probabilities) == 1, f"Sum is {sum(probabilities)}, should be 1."

            def get_probability():
                nonlocal index
                probability = probabilities[index]
                index += 1
                return probability

            return get_probability

        get_probability = get_probability_generator()

        dogs = {
            dog.name: {
                "probability": get_probability(),
                "instance": dog
            }
            for dog in [Dog(f"Dog{iteration}", iteration) for iteration in range(1, 11)]
        }

        player_1 = Player(5, dogs)
        player_2 = Player(5, dogs)

        self.players = [player_1, player_2]

        for index, player in enumerate(self.players):
            print(f"\nPlayer #{index}:")
            player.print_deck()

    def run(self):
        """
        Run one frame of the game, and return a boolean value indicating whether the game is still running.
        """

        self.update_model()
        self.compose_frame()

        return False

    def update_model(self):
        """
        Play one round of the game (and update state).
        """
        pass

    def compose_frame(self):
        """
        Print current frame to output.
        """
        pass
