
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""


from serpapi import GoogleSearch

params = {
  "engine": "google_lens",
  "url": "https://i.ibb.co/pZStwWw/pen.jpg",
  "no_cache": "true",
  "api_key": "21821398356fa120a0910724c0df63944cffc73bff0d13f4db1485ae1c75d3d4"
}

search = GoogleSearch(params)
results = search.get_dict()

name_price_url = []

important_keys = ["source","title","price","thumbnail"]

if results['search_metadata']['status'] != "Success":
    print("no item found")
else:
    for item in results['visual_matches']:
        
        name_price_url += [
            {"source": item['source'],
             "title":item['title'],
             "price":item['price']['value'],
             "thumbnail":item['thumbnail']}]




#%%

import requests
import time

def upload_image_to_imgbb(image_path, api_key):
    url = "https://api.imgbb.com/1/upload"
    files = {"image": (image_path, open(image_path, "rb"))}
    params = {"key": api_key}
    
    response = requests.post(url, files=files, params=params)
    data = response.json()
    
    return data.get("data", {}).get("url")

if __name__ == "__main__":
    api_key = "fe4095abd2b2d313d039c4d7e28fb628"
    image_path = "pen.jpg"

    try:
        url = upload_image_to_imgbb(image_path, api_key)
        print(f"Uploaded image URL: {url}")

    except Exception as e:
        print("Error:", e)