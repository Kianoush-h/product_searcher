# Product Search Web App

![Product Search App](app_screenshot.png)

This project is a simple web application built with Python and Flask that allows users to upload a picture of a product, such as a pen, and then performs a Google image search to find stores that sell the product. The app then extracts and presents a list of stores along with their prices for the identified product.

## Features

- **User-Friendly Interface**: The web app provides an intuitive user interface where users can easily upload product images and initiate searches.

- **Google Custom Search**: Utilizes the Google Custom Search JSON API to perform image searches based on the uploaded picture's URL.

- **Result Extraction**: Extracts relevant information from the search results, including store names and prices for the identified product.

- **Responsive Design**: The app's responsive design ensures a seamless experience across various devices and screen sizes.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/product-search-app.git`

2. Install the required packages: `pip install -r requirements.txt`

3. Obtain a Google API Key and Custom Search Engine ID and replace them in the `app.py` file.

4. Run the application: `python app.py`

5. Open your web browser and navigate to `http://localhost:5000` to use the app.

## Screenshots

![Upload Page](screenshots/upload_page.png)
*Upload Page*

![Results Page](screenshots/results_page.png)
*Results Page*

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`

3. Make your changes and commit them: `git commit -m 'Add some feature'`

4. Push your changes to your fork: `git push origin feature-name`

5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the description further to match the specific details and features of your project. Also, make sure to add relevant screenshots of your web app to the repository and update the image URLs in the README accordingly.