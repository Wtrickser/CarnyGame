import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('cloud1.png')
cloud2 = pygame.image.load('cloud2.png')

land_y = 560
land_speed = 1

water_y = 640
water_speed = 1.5

cloud1_y = 50
cloud1_speed = 1

cloud2_y = 70
cloud2_speed = 1

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.blit(wood_bg, (0,0))

  land_y -= land_speed
  if land_y <= 520 or land_y >= 600:
    land_speed *= -1
  screen.blit(land_bg, (0,land_y))

  water_y -= water_speed
  if water_y <= 620 or water_y >= 680:
    water_speed *= -1
  screen.blit(water_bg, (0,water_y))

  cloud1_y -= cloud1_speed
  if cloud1_y <= 30 or cloud1_y >= 80:
    cloud1_speed *= -1
  screen.blit(cloud1, (300,cloud1_y+20))
  screen.blit(cloud1, (650,cloud1_y))
  screen.blit(cloud1, (950,cloud1_y))

  cloud2_y -= cloud2_speed
  if cloud2_y <= 60 or cloud2_y >= 120:
    cloud2_speed *= -1
  screen.blit(cloud2, (100,cloud2_y))
  screen.blit(cloud2, (500,cloud2_y))
  screen.blit(cloud2, (800,cloud2_y))

  pygame.display.update()
  clock.tick(120)