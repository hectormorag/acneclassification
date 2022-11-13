# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:29:03 2022

@author: 52551
"""

from PIL import Image
import os
from tqdm import tqdm
import random


def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)

for k in range(0,5):
    
    for f in tqdm(os.listdir(r"C:\Users\52551\Desktop\assignment acne severity classification\assignment acne severity classification\imagesdata1\data\400 Healthy")):
        
        if f.endswith('.jpg'):
            i=Image.open(f)
            fn,fext=os.path.splitext(f)
            if random.choice([0,1])==0:
                i = zoom_at(i.rotate(random.choice([0, 5, -5, 10, -10, 30, -30, 45, -45])).transpose(Image.FLIP_LEFT_RIGHT), round(random.uniform(62,189)),round(random.uniform(62,189)),random.uniform(1.3,1.6))
                i.save(r"C:/Users/52551/Desktop/assignment acne severity classification/assignment acne severity classification/imagesdata1/data/healthy/{}_{}".format(k,fn))
            else:
                i = zoom_at(i.rotate(random.choice([0, 5, -5, 10, -10, 30, -30, 45, -45])),round(random.uniform(62,189)),round(random.uniform(62,189)), random.uniform(1.3,1.6))
                i.save(r"C:/Users/52551/Desktop/assignment acne severity classification/assignment acne severity classification/imagesdata1/data/healthy/{}_{}".format(k,fn))
                
        
           
