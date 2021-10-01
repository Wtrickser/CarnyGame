import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('cloud1.png')
cloud2 = pygame.image.load('cloud2.png')
crosshair = pygame.image.load('crosshair.png')
duck_surface = pygame.image.load('duck.png')

land_y = 560
land_v = 1

water_y = 640
water_v = 1.5

cloud1_y = 50
cloud1_v = 1

cloud2_y = 70
cloud2_v = 1

duck_list = []
for duck in range(20):
	duck_position_x = random.randrange(50,1200)
	duck_position_y = random.randrange(120,600)
	duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
	duck_list.append(duck_rect)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  screen.blit(wood_bg, (0,0))

  land_y -= land_v
  if land_y <= 520 or land_y >= 600:
    land_v *= -1
  screen.blit(land_bg, (0,land_y))

  for duck_rect in duck_list:
    screen.blit(duck_surface,duck_rect)

  water_y -= water_v
  if water_y <= 620 or water_y >= 680:
    water_v *= -1
  screen.blit(water_bg, (0,water_y))

  cloud1_y -= cloud1_v
  if cloud1_y <= 30 or cloud1_y >= 80:
    cloud1_v *= -1
  screen.blit(cloud1, (300,cloud1_y+20))
  screen.blit(cloud1, (650,cloud1_y))
  screen.blit(cloud1, (950,cloud1_y))

  cloud2_y -= cloud2_v
  if cloud2_y <= 60 or cloud2_y >= 120:
    cloud2_v *= -1
  screen.blit(cloud2, (100,cloud2_y))
  screen.blit(cloud2, (500,cloud2_y))
  screen.blit(cloud2, (800,cloud2_y))

  pygame.display.update()
  clock.tick(120)