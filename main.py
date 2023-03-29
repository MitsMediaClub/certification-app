from PIL import Image, ImageDraw, ImageFont
import csv

def create_image(name, dept, prize,house, event):
    with Image.open("./varnam_template.png").convert("RGBA") as base:
        W, H = base.size
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        
        fnt = ImageFont.truetype("gillsan.ttf", 400)
        fnt1 = ImageFont.truetype("gillsan.ttf", 150)
        
        _,_,w,h = fnt.getbbox(name)
        d = ImageDraw.Draw(txt)

        d.text(((W-w)/2,(H-h-150)/2), name, font=fnt, fill="black")
        
        d.text((2045, 2945), dept, font=fnt1, fill=(0, 0, 0, 255))
        d.text((3584, 2954), prize, font=fnt1, fill=(0, 0, 0, 255))
        d.text(((W-w)/2-250,(H-h+1800)/2), event, font=fnt1, fill=(215, 25, 32, 255))
        
        
        out = Image.alpha_composite(base, txt)
        out.save(fp=f"./output/{name}.png", format="PNG")



create_image("HariY", "S4 CSAI", "First", "ENGLISH HINDI (GROUP)")


with open ("./varnam.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        create_image(row[0], row[1], row[2], row[3], row[4])
        