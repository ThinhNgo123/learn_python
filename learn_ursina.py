from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# from ursina.camera import camera

app = Ursina()
window.vsync = False
entity = Entity(
    model='cube', 
    collider='box', 
    texture='shore', 
    color=color.white,
    scale=(100, 1, 100))
player = FirstPersonController(y=2, origin_y=-.5)
# player.add_script()
app.run()