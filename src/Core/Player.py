import random
import calendar
import time


class Player:
    def __init__(self, deck_size, dogs):
        self._deck = []

        # Seed random with current time to eradicate previous seeds
        random.seed(calendar.timegm(time.gmtime()))

        picked_dogs = []

        for iteration in range(deck_size):
            chance = random.random()

            for dog_name, dog_attributes in dogs.items():
                if dog_name in picked_dogs:
                    continue

                if dog_attributes["probability"] < chance:
                    picked_dogs.append(dog_name)
                    self.deck.append(dog_attributes["instance"])
                    break

    @property
    def deck(self):
        return self._deck

    def print_deck(self):
        print(", \n".join(str(item) for item in self.deck))