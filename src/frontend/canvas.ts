import type { Sprite } from "./types"


export class Canvas {

    readonly ctx: CanvasRenderingContext2D
    readonly imageData: { [name: string]: HTMLImageElement } = {}
    protected bgColor: string = ''

    constructor(readonly canvas: HTMLCanvasElement) {
        this.ctx = canvas.getContext('2d')!
    }

    setWidth(width: number) {

        if (width === this.canvas.width) return
        this.canvas.width = width
    }

    setHeght(height: number) {

        if (height === this.canvas.height) return
        this.canvas.height = height
    }

    setBgColor(color: string) {

        if (this.bgColor === color) return
        this.ctx.fillStyle = color
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
    }

    reDrawAll(sprites: Sprite[]) {

        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
        sprites.forEach(s => {
            this.draw(s)
        })
    }

    draw(s: Sprite) {

        if (s.image_base64) {
            const image = new Image()
            image.src = s.image_base64
            this.imageData[s.name] = image
        }

        const image = this.imageData[s.name]
        if (!image) return

        let pos = { x: s.x, y: s.y }

        for (let i = 0; i < s.repeat_x; i++) {
            for (let j = 0; j < s.repeat_y; j++) {
                this.ctx.drawImage(image, pos.x, pos.y)
                pos.x += image.width
            }
            pos.x = s.x
            pos.y += image.height
        }
    }
}
