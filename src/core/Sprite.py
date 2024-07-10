import base64
from dataclasses import dataclass
from io import BytesIO
from PIL import Image
from core.Object import Object

@dataclass
class Sprite(Object):

    # def draw(self, canvas: Canvas):

    #     path = str(self.get('image'))
    #     x = int(self.get('pos_x'))
    #     y = int(self.get('pos_y'))

    #     canvas.draw_image(path, int(x), int(y))
    
    def to_json(self,  include_image:bool=False, center_x:int=0, center_y:int=0, canvas_width:int = 0, canvas_height:int = 0):

        x = int(self.get('pos_x'))
        y = int(self.get('pos_y'))

        x = x - (center_x - canvas_width//2)
        y = y - (center_y - canvas_height//2)

        return {
            'name': self.name,
            'x': x,
            'y': y,
            **({'image_base64': self.image_base64()} if include_image else {}),
        }

    def image_base64(self)->str:

        image = Image.open(str(self.get('image')))
        buffered = BytesIO()
        image.save(buffered, format='png', optimize=True, quality=10)
        out = base64.b64encode(buffered.getvalue()).decode('utf-8')
        out = 'data:image/png;base64,' + out
        return out

