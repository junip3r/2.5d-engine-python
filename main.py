import math
import pygame
from player import player
from settings import *
from map import world_map

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pl = player()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pl.movement()
	sc.fill(BLACK)

	pygame.draw.circle(sc, GREEN, (int(pl.x), int(pl.y)), player_radius)
	pygame.draw.line(sc, GREEN, pl.pos, (pl.x + WIDTH * math.cos(pl.angle),
		pl.y + WIDTH * math.sin(pl.angle)), width=1)
	for x, y in world_map:
		pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), width=2)

	pygame.display.flip()
	clock.tick(FPS)