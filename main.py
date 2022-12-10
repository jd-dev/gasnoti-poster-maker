import json
import sys
import os
import time
from PIL import Image, ImageDraw, ImageFont 

TODAY_X = 420
TOMORROW_X = 640
DIFF_X = 900
COLOR_RED = "#E82900"
COLOR_GREEN = "#34CB46"
position_y = {
    "gasohol_95": 330,
    "gasohol_91": 440,
    "gasohol_e20": 550,
    "gasohol_e85": 660,
    "diesel_b7": 770,
    "diesel_b20": 880,
}

class myTemplate(): 
    def __init__(self, name, description, prices):
        self.name=name #Saves Name input as a self object
        self.description=description #Saves Description input as a self object
        self.prices = prices
    def draw(self):        
        self.prices.sort(key=lambda a: a['rank'])
        
        img = Image.open("template_new.jpg", 'r').convert('RGB') #Opens Template Image
        font_path = "./assets/fonts/NotoSansThai-Bold.ttf"
        font = ImageFont.truetype(font_path, 60)
        imgdraw=ImageDraw.Draw(img)

        for price in self.prices:
            name = price["name"]
            indicator = price["indicator"]
            y_index = position_y[name]
            imgdraw.text((TODAY_X, y_index), 
                     price['today'], 
                     font=font,
                     fill=(0))
            imgdraw.text((TOMORROW_X, y_index),
                        price['tomorrow'], 
                        font=font,
                        fill=(0))
            if indicator:
                imgdraw.text((DIFF_X, y_index),
                            price['diff'], 
                            font=font,
                            fill=(COLOR_RED if indicator > 0 else COLOR_GREEN))
                
        file_name = str(time.time())
        img.save("./out/poster.png".format(file_name))

prices = []
payload_file  = "./payload.json"
if not os.path.exists(payload_file):
    sys.exit("payload not found")
with open('./payload.json', 'r') as f:
    raw = json.load(f)
    print(raw)
    prices = raw['data']['prices']
template=myTemplate('Hello, world!', 'Hi there', prices)
template.draw()