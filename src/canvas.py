from PIL import Image

class Canvas:

    def __init__(self, width:int, height:int, color_bg:str) -> None:

        self.rendered = Image.new('RGB', (width, height), color=color_bg)
        self.cache = {}

    def draw_image(self, image_path:str, x:int, y:int):

        if image_path not in self.cache:
            self.cache[image_path] = Image.open(image_path)

        image = self.cache[image_path]
        self.rendered.paste(image, (x, y), image)
    
    def get_rendered(self):

        return self.rendered


