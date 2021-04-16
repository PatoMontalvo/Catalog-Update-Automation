import os
import requests
import json

dir = r"/home/student-02-1c64a6f43871/supplier-data/descriptions/"  #Source directory
list_dir = os.listdir(dir)
upload_file = {
               "name": 0,
               "weight": 0,
               "description": 0,
               "image_name": 0
}


def process_info(location, list):
  #Pairs and uploads the description information of each image
  for dp in list:
    if ".txt" in dp:
      with open(dir + dp, "r" ) as f:
        lines = f.readlines()
        upload_file["name"] = lines[0]
        upload_file["weight"] = int(lines[1].strip(" lbs\n"))
        upload_file["description"] = lines[2]
        upload_file["image_name"] = dp.strip(".txt") + ".jpeg"
        response = requests.post("http://35.226.0.255/fruits/", data = upload_file)
    else:
      pass
  return response

response = process_info(dir, list_dir)
print(response)
print(response.raise_for_status())