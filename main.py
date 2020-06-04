import pygame

pygame.init()
print("Welcome to tic tac toe")
screen = pygame.display.set_mode((300, 400))
lines = pygame.image.load("Untitled.png")
circle = pygame.image.load("circle.png")
cross = pygame.image.load("cross.png")

# making every block condition false
cr_first_block = False
ci_first_block = False
cr_second_block = False
ci_second_block = False
cr_third_block = False
ci_third_block = False
cr_4th_block = False
ci_4th_block = False
cr_5th_block = False
ci_5th_block = False
cr_6th_block = False
ci_6th_block = False
cr_7th_block = False
ci_7th_block = False
cr_8th_block = False
ci_8th_block = False
cr_9th_block = False
ci_9th_block = False


def which_fun():
    return True


i = 0
runn = True
while runn:
    screen.fill((255, 255, 255))
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        runn = False
    if event.type == pygame.MOUSEBUTTONDOWN:  # checks if mouse button clicked
        if event.button == 1:  # mouse button 1 clicked
            # print("button 1 pressed")
            if event.pos[0] < 100 and event.pos[1] < 133 and all([cr_first_block == False, ci_first_block == False]):
                if i % 2 == 0:
                    cr_first_block = which_fun()
                    i += 1
                else:
                    ci_first_block = which_fun()
                    i += 1
            if event.pos[0] in range(100, 200) and event.pos[1] < 133 and all(
                    [cr_second_block == False, ci_second_block == False]):
                if i % 2 == 0:
                    cr_second_block = which_fun()
                    i += 1
                else:
                    ci_second_block = which_fun()
                    i += 1
            if event.pos[0] in range(200, 300) and event.pos[1] in range(0, 133) and all(
                    [cr_third_block == False, ci_third_block == False]):
                if i % 2 == 0:
                    cr_third_block = which_fun()
                    i += 1
                else:
                    ci_third_block = which_fun()
                    i += 1
            if event.pos[0] in range(0, 100) and event.pos[1] in range(133, 266) and all(
                    [cr_4th_block == False, ci_4th_block == False]):
                if i % 2 == 0:
                    cr_4th_block = which_fun()
                    i += 1
                else:
                    ci_4th_block = which_fun()
                    i += 1
            if event.pos[0] in range(100, 200) and event.pos[1] in range(133, 266) and all(
                    [cr_5th_block == False, ci_5th_block == False]):
                if i % 2 == 0:
                    cr_5th_block = which_fun()
                    i += 1
                else:
                    ci_5th_block = which_fun()
                    i += 1
            if event.pos[0] in range(200, 300) and event.pos[1] in range(133, 266) and all(
                    [cr_6th_block == False, ci_6th_block == False]):
                if i % 2 == 0:
                    cr_6th_block = which_fun()
                    i += 1
                else:
                    ci_6th_block = which_fun()
                    i += 1
            if event.pos[0] in range(0, 100) and event.pos[1] in range(266, 400) and all(
                    [cr_7th_block == False, ci_7th_block == False]):
                if i % 2 == 0:
                    cr_7th_block = which_fun()
                    i += 1
                else:
                    ci_7th_block = which_fun()
                    i += 1
            if event.pos[0] in range(100, 200) and event.pos[1] in range(266, 400) and all(
                    [cr_8th_block == False, ci_8th_block == False]):
                if i % 2 == 0:
                    cr_8th_block = which_fun()
                    i += 1
                else:
                    ci_8th_block = which_fun()
                    i += 1
            if event.pos[0] in range(200, 300) and event.pos[1] in range(266, 400) and all(
                    [cr_9th_block == False, ci_9th_block == False]):
                if i % 2 == 0:
                    cr_9th_block = which_fun()
                    i += 1
                else:
                    ci_9th_block = which_fun()
                    i += 1

    if cr_first_block:
        screen.blit(cross, (0, 0))
    if ci_first_block:
        screen.blit(circle, (0, 0))
    if cr_second_block:
        screen.blit(cross, (100, 0))
    if ci_second_block:
        screen.blit(circle, (100, 0))
    if cr_third_block:
        screen.blit(cross, (200, 0))
    if ci_third_block:
        screen.blit(circle, (200, 0))
    if cr_4th_block:
        screen.blit(cross, (0, 133))
    if ci_4th_block:
        screen.blit(circle, (0, 133))
    if cr_5th_block:
        screen.blit(cross, (100, 133))
    if ci_5th_block:
        screen.blit(circle, (100, 133))
    if cr_6th_block:
        screen.blit(cross, (200, 133))
    if ci_6th_block:
        screen.blit(circle, (200, 133))
    if cr_7th_block:
        screen.blit(cross, (0, 266))
    if ci_7th_block:
        screen.blit(circle, (0, 266))
    if cr_8th_block:
        screen.blit(cross, (100, 266))
    if ci_8th_block:
        screen.blit(circle, (100, 266))
    if cr_9th_block:
        screen.blit(cross, (200, 266))
    if ci_9th_block:
        screen.blit(circle, (200, 266))
    screen.blit(lines, (0, 0))
    if all([ci_9th_block, ci_5th_block, ci_first_block]) or all([cr_9th_block, cr_5th_block, cr_first_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(0, 0), (300, 400)], 10)
    if all([ci_third_block, ci_5th_block, ci_7th_block]) or all([cr_third_block, cr_5th_block, cr_7th_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(300, 0), (0, 400)], 10)
    if all([ci_third_block, ci_second_block, ci_first_block]) or all([cr_third_block, cr_second_block, cr_first_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(0, 66), (300, 67)], 10)
    if all([ci_4th_block, ci_5th_block, ci_6th_block]) or all([cr_4th_block, cr_5th_block, cr_6th_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(0, 200), (300, 201)], 10)
    if all([ci_7th_block, ci_8th_block, ci_9th_block]) or all([cr_7th_block, cr_8th_block, cr_9th_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(0, 333), (300, 334)], 10)
    if all([ci_third_block, ci_6th_block, ci_9th_block]) or all([cr_third_block, cr_6th_block, cr_9th_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(250, 0), (250, 400)], 10)
    if all([ci_4th_block, ci_7th_block, ci_first_block]) or all([cr_4th_block, cr_7th_block, cr_first_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(50, 0), (50, 400)], 10)
    if all([ci_5th_block, ci_8th_block, ci_second_block]) or all([cr_5th_block, cr_8th_block, cr_second_block]):
        pygame.draw.lines(screen, [0, 0, 0], True, [(150, 0), (150, 400)], 10)

    pygame.display.update()
