
# we only append one value at once if we are using list.append(40)

# else we can use for loop ----- 
games = [10]
for i in range(5):
    game = input(f"Enter game {i + 1}: ")
    games.append(game)

print("\nAll games:", games)
print("Second game:", games[1])