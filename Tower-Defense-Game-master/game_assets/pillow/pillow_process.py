from PIL import ImageDraw, Image

bg = Image.open("./pngtree-game-button-set-yellow-png-png-image_5996878.jpg")
# bg = Image.open("../Tower-Defense-2D-Game-Kit27.png")
# bg = bg.crop((1000, 20, 1440, 600))
# colors = []
for width in range(bg.width):
    # row = []
    for height in range(bg.height):
        pixel = bg.getpixel((width, height))
        if pixel == (255, 255, 255):
            # row.append()
            bg.putpixel((width, height), (0, 255, 0))
    # colors.append(row)
# print(size)
bg.show()
# bg.save("../bg.png")