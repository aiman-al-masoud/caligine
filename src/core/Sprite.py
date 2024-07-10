from dataclasses import dataclass
from canvas import Canvas
from core.Object import Object

@dataclass
class Sprite(Object):

    def draw(self, canvas: Canvas):

        path = str(self.get('image'))
        x = int(self.get('pos_x'))
        y = int(self.get('pos_y'))

        canvas.draw_image(path, int(x), int(y))
