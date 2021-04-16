#!/usr/bin/env python3

from PIL import Image
import os

source_dir = r"/home/student-02-1c64a6f43871/supplier-data/images/"   #Location of files
image_dir = os.listdir(source_dir)   #transforms source directory to list
size = 600, 400   #desired size


def process_images(dir):
  #Transforms Image from ".tiff" format to ".JPEG", re-sizes to (600 x 400) and saves it to selected directory
  for img in dir:
    if ".tiff" in img:
      im = Image.open(source + img)
      im.convert("RGB").resize(size).save(source_dir + img.replace(".tiff",".jpeg"), "JPEG")
    else:
      pass

process_images(image_dir)