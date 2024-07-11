import base64
from dataclasses import dataclass
from io import BytesIO
from typing import TYPE_CHECKING, Optional, TypedDict
from PIL import Image
from core.Object import Object
from core.Num import Num

if TYPE_CHECKING:
    from core.World import World
    from core.Ast import Ast

@dataclass
class Sprite(Object):

    def execute(self, world: 'World') -> 'Ast':

        if not self.has('pos_x'):
            raise Exception()

        if not self.has('pos_y'):
            raise Exception()
        
        if not self.has('image'):
            raise Exception()

        if not self.has('repeat_x'):
            self.set('repeat_x', Num(1))

        if not self.has('repeat_y'):
            self.set('repeat_y', Num(1))

        self.image = Image.open(str(self.get('image')))
        
        return self

    def to_json(self,  include_image:bool=False, offset_x:int=0, offset_y:int=0)->'SpriteJson':

        x = int(self.get('pos_x')) - offset_x
        y = int(self.get('pos_y')) - offset_y

        repeat_x = int(self.get('repeat_x'))
        repeat_y = int(self.get('repeat_y'))

        return {
            'name': self.name,
            'x': x,
            'y': y,
            'repeat_x': repeat_x,
            'repeat_y': repeat_y,
            'image_base64': self.image_base64() if include_image else None
        }

    def image_base64(self)->str:

        buffered = BytesIO()
        self.image.save(buffered, format='png', optimize=True, quality=10)
        out = base64.b64encode(buffered.getvalue()).decode('utf-8')
        out = 'data:image/png;base64,' + out
        return out
    
    def get(self, key: 'str|Ast', default: 'Ast|None' = None) -> 'Ast':
        
        if str(key) == 'width':
            return Num(self.image.width * int(self.get('repeat_y')))

        if str(key) == 'height':
            return Num(self.image.height * int(self.get('repeat_x')))

        return super().get(key, default)


class SpriteJson(TypedDict):
    name:str
    x:int
    y:int
    repeat_x:int
    repeat_y:int
    image_base64:Optional[str]
