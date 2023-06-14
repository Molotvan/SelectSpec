worlds = ['hello', '>=<', 'python', 'my', 'cat', '456', 'dance', 'bye']

for world in worlds:
    if len(world)>3:
        worlds.remove(world)

short_worlds = worlds
print(short_worlds)
