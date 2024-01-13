from perlin_noise import PerlinNoise
from ursina import Button, color, scene

def create_chunk(size, ground_depth, noise, position=(0, 0, 0)):
    boxes = []
    for x in range(size):
        for z in range(size):
            y = int(noise([(x + position[0]) / (size * 10), (z + position[2]) / (size * 10)]) * 10) + ground_depth
            for i in range(y - ground_depth, y):
                box = Button(color=color.white, model='cube', position=(x + position[0], i, z + position[2]), texture='textures/grass.png', parent=scene, origin_y=0.5, collider='mesh')
                boxes.append(box)
                
    return boxes


