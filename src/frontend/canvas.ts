import type { Sprite } from "./types"


export class Canvas {

    readonly ctx: CanvasRenderingContext2D

    readonly imageData: {[name:string]:HTMLImageElement} = {}
    protected bgColor: string = ''

    constructor(readonly canvas: HTMLCanvasElement) {
        this.ctx = canvas.getContext('2d')!
    }

    setWidth(width: number) {

        if (width===this.canvas.width) return
        this.canvas.width = width
    }

    setHeght(height: number) {

        if (height===this.canvas.height) return
        this.canvas.height = height
    }

    setBgColor(color: string) {

        if (this.bgColor===color) return 
        this.ctx.fillStyle = color
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
    }

    reDrawAll(sprites:Sprite[]){
   
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
        sprites.forEach(s=>{

            if (s.image_base64){
                const image = new Image()
                image.src = s.image_base64
                this.imageData[s.name] = image
            }

            if (!this.imageData[s.name]) return

            this.ctx.drawImage(this.imageData[s.name], s.x, s.y)
        })
    }
}
