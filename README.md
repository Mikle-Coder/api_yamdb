# YaMDb API Project

## Description
The YaMDb project is an API built using Django REST framework for collecting user reviews and ratings on various works, including books, movies, and music. Works are categorized into different genres, and new genres can be created by administrators. Users can leave text reviews and rate works on a scale from one to ten, and the system calculates the average rating for each work.

The primary purpose of this project is to provide a platform for users to review and rate different works across categories and to explore the capabilities of the Django REST framework.

## Installation
To deploy this project on your local machine, follow these steps:
1. Ensure you have Python and pip installed.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install the required modules from the `requirements.txt` file by running the following command:
```
pip install -r requirements.txt
```
5. Start the project using the following command to make migrations, migrate, and run server:
```
python3 deploy.py
```
## Examples
You can find examples of API requests and responses by accessing the API documentation at [http://localhost:8000/redoc/](http://localhost:8000/redoc/). This documentation provides detailed information on available endpoints and how to interact with them.

Enjoy using the YaMDb API for collecting and sharing reviews on a wide range of works!