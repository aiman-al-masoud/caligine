from dataclasses import dataclass
from typing import Dict
from core.Ast import Ast
from typing import TYPE_CHECKING, Dict
from canvas import Canvas
from typing import TYPE_CHECKING
from core.Num import Num


from core.Str import Str
if TYPE_CHECKING:
    from core.World import World

@dataclass
class Object(Ast):
    name:str
    props: Dict[str, Ast]

    def execute(self, world: 'World') -> 'Ast':

        if not world.has_obj(self.name):
            world.add_obj(self)
            
        return self

    def subst(self, d: Dict['Ast', 'Ast']) -> 'Ast':
        return Object(self.name, {k:v.subst(d) for k,v in self.props.items()})

    def get(self, key: str) -> 'Ast':
        from core.Bool import Bool
        return self.props.get(key, Bool(False))

    def set(self, key: str, value: 'Ast'):
        self.props[key] = value

    def is_drawable(self):
        return 'image' in self.props

    def draw(self, canvas: Canvas):

        if not self.is_drawable():
            return

        path = self.get('image')
        x = self.get('pos_x')
        y = self.get('pos_y')

        assert isinstance(path, Str)
        assert isinstance(x, Num)
        assert isinstance(y, Num)

        canvas.draw_image(path.value, int(x), int(y))

    def is_within_bounding_box(self, x_left:int, y_top:int, width:int, height:int):

        if not self.is_drawable():
            return

        x_right = x_left + width
        y_bottom = y_top + height

        x = int(self.get('pos_x'))
        y = int(self.get('pos_y'))

        return x_left < x < x_right and y_top < y < y_bottom

