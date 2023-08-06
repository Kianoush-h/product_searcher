
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""


from flask import Flask, render_template, request
from serpapi import GoogleSearch
import pandas as pd
import requests
import os

app = Flask(__name__)

def upload_image_to_imgbb(image_path, api_key):
    url = "https://api.imgbb.com/1/upload"
    files = {"image": (image_path, open(image_path, "rb"))}
    params = {"key": api_key}
    
    response = requests.post(url, files=files, params=params)
    data = response.json()
    
    return data.get("data", {}).get("url")




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file:
                image_filename = file.filename
                # image_path = os.path.join(os.getcwd(), image_filename)
                image_path = os.path.join(image_folder, image_filename)
                file.save(image_path)
                
                api_key = "fe4095abd2b2d313d039c4d7e28fb628"
                url = upload_image_to_imgbb(image_path, api_key)
                
                
                if url:
                    params = {
                        "engine": "google_lens",
                        "url": url,
                        "no_cache": "true",
                        "api_key": "21821398356fa120a0910724c0df63944cffc73bff0d13f4db1485ae1c75d3d4",
                    }

                    search = GoogleSearch(params)
                    results = search.get_dict()

                    name_price_url = []

                    important_keys = ["source", "title", "price", "thumbnail"]

                    if results['search_metadata']['status'] != "Success":
                        print("no item found")
                    else:
                        for item in results['visual_matches']:
                            name_price_url.append({
                                "source": item.get('source'),
                                "title": item.get('title'),
                                "link": item.get('link'),
                                "price": item['price'].get('extracted_value') if 'price' in item else None,
                                "currency": item['price'].get('currency') if 'price' in item else None,
                                "thumbnail": item.get('thumbnail')
                            })

                    df = pd.DataFrame(name_price_url)
                    filtered_df = df[df['link'].notnull()]
                    filtered_df = df[df['currency'].notnull()]
                    filtered_df = filtered_df.sort_values(by='price')
                    filtered_df = filtered_df.reset_index()
                    filtered_df = filtered_df[["source","link","price"]]
                    
                    filtered_df.to_csv("results.csv", index=False)

                    return render_template('index.html', data=filtered_df.to_dict('records'), image=image_filename)
                else:
                    return "Error uploading image... retry again :)"

        except Exception as e:
            return f"Error: {e}"

    return render_template('index.html', data=[])

if __name__ == '__main__':
    image_folder = "uploads"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    app.run()
