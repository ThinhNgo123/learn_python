import iso
import assets
from vectors import vec3

class Test:

    def __init__(self, game):
        self.view = game.view
        self.window = game.window

    # Abstract method that is run upon initialization of the game:
    def onInit(self):
        pass


class TestIso(Test):

    def onInit(self):
        pass
        #image = assets.loadImage("assets/terrain.png")
        #sprite = Sprite(image)
        #self.view.addSprite(sprite)

        # for y in range(10):
        #     for x in range(10):
        #         center_blob = assets.load_image("assets/test/blob.png")
        #         center_spr = iso.Sprite(center_blob)
        #         loc = vec3(x, y, 0)
        #         center_spr.set_location(loc)
        #         center_spr.set_layer(10)
        #         self.view.add_sprite(center_spr)




