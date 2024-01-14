from perlin_noise import PerlinNoise
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from terrain.create_chunk import create_chunk

app = Ursina()
player = FirstPersonController()
player.y = 10
Sky()

#TODO: Keep settings as 4, 2? higher amplitude = more reakistic terrain?
noise = PerlinNoise(octaves=4, seed=2)

chunk_size = 6
ground_depth = 6
world_size = 3

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
