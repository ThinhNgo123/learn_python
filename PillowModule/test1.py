from PIL import Image, ImageDraw, ImageFont

# img = Image.open("Sample.png")
# img_rotate = img.rotate(180)
# img_crop = img.crop((0, 0, 200, 200))
# scale_refactor = 0.5
# WIDTH = 0
# HEIGHT = 1
# img_resize = img.resize((int(img.size[WIDTH] * scale_refactor), int(img.size[HEIGHT] * scale_refactor)))
# img_transpose_left = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# img_transpose_up = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# img_list = [img, img_rotate, img_crop, img_resize, img_transpose_left, img_transpose_up]

# number = 5
# img_list[number].show()
# 
image = Image.new("RGB", (400, 400), color=(255, 255, 255))
image_1 = Image.new("RGB", (50, 50), color=(255, 0, 0))
draw = ImageDraw.Draw(image)
draw.rounded_rectangle(((50, 50), (200, 300)), fill=(0, 0, 0), outline=(255, 0, 0), width=5, radius=5)
image.paste(image_1, (30, 50))#, mask=image)
draw.text((100, 100.5), "hello", (233, 216, 166), ImageFont.truetype("./project/Font/DejaVuSans/DejaVuSans-Bold.ttf", 24))
image.show()