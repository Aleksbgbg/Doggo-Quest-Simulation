import random


class Player:
    def __init__(self, name, dogs):
        self.name = name
        self._deck = [dog for dog in dogs]
        self._acquired_deck = []

    @property
    def acquired_deck(self):
        return self._acquired_deck

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

        #print(f"{self.name} picks {fighter_1.name}\n{other_player.name} picks {fighter_2.name}")

        def swap_cards(player_1, player_2, dog):
            #print(f"{player_1.name} acquires {player_2.name}'s {dog.name}")
            player_1.acquired_deck.append(dog)
            player_2.deck.remove(dog)

        if fighter_1.strength == fighter_2.strength:
            return
        elif fighter_1.strength > fighter_2.strength:
            swap_cards(self, other_player, fighter_2)
        else:
            swap_cards(other_player, self, fighter_1)