import requests

from flask import Flask

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

# [moved code lower]

# need to branch out into classes

# API endpoint
url = "https://api.scryfall.com/cards/named?exact=lightning+bolt "

# GET request to the API
response = requests.get(url)

@app.route('/')
@app.route('/hello')
def hello():
   # Render the page
   return "Response: " + str(response.status_code)

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449) 