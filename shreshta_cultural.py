from PIL import Image, ImageDraw, ImageFont
import csv
import time

start = time.time()



def create_image(name, dept, prize,house, event):
    with Image.open("./Cult.png").convert("RGBA") as base:
        W, H = base.size
        txt = Image.new("RGBA", base.size, (255, 255, 255, 1))
        
        fnt = ImageFont.truetype("gillsan.ttf", 400)
        fnt1 = ImageFont.truetype("gillsan.ttf", 130)
        
        _,_,w,h = fnt.getbbox(name)
        d = ImageDraw.Draw(txt)

        d.text(((W-w)/2,(H-h)/2), name, font=fnt, fill="white")
        w,h = fnt1.getsize(prize.upper());
        d.text(((W-w)/2-150, 2995), prize.upper(), font=fnt1, fill=(255, 255, 255, 255))
        w,h = fnt1.getsize(event.upper());
        d.text(((W-w)/2,3190), event.upper(), font=fnt1, fill=(250, 101, 106, 255))
        
        
        out = Image.alpha_composite(base, txt)
        out.save(fp=f"./output_sh_cult/{name}.png", format="PNG", compress_level=1)



# create_image("HariY", "S4 CSAI", "First","Green", "ENGLISH HINDI (GROUP)")

create_image("Vyshnav D Kumarayil", "S4 CSE A", "SECOND" , "RED", "PITCH PERFECT")
end = time.time()
print(f"{end - start}s")
        