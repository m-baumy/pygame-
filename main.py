import pygame
import random
from random import randrange
pygame.display.set_caption('Mouse escaping Game')
icon=pygame.image.load('mice.png')
pygame.display.set_icon(icon)
pygame.display.init()
x = 50
y = 50
z = 50
steps_value = 0
blue = (0, 0, 255)
white = (255, 255, 255)
green = (0, 255, 0)
pink = (236, 0, 165)
red = (255, 0, 0)


font = pygame.font.Font('freesansbold.ttf', 32)
textX =10
textY =10




window = pygame.display.set_mode((550, 550))


list = [pygame.draw.rect(window, green, [500, 200, z, z]), \
        pygame.draw.rect(window, blue, [0, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [50, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [100, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [150, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [200, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [250, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [300, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [350, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [400, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [450, 0, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 50, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 100, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 150, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 200, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 250, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 300, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 350, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 400, 50, 50]), \
        pygame.draw.rect(window, blue, [0, 450, 50, 50]), \
        pygame.draw.rect(window, blue, [50, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [100, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [150, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [200, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [250, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [300, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [350, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [400, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [450, 500, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 50, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 100, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 150, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 250, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 300, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 350, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 400, 50, 50]), \
        pygame.draw.rect(window, blue, [500, 450, 50, 50])
        ]

row1 = [pygame.draw.rect(window, white, [x, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 50, y, z, z]), \
        pygame.draw.rect(window, white, [x + 100, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 150, y, z, z]), \
        pygame.draw.rect(window, white, [x + 200, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 250, y, z, z]), \
        pygame.draw.rect(window, white, [x + 300, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 350, y, z, z]), \
        pygame.draw.rect(window, white, [x + 400, y, z, z])]
y = y + 50
row2 = [pygame.draw.rect(window, pink, [x, y, z, z]), \
        pygame.draw.rect(window, white, [x + 50, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 100, y, z, z]), \
        pygame.draw.rect(window, white, [x + 150, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 200, y, z, z]), \
        pygame.draw.rect(window, white, [x + 250, y, z, z]),
        pygame.draw.rect(window, pink, [x + 300, y, z, z]), \
        pygame.draw.rect(window, white, [x + 350, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 400, y, z, z])]
y = y + 50
row3 = [pygame.draw.rect(window, white, [x, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 50, y, z, z]), \
        pygame.draw.rect(window, white, [x + 100, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 150, y, z, z]), \
        pygame.draw.rect(window, white, [x + 200, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 250, y, z, z]), \
        pygame.draw.rect(window, white, [x + 300, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 350, y, z, z]), \
        pygame.draw.rect(window, white, [x + 400, y, z, z])]
y = y + 50
row4 = [pygame.draw.rect(window, pink, [x, y, z, z]), \
        pygame.draw.rect(window, white, [x + 50, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 100, y, z, z]), \
        pygame.draw.rect(window, white, [x + 150, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 200, y, z, z]), \
        pygame.draw.rect(window, white, [x + 250, y, z, z]),
        pygame.draw.rect(window, pink, [x + 300, y, z, z]), \
        pygame.draw.rect(window, white, [x + 350, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 400, y, z, z])]
y = y + 50
row5 = [pygame.draw.rect(window, white, [x, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 50, y, z, z]), \
        pygame.draw.rect(window, white, [x + 100, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 150, y, z, z]), \
        pygame.draw.rect(window, white, [x + 200, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 250, y, z, z]), \
        pygame.draw.rect(window, white, [x + 300, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 350, y, z, z]), \
        pygame.draw.rect(window, white, [x + 400, y, z, z])]

row6 = [pygame.draw.rect(window, white, [x, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 50, y, z, z]), \
        pygame.draw.rect(window, white, [x + 100, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 150, y, z, z]), \
        pygame.draw.rect(window, white, [x + 200, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 250, y, z, z]), \
        pygame.draw.rect(window, white, [x + 300, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 350, y, z, z]), \
        pygame.draw.rect(window, white, [x + 400, y, z, z])]
y = y + 50
row7 = [pygame.draw.rect(window, pink, [x, y, z, z]), \
        pygame.draw.rect(window, white, [x + 50, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 100, y, z, z]), \
        pygame.draw.rect(window, white, [x + 150, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 200, y, z, z]), \
        pygame.draw.rect(window, white, [x + 250, y, z, z]),
        pygame.draw.rect(window, pink, [x + 300, y, z, z]), \
        pygame.draw.rect(window, white, [x + 350, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 400, y, z, z])]
y = y + 50
row8 = [pygame.draw.rect(window, white, [x, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 50, y, z, z]), \
        pygame.draw.rect(window, white, [x + 100, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 150, y, z, z]), \
        pygame.draw.rect(window, white, [x + 200, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 250, y, z, z]), \
        pygame.draw.rect(window, white, [x + 300, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 350, y, z, z]), \
        pygame.draw.rect(window, white, [x + 400, y, z, z])]
y = y + 50
row9 = [pygame.draw.rect(window, pink, [x, y, z, z]), \
        pygame.draw.rect(window, white, [x + 50, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 100, y, z, z]), \
        pygame.draw.rect(window, white, [x + 150, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 200, y, z, z]), \
        pygame.draw.rect(window, white, [x + 250, y, z, z]),
        pygame.draw.rect(window, pink, [x + 300, y, z, z]), \
        pygame.draw.rect(window, white, [x + 350, y, z, z]), \
        pygame.draw.rect(window, pink, [x + 400, y, z, z])]
y = y + 50
row10 = [pygame.draw.rect(window, white, [x, y, z, z]), \
         pygame.draw.rect(window, pink, [x + 50, y, z, z]), \
         pygame.draw.rect(window, white, [x + 100, y, z, z]), \
         pygame.draw.rect(window, pink, [x + 150, y, z, z]), \
         pygame.draw.rect(window, white, [x + 200, y, z, z]), \
         pygame.draw.rect(window, pink, [x + 250, y, z, z]), \
         pygame.draw.rect(window, white, [x + 300, y, z, z]), \
         pygame.draw.rect(window, pink, [x + 350, y, z, z]), \
         pygame.draw.rect(window, white, [x + 400, y, z, z])]
catImg = pygame.image.load('cat.png')
cat_pos=[[105,60],[155,60],[205,60],[255,60],[305,60],[355,60],[405,60],[455,60],\
       [55,110],[105,110],[155,110],[205,110],[255,110],[305,110],[355,110],[405,110],[455,110],\
       [55,160],[105,160],[155,160],[205,160],[255,160],[305,160],[355,160],[405,160],[455,160],\
       [55,210],[105,210],[155,210],[205,210],[255,210],[305,210],[355,210],[405,210],[455,210],\
       [55,260],[105,260],[155,260],[205,260],[255,260],[305,260],[355,260],[405,260],[455,260],\
       [55,310],[105,310],[155,310],[205,310],[255,310],[305,310],[355,310],[405,310],[455,310],\
       [55,360],[105,360],[155,360],[205,360],[255,360],[305,360],[355,360],[405,360],[455,360],\
       [55,410],[105,410],[155,410],[205,410],[255,410],[305,410],[355,410],[405,410],[455,410],\
       [55,460],[105,460],[155,460],[205,460],[255,460],[305,460],[355,460],[405,460],[455,460],\
       ]
q,w=random.choice(cat_pos)
catX =q
catY =w

def cat(catX,catY) :
        window.blit(catImg, (catX,catY))
pygame.display.update()

mouseImg = pygame.image.load('mouse.png')
mouseX =55
mouseY = 60
mouseX_change=0
mouseY_change=0

def mouse(mouseX,mouseY) :
        window.blit(mouseImg, (mouseX,mouseY))



def show_steps(x,y) :
        steps= font.render("score :" + str( steps_value ) , True, (255,255,255))
        window.plit(steps,(x,y) )
pygame.display.update()
while True:
   for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             exit()
         key = pygame.key.get_pressed()
         if key[pygame.K_UP]:
             mouseY_change = -50
             steps_value+= 1
         if key[pygame.K_DOWN]:
             mouseY_change = 50
             steps_value += 1
         if key[pygame.K_RIGHT]:
             mouseX_change = 50
             steps_value+= 1
         if key[pygame.K_LEFT]:
             mouseX_change = -50
             steps_value += 1
   mouseY += mouseY_change
   mouseX += mouseX_change
   mouseX_change = 0
   mouseY_change = 0
   cat(catX, catY)
   mouse(mouseX, mouseY)
   show_steps(textX,textY)
   pygame.display.update()

   pass