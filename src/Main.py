from Core.Game import Game

game = Game()

wins = [0, 0]

for iteration in range(100000):
    while True:
        result = game.run()

        if result == -1:
            continue
        print(result)

        wins[result] += 1
        game = Game()
        break

print(wins)