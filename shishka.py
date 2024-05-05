import  pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 0






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill("black")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3

    pygame.draw.rect(win, "blue" , (x, 450, 50, 10))

    pygame.draw.circle(win, "red", )






    pygame.time.delay(15)
    pygame.display.update()


