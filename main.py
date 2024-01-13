from perlin_noise import PerlinNoise
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from terrain.create_chunk import create_chunk

app = Ursina()
player = FirstPersonController()
Sky()

noise = PerlinNoise(octaves=2, seed=1)

chunk_size = 8
ground_depth = 8
world_size = 2

chunks = []

# Generate chunks and store them in the 'chunks' list
for i in range(world_size):
    for j in range(world_size):
        chunk = create_chunk(chunk_size, ground_depth, noise, position=(i * chunk_size, 0, j * chunk_size))
        chunks.extend(chunk)


def input(key):
    for box in chunks:
        if box.hovered:
            if key == 'right mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal, texture='textures/grass.png', parent=scene, origin_y=0.5, collider='mesh')
                chunks.append(new)

            if key == 'left mouse down':
                chunks.remove(box)
                destroy(box)

app.run()
