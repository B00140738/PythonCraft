from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from terrain.create_chunk import create_chunk

app = Ursina()
player = FirstPersonController()
Sky()

chunk_size = 8

# Call the create_chunk function from create_chunk.py
boxes = create_chunk(chunk_size)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'right mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal, texture='textures/grass.png', parent=scene, origin_y=0.5)
                boxes.append(new)

            if key == 'left mouse down':
                boxes.remove(box)
                destroy(box)

app.run()
