import pygame

def Button(screen, positionX, positionY, text):
        screen = screen
        font = pygame.font.SysFont("Arial", 30)
        text_render = font.render(text, 1, (0, 0, 0))
        x, y, w , h = text_render.get_rect()
        x = positionX
        y = positionY
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(screen, (200, 210, 220), (x, y, w , h))
        return screen.blit(text_render, (x, y))

def EnemyTextBox(screen, positionX, positionY, text):
        screen = screen
        font = pygame.font.SysFont("Arial", 35)
        text_render = font.render(text, 1, (0, 0, 0))
        x, y, w , h = text_render.get_rect()
        x = positionX - w * 1.2
        y = positionY
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(screen, (210, 225, 254), (x, y, w , h))
        return screen.blit(text_render, (x, y))

def button1():
    print("Button1")

def button2():
    print("Button2")

def button3():
    print("Button3")

def button4():
    print("Button4")
