games = []
for i in range(5):
    game = input(f"Enter game {i + 1}: ")
    games.append(game)

print("\nAll games:", games)
print("Second game:", games[1])