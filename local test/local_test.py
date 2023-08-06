
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""


from serpapi import GoogleSearch
import pandas as pd 
import requests

def upload_image_to_imgbb(image_path, api_key):
    url = "https://api.imgbb.com/1/upload"
    files = {"image": (image_path, open(image_path, "rb"))}
    params = {"key": api_key}
    
    response = requests.post(url, files=files, params=params)
    data = response.json()
    
    return data.get("data", {}).get("url")


api_key = "fe4095abd2b2d313d039c4d7e28fb628"
# image_path = "pen.jpg"
# image_path = "swim.png"
image_path = "D:\GitHub\product_searcher\local test\pen.jpg"



try:
    url = upload_image_to_imgbb(image_path, api_key)
    print(f"Uploaded image URL: {url}")

except Exception as e:
    url = ""
    print("Error:", e)

if url != "":
        
    params = {
      "engine": "google_lens",
      "url": url,
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
                {"source": item['source'] if 'source' in list(item.keys()) else None,
                 "title":item['title'] if 'title' in list(item.keys()) else None,
                 "link":item['link'] if 'link' in list(item.keys()) else None,
                 "price":item['price']['extracted_value'] if 'price' in list(item.keys()) else None,
                 "currency":item['price']['currency'] if 'price' in list(item.keys()) else None,
                 "thumbnail":item['thumbnail'] if 'thumbnail' in list(item.keys()) else None,
                 }]
    
    
    df = pd.DataFrame(name_price_url)
    filtered_df = df[df['link'].notnull()]
    filtered_df = df[df['currency'].notnull()]
    filtered_df = filtered_df.sort_values(by='price')
    filtered_df = filtered_df.reset_index()
    filtered_df = filtered_df[["source","link","price"]]


