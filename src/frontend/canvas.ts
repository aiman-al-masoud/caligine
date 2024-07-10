import type { Sprite } from "./types"


export class Canvas {

    readonly ctx: CanvasRenderingContext2D
    readonly spriteData: { [name: string]: Sprite } = {}
    protected bgColor: string = 'red'

    constructor(readonly canvas: HTMLCanvasElement) {
        this.ctx = canvas.getContext('2d')!
    }

    setWidth(width: number) {
        this.canvas.width = width
    }

    setHeght(height: number) {
        this.canvas.height = height
    }

    drawSprite(sprite: Sprite) {

        const {x:xOld, y:yOld} = this.spriteData[sprite.name] ?? {x:0, y:0}
        this.spriteData[sprite.name] = {...this.spriteData[sprite.name], ...sprite}

        const { image_base64 } = this.spriteData[sprite.name]

        const image = new Image()
        image.src = image_base64

        this.ctx.clearRect(xOld, yOld, image.width, image.height)
        this.ctx.drawImage(image, sprite.x, sprite.y)
        this.spriteData[sprite.name].x = sprite.x
        this.spriteData[sprite.name].y = sprite.y
    }

    setBgColor(color: string) {
        this.bgColor = color
    }

}

