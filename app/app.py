
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""




from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image_file']
        api_key = 'AIzaSyAYzJh5GO_NXQUb0LNl5y1zWhrqoanmPpE'
        cx = '24182732d347e4550'

        result = search_product_image(image_file, api_key, cx)
        
        # Process result to extract store and price information

        return render_template('index.html', results=extract_results)

    return render_template('index.html', results=None)

def search_product_image(image_file, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "searchType": "image",
    }



    files = {"imgFile": (image_file.filename, image_file.stream, image_file.content_type)}
    print("Filename:", image_file.filename)
    print("Content-Type:", image_file.content_type)

    headers = {"Content-Type": "multipart/form-data"}
    response = requests.post(base_url, params=params, files=files, headers=headers)
    
    # response = requests.post(base_url, params=params, files=files)
    print("*"*10)
    print(response.text)  # Print the response content for debugging
    print("*"*10)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)



    return data



def extract_results(data):
    items = data.get('items', [])
    extracted_results = []

    for item in items:
        title = item.get('title', '')
        link = item.get('link', '')
        extracted_results.append((title, link))

    return extracted_results


if __name__ == '__main__':
    app.run()


