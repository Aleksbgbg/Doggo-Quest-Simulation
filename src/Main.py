from Core.Game import Game

iterations = 100000

game = Game()

wins = [0, 0]

for iteration in range(iterations):
    while True:
        result = game.run()

        if result == -1:
            continue

        wins[result] += 1

        game = Game()

        break

print(f"Player 1 wins: {wins[0]:,} ({wins[0] / iterations * 100:.2f}%)\nPlayer 2 wins: {wins[1]:,} ({wins[1] / iterations * 100:.2f}%)")