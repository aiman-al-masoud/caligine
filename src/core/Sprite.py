import base64
from dataclasses import dataclass
from io import BytesIO
import os
from typing import TYPE_CHECKING, Optional, TypedDict
from PIL import Image
from core.Object import Object
from core.Num import Num
from core.Str import Str

if TYPE_CHECKING:
    from core.World import World
    from core.Ast import Ast

@dataclass(kw_only=True)
class Sprite(Object):

    def init(self, world: 'World')->'Ast':

        from core.Halt import Halt        

        if not self.has('pos_x'):
            raise Halt(self, 'sprite must have a "pos_x"')

        if not self.has('pos_y'):
            raise Halt(self, 'sprite must have a "pos_y"')
        
        if not self.has('image'):
            raise Halt(self, 'sprite must have an "image"')

        if not self.has('repeat_cols'):
            self.set('repeat_cols', Num(value=1))

        if not self.has('repeat_rows'):
            self.set('repeat_rows', Num(value=1))

        self.set('type', Str(value='sprite'))
        self.load_image(world)
        return self

    def to_json(self,  include_image:bool=False, offset_x:int=0, offset_y:int=0)->'SpriteJson':

        x = int(self.get('pos_x')) - offset_x
        y = int(self.get('pos_y')) - offset_y

        repeat_cols = int(self.get('repeat_cols'))
        repeat_rows = int(self.get('repeat_rows'))

        return {
            'name': self.get_name(),
            'x': x,
            'y': y,
            'repeat_cols': repeat_cols,
            'repeat_rows': repeat_rows,
            'image_base64': self.image_base64() if include_image else None,
        }

    def image_base64(self)->str:

        buffered = BytesIO()
        self.image.save(buffered, format='png', optimize=True, quality=10)
        out = base64.b64encode(buffered.getvalue()).decode('utf-8')
        out = 'data:image/png;base64,' + out
        return out
    
    def get(self, key: 'str|Ast', default: 'Ast|None' = None) -> 'Ast':
        
        if str(key) == 'width':
            return Num(value=self.image.width * int(self.get('repeat_rows')))

        if str(key) == 'height':
            return Num(value=self.image.height * int(self.get('repeat_cols')))

        if str(key) == 'right_x':
            return self.get('pos_x').perform_op('+', self.get('width'))

        if str(key) == 'bottom_y':
            return self.get('pos_y').perform_op('+', self.get('height'))

        return super().get(key, default)
    
    def load_image(self, world:'World'):

        path_script = str(world.get('path_script'))
        path_img_rel = str(self.get('image'))
        path_folder = os.path.split(path_script)[0]
        path_img_abs = os.path.join(path_folder, path_img_rel)
        path_img_abs = os.path.abspath(path_img_abs)
        self.image = Image.open(path_img_abs)
    
    def __str__(self) -> str:
        return f'sprite{{name={self.get_name()}}}'


class SpriteJson(TypedDict):
    name:str
    x:int
    y:int
    repeat_cols:int
    repeat_rows:int
    image_base64:Optional[str]
