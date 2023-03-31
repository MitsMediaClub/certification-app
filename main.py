from PIL import Image, ImageDraw, ImageFont
import csv
import time

start = time.time()



def create_image(name, dept, prize,house, event):
    with Image.open("./varnam_template.png").convert("RGBA") as base:
        W, H = base.size
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        
        fnt = ImageFont.truetype("gillsan.ttf", 400)
        fnt1 = ImageFont.truetype("gillsan.ttf", 150)
        
        _,_,w,h = fnt.getbbox(name)
        d = ImageDraw.Draw(txt)

        d.text(((W-w)/2,(H-h)/2), name, font=fnt, fill="black")
        
        d.text((1900, 2945), dept.upper(), font=fnt1, fill=(0, 0, 0, 255))
        d.text((3584, 2954), prize.upper(), font=fnt1, fill=(0, 0, 0, 255))
        d.text(((W-w)/2+400,3190), event, font=fnt1, fill=(215, 25, 32, 255))
        d.text(((W-w)/2+500,3370), f"{house} house".upper(), font=fnt1, fill=(0, 0, 0, 255))
        
        
        out = Image.alpha_composite(base, txt)
        out.save(fp=f"./output/{name}.png", format="PNG", compress_level=1)



# create_image("HariY", "S4 CSAI", "First","Green", "ENGLISH HINDI (GROUP)")


with open ("details.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        create_image(row[0], row[1], row[2], row[3], row[4])
        end = time.time()
        print(f"{end - start}s")
        