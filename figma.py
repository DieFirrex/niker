import pygame 
pygame.init()
import math

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("GTA 6")

pygame_image = pygame.image.load("niger1.png")
pygame_rect = pygame_image.get_rect(center=(600 // 2,600 // 2))


RED = (255,0,0)
YELLOW = (255,255,0)

bullets = []
bullet_image = pygame.Surface((200,200))
bullet_image.fill((0,0,0))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angel = math.degrees(math.atan2(mouse_y - pygame_rect.centery, mouse_x - pygame_rect.centerx)) - 90
                bullet_x = math.cos(angel) * 10
                bullet_y = math.sin(angel) * 10
                bullets.append([pygame_rect.centerx, pygame_rect.centerx, bullet_x, bullet_y])
    

    mouse_x, mouse_y = pygame.mouse.get_pos()
    angel = math.degrees(math.atan2(mouse_y - pygame_rect.centery, mouse_x - pygame_rect.centerx)) - 90
    image_rotated = pygame.transform.rotate(pygame_image, -angel)
    new_rect = image_rotated.get_rect(center=pygame_rect.center)
    window.fill(YELLOW)
    window.blit(image_rotated, new_rect)

    for b in bullets:
        b[0] += b[2]
        b[1] += b[3]
        
    for b in bullets:
        window.blit(bullet_image, (b[0], b[1]))
    
    pygame.display.flip()






