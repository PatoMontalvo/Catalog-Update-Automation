!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"    #web-page destination
dir = r"/home/student-02-1c64a6f43871/supplier-data/images/" #Images source directory
list_dir = os.listdir(dir) #trasnforms directory to a list

def upload_images(location, list):
  #uploads images in source directory to the desired web-page destination
  for img in list:
    if ".jpeg" in img:
      with open(location + img, 'rb') as opened:
       r = requests.post(url, files={'file': opened})

upload_images(dir, list_dir)