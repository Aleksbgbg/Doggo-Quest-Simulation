import random
import calendar
import time


class Player:
    def __init__(self, name, deck_size, dogs):
        self.name = name
        self._deck = []

        # Seed random with current time to eradicate previous seeds
        #if self.seeds == 0:
         #   random.seed(calendar.timegm(time.gmtime()))
          #  self.seeds += 1

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

    def _pick_fighter(self):
        return random.choice(self.deck)

    def fight(self, other_player):
        fighter_1 = self._pick_fighter()
        fighter_2 = other_player._pick_fighter()

        def swap_cards(player_1, player_2):
            swap_dog = player_1.deck.pop()
            # print(f"{player_1.name} acquires {player_2.name}'s {swap_dog.name}")
            player_2.deck.append(swap_dog)

        if fighter_1.strength > fighter_2.strength:
            swap_cards(other_player, self)
        else:
            swap_cards(self, other_player)