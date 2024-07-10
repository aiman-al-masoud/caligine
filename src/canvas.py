import base64
from io import BytesIO
from PIL import Image

class Canvas:

    def __init__(self, width:int, height:int, color_bg:str) -> None:

        self.rendered = Image.new('RGB', (width, height), color=color_bg)
        self.cache = {}
        self.center_x = 0
        self.center_y = 0
        self.width = width
        self.height = height
    
    def set_center(self, center_x:int, center_y:int):

        self.center_x = center_x
        self.center_y = center_y

    def draw_image(self, image_path:str, x:int, y:int):

        if image_path not in self.cache:
            self.cache[image_path] = Image.open(image_path)

        image = self.cache[image_path]
        self.rendered.paste(image, (x - (self.center_x - self.width//2), y - (self.center_y - self.height//2)), image)
    
    def get_rendered(self):

        return self.rendered

    def get_base64(self):

        buffered = BytesIO()
        self.rendered.save(buffered, format="png", optimize=True, quality=10)
        out = base64.b64encode(buffered.getvalue()).decode('utf-8')
        out = 'data:image/png;base64,' + out
        return out


