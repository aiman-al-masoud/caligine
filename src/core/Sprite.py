import base64
from dataclasses import dataclass
from io import BytesIO
from typing import Optional, TypedDict
from PIL import Image
from core.Object import Object

@dataclass
class Sprite(Object):
    
    def to_json(self,  include_image:bool=False, offset_x:int=0, offset_y:int=0)->'SpriteJson':

        x = int(self.get('pos_x')) - offset_x
        y = int(self.get('pos_y')) - offset_y

        return {
            'name': self.name,
            'x': x,
            'y': y,
            'image_base64': self.image_base64() if include_image else None
        }

    def image_base64(self)->str:

        image = Image.open(str(self.get('image')))
        buffered = BytesIO()
        image.save(buffered, format='png', optimize=True, quality=10)
        out = base64.b64encode(buffered.getvalue()).decode('utf-8')
        out = 'data:image/png;base64,' + out
        return out


class SpriteJson(TypedDict):
    name:str
    x:int
    y:int
    image_base64:Optional[str]
