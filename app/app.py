
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
        image_url = request.form['image_url']
        api_key = 'AIzaSyAYzJh5GO_NXQUb0LNl5y1zWhrqoanmPpE'
        cx = '24182732d347e4550'

        result = search_product_image(image_url, api_key, cx)
        # Process result to extract store and price information

        return render_template('index.html', results=extracted_results)

    return render_template('index.html', results=None)

def search_product_image(image_file, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "searchType": "image",
    }

    files = {"imgFile": (image_file.filename, image_file.stream, image_file.content_type)}

    response = requests.post(base_url, params=params, files=files)
    data = response.json()

    return data



def extract_results(data):
    # Implement the result extraction here
    print("extract_results")

if __name__ == '__main__':
    app.run()


















































