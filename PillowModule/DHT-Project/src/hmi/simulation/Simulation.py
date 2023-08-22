import pygame, sys
from PIL import Image
from templates.Base import FRAME_WIDTH, FRAME_HEIGHT
from HMI_Screen import HMIScreen
from test_use_pygame.Control import Control
    
def main():
    pygame.init()
    win = pygame.display.set_mode((FRAME_WIDTH + 310, FRAME_HEIGHT))
    clock = pygame.time.Clock()
    control = Control(win)
    hmi_screen = HMIScreen()
    shift = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                control.check_key_down(event)
                if event.key == pygame.K_RETURN:
                    hmi_screen.event_handling("enter")
                    # image = get_image(hmi_screen.get_screen())
                elif event.key == pygame.K_DOWN:
                    hmi_screen.event_handling("down")
                    # image = get_image(hmi_screen.get_screen())
                elif event.key == pygame.K_UP:
                    hmi_screen.event_handling("up")
                    # image = get_image(hmi_screen.get_screen())
                elif event.key == pygame.K_LEFT:
                    hmi_screen.event_handling("left")
                    # image = get_image(hmi_screen.get_screen())
                elif event.key == pygame.K_RIGHT:
                    hmi_screen.event_handling("right")
                    # image = get_image(hmi_screen.get_screen())
                elif event.key == pygame.K_BACKSPACE:
                    hmi_screen.event_handling("delete")
                    # image = get_image(hmi_screen.get_screen())
                elif event.key == pygame.K_F1:
                    hmi_screen.event_handling("f1")
                elif event.key == pygame.K_F2:
                    hmi_screen.event_handling("f2")
                elif event.key == pygame.K_F3:
                    hmi_screen.event_handling("f3")
                elif event.key == pygame.K_F4:
                    hmi_screen.event_handling("f4")
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift = True
                elif shift:
                    # print(type(event.unicode))
                    hmi_screen.event_handling(event.unicode)
                else:
                    # print(type(event.unicode))
                    hmi_screen.event_handling(event.unicode)
                    
            elif event.type == pygame.KEYUP:
                control.check_key_up()
            #     if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            #         shift = False
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RETURN]:
        #     hmi_screen.event_handling("enter")
        #     # image = get_image(hmi_screen.get_screen())
        # elif keys[pygame.K_DOWN]:
        #     hmi_screen.event_handling("down")
        #     # image = get_image(hmi_screen.get_screen())
        # elif keys[pygame.K_UP]:
        #     hmi_screen.event_handling("up")
        #     # image = get_image(hmi_screen.get_screen())
        # elif keys[pygame.K_LEFT]:
        #     hmi_screen.event_handling("left")
        #     # image = get_image(hmi_screen.get_screen())
        # elif keys[pygame.K_RIGHT]:
        #     hmi_screen.event_handling("right")
        #     # image = get_image(hmi_screen.get_screen())
        # elif keys[pygame.K_BACKSPACE]:
        #     hmi_screen.event_handling("delete")
        #     # image = get_image(hmi_screen.get_screen())
        # elif keys[pygame.K_F1]:
        #     hmi_screen.event_handling("f1")
        # elif keys[pygame.K_F2]:
        #     hmi_screen.event_handling("f2")
        # elif keys[pygame.K_F3]:
        #     hmi_screen.event_handling("f3")
        # elif keys[pygame.K_F4]:
        #     hmi_screen.event_handling("f4")

        image = get_image(hmi_screen.get_screen())
        win.fill((255, 255, 255))
        win.blit(image, (0, 0))

        control.draw(FRAME_WIDTH + 10, 0)

        pygame.display.update()
        clock.tick(30)

def get_image(image):
    # pygame.image.frombuffer()
    return pygame.image.frombuffer(image.tobytes(), (FRAME_WIDTH, FRAME_HEIGHT), "RGB")

if __name__ == "__main__":
    main()