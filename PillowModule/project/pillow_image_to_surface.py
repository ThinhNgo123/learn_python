import pygame, sys
from PIL import Image
from templates.Base import FRAME_WIDTH, FRAME_HEIGHT
from templates.Menu import Menu
from frame_Menu_Sensor import FrameMenuSensor 
from test_use_pygame.Control import Control
    
def main():
    global frame_sensor
    pygame.init()
    win = pygame.display.set_mode((FRAME_WIDTH + 310, FRAME_HEIGHT))
    clock = pygame.time.Clock()
    control = Control(win)
    frame_sensor = FrameMenuSensor("rt")
    for i in range(20):
        frame_sensor.add_menu_element(f"Sensor {i+1}")
    texts = [
        ("hdkhd", "dkjhd", "djhdh"), 
        ("djhd", "12:34", "hello"), 
        ("192.168.1.123", "12:00", "world")]
    i = 0
    image_surface = get_image(texts[i][0], texts[i][1], texts[i][2])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                control.check_key_down(event)

                if event.key == pygame.K_RETURN:
                    i = (i + 1) % len(texts)
                    image_surface = get_image(texts[i][0], texts[i][1], texts[i][2])
                elif event.key == pygame.K_RIGHT:
                    frame_sensor.event_handling("right")
                elif event.key == pygame.K_DOWN:
                    frame_sensor.event_handling("down")
                    image_surface = get_image(texts[i][0], texts[i][1], texts[i][2])
                elif event.key == pygame.K_UP:
                    frame_sensor.event_handling("up")
                    image_surface = get_image(texts[i][0], texts[i][1], texts[i][2])
                
            elif event.type == pygame.KEYUP:
                control.check_key_up()
        
        win.fill((255, 255, 255))
        win.blit(image_surface, (0, 0))

        control.draw(FRAME_WIDTH + 10,0)

        pygame.display.update()
        clock.tick(30)

def get_image(ip, time, content):
    frame_sensor.layout.set_time(time)
    frame_sensor.layout.set_ip(ip)
    frame_sensor.layout.set_content(content)
    return pygame.image.fromstring(frame_sensor.to_bytes(), (FRAME_WIDTH, FRAME_HEIGHT), "RGB")

if __name__ == "__main__":
    main()