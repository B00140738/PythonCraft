from ursina import Button, color, scene

def create_chunk(size):
    boxes = []
    for x in range(size):
        for y in range(0, -size, -1):
            for z in range(size):
                box = Button(color=color.white, model='cube', position=(x, y, z), texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(box)
    return boxes


