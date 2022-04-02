scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellow jacket", "hornet", "paper wasp"}

scary_set = scorpions | snakes | spiders | vespas
print(scary_set)

land_scary = scorpions.union(snakes.union(spiders))
print(land_scary)

